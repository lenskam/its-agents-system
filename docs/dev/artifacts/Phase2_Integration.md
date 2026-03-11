# Phase 2: Core Agents — Implementation Plan

> **Parent**: [task.md](file:///home/kamdemlens/.gemini/antigravity/brain/7251f1e7-d16c-49b6-ba55-c1a1af7b1dc7/task.md) → Phase 2  
> **Depends on**: [Phase 1](file:///home/kamdemlens/.gemini/antigravity/brain/7251f1e7-d16c-49b6-ba55-c1a1af7b1dc7/phase1_foundation.md) (base agent, LLM layer, Odoo client)  
> **Timeline**: Days 6-10 (Week 2)  
> **Goal**: Security Agent (daily audit) + Support N1 Agent (FAQ + Helpdesk integration)

---

## Proposed Changes

### 2.1 Agent Sécurité (Days 6-7)

Automated daily security audit of Odoo instances.

#### [NEW] [agents/security/agent.py](file:///home/kamdemlens/ITS/its-agents-system/agents/security/agent.py)

```python
# SecurityAgent(BaseAgent):
#   - execute(task_input) -> AgentResult
#     Runs full security audit for a client, generates report
#   - audit_accounts(client_id) -> list[SecurityFinding]
#   - audit_privilege_escalation(client_id) -> list[SecurityFinding]
#   - audit_separation_of_duties(client_id) -> list[SecurityFinding]
#   - generate_report(findings) -> ReportOutput (HTML/PDF)
#
# SecurityFinding:
#   - severity: "critical" | "warning" | "info"
#   - category: str (e.g. "orphan_account", "privilege_escalation")
#   - description: str
#   - affected_users: list[str]
#   - recommendation: str (LLM-generated via Ollama — confidential data)
```

Audit checks:

1. **Orphan accounts** — Users active in Odoo but not in HR/company directory
2. **Stale accounts** — No login for 90+ days but still active
3. **Privilege escalation** — Users in admin/settings groups without justification
4. **Separation of Duties (SoD)** — Forbidden combinations (e.g., create supplier + validate invoice)
5. **Offboarding compliance** — Departed employees still active

#### [NEW] [agents/security/audits.py](file:///home/kamdemlens/ITS/its-agents-system/agents/security/audits.py)

Individual audit functions, each using `OdooClient.search_read()` to query users, groups, access rights.

#### [NEW] [agents/security/reports.py](file:///home/kamdemlens/ITS/its-agents-system/agents/security/reports.py)

Jinja2 template → HTML report. Optional PDF via `weasyprint` or plain HTML file.

#### [NEW] [agents/security/templates/security_report.html](file:///home/kamdemlens/ITS/its-agents-system/agents/security/templates/security_report.html)

HTML template with severity-colored findings, summary stats, recommendations.

---

### 2.2 Agent Support N1 (Days 8-10)

FAQ-based intelligent support with Odoo Helpdesk integration.

#### [NEW] [agents/support/agent.py](file:///home/kamdemlens/ITS/its-agents-system/agents/support/agent.py)

```python
# SupportAgent(BaseAgent):
#   - execute(task_input) -> AgentResult
#     Receives question, searches knowledge base, synthesizes answer
#   - search_knowledge(query: str) -> list[KnowledgeEntry]
#     Text search across markdown FAQ files (TF-IDF or simple keyword match)
#   - synthesize_answer(query: str, relevant_entries: list) -> str
#     Uses LLM (Gemini Flash — FAQ content is not confidential) to compose answer
#   - categorize_ticket(ticket_text: str) -> TicketCategory
#     Classification: billing, technical, access, feature_request, other
```

#### [NEW] [agents/support/knowledge/](file:///home/kamdemlens/ITS/its-agents-system/agents/support/knowledge/)

Directory of markdown files, each representing a FAQ entry:

```
knowledge/
├── 01_password_reset.md        # "Comment réinitialiser mon mot de passe ?"
├── 02_invoice_creation.md      # "Comment créer une facture dans Odoo ?"
├── 03_stock_reception.md       # "Procédure de réception de stocks"
├── ...
└── index.json                  # Pre-computed search index
```

Each file format:

```markdown
---
title: Comment réinitialiser mon mot de passe Odoo ?
tags: [password, login, access, reset]
category: access
---

## Procédure

1. Aller sur la page de connexion Odoo
2. Cliquer sur "Mot de passe oublié"
   ...
```

#### [NEW] [agents/support/helpdesk.py](file:///home/kamdemlens/ITS/its-agents-system/agents/support/helpdesk.py)

```python
# HelpdeskIntegration:
#   - get_open_tickets(client_id) -> list[Ticket]
#     Via OdooClient: search_read on helpdesk.ticket model
#   - suggest_response(ticket: Ticket) -> str
#     Calls SupportAgent.execute() with ticket description
#   - update_ticket_note(ticket_id, suggestion) -> bool
#     Writes AI suggestion as internal note on ticket
```

#### [NEW] API routes for support

```python
# api/routes/support.py
# POST /api/agents/support/ask  — body: {"question": "...", "client_id": "..."}
# GET  /api/agents/support/tickets?client_id=... — List open tickets with AI suggestions
```

---

## Verification Plan

### Automated Tests

```bash
uv run pytest tests/unit/test_security.py tests/unit/test_support.py -v
```

| Test                            | What It Covers                                   |
| ------------------------------- | ------------------------------------------------ |
| `test_orphan_account_detection` | Mock Odoo users → detect orphans                 |
| `test_sod_violations`           | Mock user groups → detect forbidden combinations |
| `test_report_generation`        | Generate HTML from mock findings                 |
| `test_knowledge_search`         | Search markdown FAQ, assert ranked results       |
| `test_answer_synthesis`         | Mock LLM → compose answer from FAQ entries       |
| `test_ticket_categorization`    | Classify sample ticket texts                     |

### Manual Verification

1. **Security audit on real client**: `uv run python -m agents.security.agent --client=<id> --once`
2. **Support ask**: `curl -X POST http://localhost:8000/api/agents/support/ask -d '{"question":"Comment réinitialiser mon mot de passe?"}' -H 'Content-Type: application/json'`
