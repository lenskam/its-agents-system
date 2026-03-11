# ITS Agents System MVP — Master Task Tracker

> **Parent**: [synthese_projet_its.md](file:///home/kamdemlens/.gemini/antigravity/brain/7251f1e7-d16c-49b6-ba55-c1a1af7b1dc7/synthese_projet_its.md)
> **Scope**: 5 agents MVP (Monitoring, Sécurité, Support N1, Reporting, Orchestrateur)
> **Deadline**: 3 weeks from 07/03/2026
> **Hardware**: 16GB RAM, Celeron 4305U (2C/2T), no GPU

---

## Phase 1: Foundation Setup (S1 — Days 1-5)

> Plan: [phase1_foundation.md](file:///home/kamdemlens/.gemini/antigravity/brain/7251f1e7-d16c-49b6-ba55-c1a1af7b1dc7/phase1_foundation.md)

### 1.1 Project Scaffold & Infrastructure

- [/] Create project structure, `pyproject.toml`, dependencies
- [ ] Docker Compose (PostgreSQL, Redis, Ollama)
- [ ] Environment config (`.env`, `config.py`)

### 1.2 LLM Integration Layer

- [ ] Benchmark Ollama models on Celeron (Phi-3 mini, Gemma 2B, TinyLlama)
- [ ] `common/llm.py` — Smart routing: Gemini Flash (primary) + Ollama (confidential data)
- [ ] Unit tests for LLM wrapper

### 1.3 Odoo Client & Multi-tenant Foundation

- [ ] `common/odoo_client.py` — XML-RPC client, multi-instance, per-client config
- [ ] Client config YAML structure (`clients/*.yml`)
- [ ] Unit tests for Odoo client

### 1.4 Base Agent Framework + API Skeleton

- [ ] `agents/base.py` — Abstract BaseAgent class
- [ ] FastAPI skeleton (`api/main.py`, health endpoint)
- [ ] Database models (asyncpg/SQLAlchemy)

### 1.5 Agent Monitoring

- [ ] `agents/monitoring/` — Health checks (ping, CPU, RAM, disk, Odoo status)
- [ ] Alerting module (email + Telegram)
- [ ] Cron scheduling
- [ ] Integration test on 1 client

---

## Phase 2: Core Agents (S2 — Days 6-10)

> Plan: phase2_core_agents.md (to be created)

### 2.1 Agent Sécurité

- [ ] `agents/security/` — Odoo account audit (orphans, privilege escalation, SoD)
- [ ] Report generation (HTML/PDF via Jinja2)
- [ ] Daily cron schedule (6h)
- [ ] Tests

### 2.2 Agent Support N1

- [ ] `agents/support/knowledge/` — Markdown FAQ base (20-30 entries)
- [ ] RAG-lite: text search + LLM synthesis
- [ ] Odoo Helpdesk integration (read tickets, suggest responses)
- [ ] API endpoint `/agents/support/ask`
- [ ] Tests

---

## Phase 3: Integration & Dashboard (S3 — Days 11-15)

> Plan: phase3_integration.md (to be created)

### 3.1 Agent Reporting

- [ ] `agents/reporting/` — Metrics collection, Jinja2 templates, PDF/HTML output
- [ ] Scheduled monthly generation
- [ ] Tests

### 3.2 Orchestrateur Simple

- [ ] FastAPI routing to agents by request type
- [ ] `/orchestrator/chat` endpoint
- [ ] Request/response logging

### 3.3 Dashboard Web Minimal

- [ ] React app setup (Vite)
- [ ] Page 1: MetricCards + activity chart
- [ ] Page 2: Logs + agent status
- [ ] API integration

### 3.4 Demo Prep & Polish

- [ ] End-to-end testing
- [ ] Documentation
- [ ] Demo script for direction

---

## Post-MVP (Month 2+)

- [ ] Qdrant vector DB for knowledge base
- [ ] Telegram bot (advanced)
- [ ] WhatsApp integration
- [ ] Dashboard React complet
- [ ] LangGraph evaluation
- [ ] Additional agents (Dev Odoo, DevOps, etc.)
- [ ] Flutter mobile app
