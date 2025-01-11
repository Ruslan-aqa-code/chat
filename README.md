# FastAPI + Kafka = Application with chat

This is a basic template for Django projects configured to use Docker Compose, Makefile, and PostgreSQL.
## Requirements

    Docker
    Docker Compose
    GNU Make

## How to Use

1. **Clone the repository**:

    git clone https://github.com/your_username/your_repository.git
    cd your_repository

2.  Install all required packages in Requirements section.

### Implemented Commands

    make app - up application and database/infrastructure
    make app-logs - follow the logs in app container
    make app-down - down application and all infrastructure
    make app-shell - go to containerized interactive shell (bash)

### Most Used Django Specific Commands

    make migrations - make migrations to models
    make migrate - apply all made migrations
    make collectstatic - collect static
    make superuser - create admin user
    make test - run tests with pytest
