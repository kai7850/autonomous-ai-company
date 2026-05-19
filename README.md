# Autonomous AI Company

Multi-agent autonomous AI company framework - CEO, Research, Content, and Execution agents operating in a fully automated pipeline.

## Architecture

- **FastAPI** - RESTful API service
- **Celery + Redis** - Async task queue for agent orchestration
- **PostgreSQL** - Persistent data storage
- **Multi-Agent Pipeline** - CEO > Research > Content > Execution

## Agent Pipeline

1. **CEO Agent** - Decomposes business goals into actionable tasks, prioritizes work items, and coordinates sub-agents
2. **Research Agent** - Autonomous market research, trend analysis, and competitive intelligence gathering
3. **Content Agent** - AI-driven content creation, optimization, and multi-platform publishing
4. **Execute Agent** - Task execution, result collection, and feedback loop for continuous improvement

## Quick Start

```bash
cp .env.example .env  # Configure your API keys
docker-compose up -d
```

## Use Cases

- Automated social media content operations
- Market research and competitive analysis
- Content generation and schedule management
- Data-driven business decision support

## Tech Stack

**Backend:** Python 3.11+, FastAPI, Celery, Redis, PostgreSQL
**AI:** Multi-LLM orchestration, RAG pipeline, Agentic workflows
**Infra:** Docker Compose, async task queue, RESTful API

## License

MIT
