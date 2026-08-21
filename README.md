# Python Web App

A hands-on study repo for learning modern Python web application conventions and best practices. This is a growing sandbox — new tools, patterns, and examples will be added as I learn them.

## 🎯 Goals

- Understand idiomatic project structure for Python web apps
- Learn how core tools fit together in a real workflow (not just in isolation)
- Build small, focused examples rather than one big monolith
- Document conventions and gotchas as I discover them

## 🧰 Tech Stack

| Tool                                      | Purpose                                  |
| ----------------------------------------- | ---------------------------------------- |
| [FastAPI](https://fastapi.tiangolo.com/)   | Web framework / API layer                |
| [SQLAlchemy](https://www.sqlalchemy.org/)  | ORM / database layer                     |
| [Alembic](https://alembic.sqlalchemy.org/) | Database migrations                      |
| [Docker](https://www.docker.com/)          | Containerization / local dev environment |

> More tools will be added here as the project grows (e.g. testing, linting, CI/CD, auth, etc.)

## 📁 Project Structure

```
.
├── app/                # Application source code
│   ├── api/            # Route definitions / endpoints
│   ├── models/         # SQLAlchemy models
│   ├── schemas/         # Pydantic schemas
│   └── core/            # Config, settings, dependencies
├── alembic/             # Migration scripts
├── tests/               # Test suite
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

*(Structure will evolve as the project develops — treat this as a living reference, not a fixed spec.)*

## 🚀 Getting Started

```bash
# Clone the repo
git clone <repo-url>
cd <repo-name>

# Build and run with Docker
docker compose up --build
```

*(Setup instructions will be filled in as the environment is configured.)*

## 📝 Notes & Learnings

This section will collect useful patterns, conventions, and lessons learned along the way — things like:

- Project layout conventions
- Migration workflow tips
- Dependency injection patterns in FastAPI
- Environment/config management

## 🗺️ Roadmap

- [ ] Basic FastAPI app skeleton
- [ ] SQLAlchemy models + database connection
- [ ] Alembic migrations set up
- [ ] Dockerize the app
- [ ] Add testing setup
- [ ] Add CI/CD pipeline
- [ ] More TBD as I go

---

*This is a personal learning project — structure and conventions will change as understanding improves.*
