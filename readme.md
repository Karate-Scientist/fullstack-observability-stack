# 🐳 Dockerized Full-Stack App with Datadog Observability

A containerized full-stack application built to demonstrate production-grade Docker skills — multi-service orchestration, real-time log streaming, APM tracing, and operational monitoring via Datadog.

> Built as a hands-on project by an 8+ year Support/Platform Engineer to sharpen container and observability skills in a real-world setup.

---

## 🧱 Architecture

```
┌─────────────────────────────────────────────────┐
│                  Docker Network                  │
│                                                  │
│  ┌──────────────┐     ┌──────────────────────┐  │
│  │   Frontend   │────▶│   Backend (Python)   │  │
│  │  HTML/JS/CSS │     │   Flask/FastAPI       │  │
│  └──────────────┘     └──────────┬───────────┘  │
│                                  │               │
│                        ┌─────────▼──────────┐   │
│                        │   PostgreSQL DB     │   │
│                        └─────────────────────┘   │
│                                                  │
│  ┌────────────────────────────────────────────┐  │
│  │         Datadog Agent (sidecar)            │  │
│  │   Logs · APM Traces · Infra Metrics        │  │
│  └────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────┘
```

### Services
| Service | Technology | Purpose |
|---|---|---|
| `frontend` | HTML / JavaScript / CSS | User interface served via container |
| `backend` | Python | Business logic, DB queries, API endpoints |
| `db` | PostgreSQL | Persistent data storage |
| `datadog-agent` | Datadog Agent | Log collection, APM tracing, infra metrics |

---

## 🎯 What This Project Demonstrates

- **Docker Compose** orchestration of a multi-service stack
- **Inter-container networking** — frontend → backend → DB communication
- **APM instrumentation** — distributed traces flowing into Datadog
- **Log streaming** — structured container logs ingested and parsed in Datadog
- **Monitors & Dashboards** — alerting rules and visualisations built in Datadog
- **Environment variable management** — secrets/config passed via `.env`, never hardcoded

---

## 📊 Datadog Observability Setup

### Logs
- All services emit structured logs captured by the Datadog Agent
- Logs are tagged by `service`, `env`, and `container_name`
- Log pipelines parse and enrich backend error/warning events

### APM
- Backend is instrumented with `ddtrace` to capture request traces
- Flame graphs show end-to-end latency from frontend request → DB query

### Monitors
- **Error rate spike** — alerts when backend 5xx responses exceed threshold
- **DB connectivity** — alerts if PostgreSQL becomes unreachable
- **Container health** — alerts on unexpected container restarts

---

## 🚀 Getting Started

### Prerequisites
- Docker + Docker Compose installed
- Datadog account (free trial works) with an API key

### Setup

```bash
# 1. Clone the repo
git clone https://github.com/Karate-Scientist/fullstack-observability-stack.git
cd fullstack-observability-stack

# 2. Create your environment file
cp .env.example .env
# Add your DD_API_KEY and DD_SITE to .env

# 3. Spin up all services
docker-compose up --build

# 4. Open the app
# Frontend: http://localhost:3000
# Backend API: http://localhost:5000
```

### Environment Variables
```
DD_API_KEY=your_datadog_api_key
DD_SITE=datadoghq.com         # or datadoghq.eu
POSTGRES_USER=admin
POSTGRES_PASSWORD=secret
POSTGRES_DB=appdb
```

---

## 📁 Project Structure

```
docker_refresh/
├── frontend/
│   ├── index.html
│   ├── app.js
│   └── styles.css
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
└── .env.example
```

---

## 🔍 Key Technical Decisions

**Why a sidecar Datadog agent instead of host-level install?**
Keeping the agent containerized means the entire observability stack is portable and reproducible — any engineer can clone this and have full monitoring running in minutes with just a DD API key.

**Why PostgreSQL instead of SQLite?**
Simulates a real production database setup. Also allows demonstrating DB connection pool monitoring via Datadog's postgres integration.

---

## 📌 What I'd Add Next

- [ ] Add health check endpoints to all services
- [ ] Wire Datadog RUM (Real User Monitoring) into the frontend
- [ ] Add CI/CD pipeline (GitHub Actions) to build and validate containers on push
- [ ] Integrate with the [Incident Triage Engine](https://github.com/Karate-Scientist/incident-triage) to auto-ingest Datadog alert payloads

---

## 🛠 Tech Stack

`Docker` · `Docker Compose` · `Python` · `PostgreSQL` · `HTML/JS/CSS` · `Datadog APM` · `Datadog Logs` · `ddtrace`

---

## 👤 Author

**Karate-Scientist** — Support/Platform Engineer with 8+ years in production systems, currently building toward Data & Analytics Engineering.

[GitHub Profile](https://github.com/Karate-Scientist)
