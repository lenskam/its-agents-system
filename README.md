# ITS Agents System

Multi-Agent AI System for Odoo Operations — MVP

## Quick Start

### Prerequisites
- Python 3.11+
- Docker & Docker Compose
- [uv](https://docs.astral.sh/uv/) (Python package manager)

### Setup

```bash
# 1. Clone and enter project
cd its-agents-system

# 2. Copy environment template
cp .env.example .env
# Edit .env with your actual values (Gemini API key, Telegram token, etc.)

# 3. Start infrastructure
docker compose up -d

# 4. Install Python dependencies
uv sync

# 5. Pull Ollama model (for confidential data processing)
docker exec its-ollama ollama pull phi3:mini

# 6. Run tests
uv run pytest tests/ -v

# 7. Start API server
uv run uvicorn api.main:app --reload --host 0.0.0.0 --port 8000

# 8. Verify
curl http://localhost:8000/health
```

### Client Configuration

Add a YAML file per client in `clients/`:
```bash
cp clients/example_client.yml clients/my_client.yml
# Edit with real Odoo connection details
```

## Architecture

```
Gemini Flash (primary) ←→ LLM Router ←→ Ollama Phi-3 (confidential)
                              ↓
                         BaseAgent
                     ↙    ↓    ↓    ↘
              Monitoring Security Support Reporting
                  ↓         ↓       ↓        ↓
              Telegram   Reports   FAQ    PDF/HTML
```

## MVP Agents (Phase 1)

| Agent | Status | Description |
|-------|--------|-------------|
| Monitoring | 🚧 | Infrastructure health checks + Telegram alerts |
| Security | 📋 | Daily Odoo account/rights audit |
| Support N1 | 📋 | FAQ-based AI support + Helpdesk integration |
| Reporting | 📋 | Automated monthly reports |
| Orchestrator | 📋 | Simple request routing |

## License

Private — ITS Internal Use Only
