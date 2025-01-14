# Docker Setup Plan

## Container Structure
```
docker-compose.yml
├── backend/
│   ├── Dockerfile
│   └── src/
├── postgres/
│   └── init.sql
└── pgadmin/ (development only)
```

## Development Setup

### Backend Dockerfile
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies and Rye
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/* \
    && curl -sSf https://rye-up.com/get | bash \
    && echo 'source "$HOME/.rye/env"' >> ~/.bashrc

# Copy Rye configuration
COPY pyproject.toml .
COPY README.md .

# Install dependencies
RUN source "$HOME/.rye/env" && rye sync

# Copy application
COPY . .

# Run the application
CMD ["sh", "-c", "source $HOME/.rye/env && rye run uvicorn studenhexe.main:app --host 0.0.0.0 --port 8000 --reload"]
```

### Docker Compose
```yaml
version: '3.8'

services:
  backend:
    build: 
      context: ./backend
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    volumes:
      - ./backend:/app
      - rye_cache:/root/.rye/cache  # Cache Rye packages
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/studenhexe
      - ENVIRONMENT=development
    depends_on:
      - db

  db:
    image: postgres:15
    ports:
      - "5432:5432"
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=studenhexe
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./postgres/init.sql:/docker-entrypoint-initdb.d/init.sql

  pgadmin:
    image: dpage/pgadmin4
    ports:
      - "5050:80"
    environment:
      - PGADMIN_DEFAULT_EMAIL=admin@studenhexe.com
      - PGADMIN_DEFAULT_PASSWORD=admin
    depends_on:
      - db

volumes:
  postgres_data:
  rye_cache:  # Persistent Rye cache
```

## Development Workflow
1. Build images: `docker-compose build`
2. Start services: `docker-compose up -d`
3. View logs: `docker-compose logs -f`
4. Access services:
   - Backend: http://localhost:8000
   - PgAdmin: http://localhost:5050
5. Stop services: `docker-compose down`

## Common Operations

### Adding Dependencies
```bash
# Enter container
docker-compose exec backend bash

# Add dependency
source ~/.rye/env
rye add package_name

# Sync dependencies
rye sync
```

### Running Tests
```bash
docker-compose exec backend bash -c "source ~/.rye/env && rye run test"
```

### Code Formatting
```bash
docker-compose exec backend bash -c "source ~/.rye/env && rye run format"
```

## Next Steps
1. [ ] Create Dockerfile with Rye setup
2. [ ] Create docker-compose.yml
3. [ ] Setup PostgreSQL init script
4. [ ] Configure environment variables
5. [ ] Test full stack locally
6. [ ] Document common operations 