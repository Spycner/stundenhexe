# Studenhexe Backend

FastAPI backend for the School Timetable Planning System.

## Development Setup

### Prerequisites
- Python 3.11+
- [Rye](https://rye-up.com/guide/installation/)
- Docker and Docker Compose (optional)

### Local Development
1. Install dependencies:
   ```bash
   rye sync
   ```

2. Activate virtual environment:
   ```bash
   rye shell
   ```

3. Run development server:
   ```bash
   uvicorn studenhexe.main:app --reload
   ```

### Docker Development
1. Build and start services:
   ```bash
   docker-compose up -d
   ```

2. View logs:
   ```bash
   docker-compose logs -f
   ```

3. Access services:
   - API: http://localhost:8000
   - API Docs: http://localhost:8000/docs
   - PgAdmin: http://localhost:5050

### Common Tasks

#### Code Quality
```bash
# Format code
rye run ruff format .

# Check code
rye run ruff check .

# Fix auto-fixable issues
rye run ruff check . --fix

# Type checking
rye run mypy .

# Run tests
rye run pytest
```

#### Database
```bash
# Create migration
rye run alembic revision --autogenerate -m "description"

# Run migrations
rye run alembic upgrade head
```

## Project Structure
```
src/studenhexe/
├── api/           # API routes
├── core/          # Core functionality
├── db/            # Database
├── models/        # SQLAlchemy models
├── schemas/       # Pydantic schemas
└── services/      # Business logic
```

## Code Style
We use [ruff](https://github.com/astral-sh/ruff) for code formatting and linting. Key configurations:
- Line length: 100 characters
- Quote style: double quotes
- Docstring style: Google
- Python version: 3.11+

See `pyproject.toml` for full configuration details.
