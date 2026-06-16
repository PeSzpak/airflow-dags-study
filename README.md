# airflow-dags-study

Apache Airflow 3.x study project — DAG examples and workflow orchestration experiments running via Docker Compose with CeleryExecutor.

## Stack

- **Apache Airflow 3.1** (CeleryExecutor)
- **PostgreSQL 16** — metadata database
- **Redis 7.2** — Celery broker
- **Docker Compose** — full local environment

## DAGs

| File | DAG ID | Concept |
|---|---|---|
| `1.PrimeiraDag.py` | `primeira_dag` | Sequential tasks with BashOperator |
| `2.segundaDag.py` | `segunda_dag` | Parallel tasks (fan-out pattern) |
| `3.TerceiraDag.py` | `terceira_Dag` | Multiple upstream tasks merging into one |
| `demo.py` | `Demo` | Advanced: BranchPythonOperator, TriggerRule, fan-out/fan-in |

### DAG Patterns covered

- **Sequential** — `task1 >> task2 >> task3`
- **Parallel (fan-out)** — `task1 >> [task2, task3] >> task4`
- **Branching** — `BranchPythonOperator` choosing between two paths at runtime
- **Trigger Rules** — `ONE_FAILED`, `ALL_DONE`, `ALL_DONE_MIN_ONE_SUCCESS`
- **Intentional failure** — branch A always fails to demonstrate error handling flow

## Getting started

### Prerequisites

- Docker + Docker Compose
- At least 4 GB RAM and 2 CPUs available

### Setup

```bash
# 1. Set your user ID (Linux only)
echo -e "AIRFLOW_UID=$(id -u)" > .env

# 2. Initialize the database
docker compose up airflow-init

# 3. Start all services
docker compose up -d

# 4. Open the Airflow UI
open http://localhost:8080
# Default credentials: airflow / airflow
```

### Stopping

```bash
docker compose down
# To also remove volumes (reset database):
docker compose down --volumes
```

## Project structure

```
airflow-project/
├── dags/                   ← DAG files (auto-loaded by Airflow)
│   ├── 1.PrimeiraDag.py
│   ├── 2.segundaDag.py
│   ├── 3.TerceiraDag.py
│   └── demo.py
├── config/
│   └── airflow.cfg         ← custom Airflow config
├── logs/                   ← task execution logs (auto-generated)
├── plugins/                ← custom plugins (empty)
└── docker-compose.yaml
```

## License

MIT © [Pedro Szpak](https://github.com/PeSzpak)
