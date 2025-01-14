# Backend Development Plan

## Project Setup with Rye 🛠️

### Initialize Project
```bash
rye init backend
cd backend
rye pin 3.11
```

### Dependencies in pyproject.toml
```toml
[project]
name = "studenhexe-backend"
version = "0.1.0"
description = "School timetable planning system backend"
dependencies = [
    "fastapi>=0.104.0",
    "uvicorn>=0.24.0",
    "sqlalchemy>=2.0.23",
    "alembic>=1.12.1",
    "pydantic>=2.5.0",
    "psycopg2-binary>=2.9.9",
    "python-jose[cryptography]>=3.3.0",
    "passlib[bcrypt]>=1.7.4",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.3",
    "black>=23.10.1",
    "isort>=5.12.0",
    "mypy>=1.7.0",
    "flake8>=6.1.0",
    "pytest-cov>=4.1.0",
]

[tool.rye]
managed = true
dev-dependencies = [
    "pytest>=7.4.3",
    "black>=23.10.1",
    "isort>=5.12.0",
    "mypy>=1.7.0",
    "flake8>=6.1.0",
    "pytest-cov>=4.1.0",
]
```

## Project Structure 📁
```
backend/
├── src/
│   └── studenhexe/
│       ├── api/           # API routes
│       ├── core/          # Core functionality
│       ├── db/            # Database
│       ├── models/        # SQLAlchemy models
│       ├── schemas/       # Pydantic schemas
│       └── services/      # Business logic
├── tests/
├── alembic/              # Database migrations
├── pyproject.toml        # Rye/project configuration
└── README.md
```

## Implementation Steps

### 1. Project Setup 🛠️
- [ ] Initialize Rye project
- [ ] Configure pyproject.toml
- [ ] Setup development tools
  - black configuration
  - isort configuration
  - mypy configuration
  - flake8 configuration
- [ ] Docker setup
  - PostgreSQL container
  - Backend service container
  - Docker compose config

### 2. Core Framework 🏗️
- [ ] FastAPI app configuration
- [ ] Database connection setup
- [ ] Middleware setup
  - CORS
  - Authentication
  - Request logging
- [ ] Base models/schemas
- [ ] API error handling
- [ ] Config management

### 3. Database Models 💾
- [ ] Base SQLAlchemy setup
- [ ] Core models implementation
  - School
  - Room
  - Teacher
  - Class
  - Subject
  - TimeSlot
  - CurriculumRequirement
- [ ] Alembic migrations setup
- [ ] Model relationships
- [ ] Indexes and constraints

### 4. API Routes 🛣️
- [ ] School management
  - CRUD operations
  - Settings management
- [ ] Resource management
  - Rooms
  - Teachers
  - Classes
  - Subjects
- [ ] Curriculum management
  - Requirements
  - Grade configurations
- [ ] Schedule management
  - Generation requests
  - Manual adjustments
  - Validation

### 5. Business Logic 🧮
- [ ] Data validation services
- [ ] Schedule generation service
- [ ] Constraint validation service
- [ ] Export/Import service

### 6. Testing Strategy 🧪
- [ ] Unit tests setup
- [ ] Integration tests
- [ ] API tests
- [ ] Performance tests

## API Design

### Core Endpoints

#### School Setup
```
POST   /api/v1/schools
GET    /api/v1/schools/{id}
PUT    /api/v1/schools/{id}
DELETE /api/v1/schools/{id}
```

#### Resource Management
```
POST   /api/v1/schools/{id}/rooms
POST   /api/v1/schools/{id}/teachers
POST   /api/v1/schools/{id}/classes
POST   /api/v1/schools/{id}/subjects
```

#### Curriculum
```
POST   /api/v1/schools/{id}/curriculum
GET    /api/v1/schools/{id}/curriculum/{grade}
PUT    /api/v1/schools/{id}/curriculum/{grade}
```

#### Schedule
```
POST   /api/v1/schools/{id}/schedule/generate
GET    /api/v1/schools/{id}/schedule
PUT    /api/v1/schools/{id}/schedule
```

## Development Workflow
1. Setup development environment
   ```bash
   # Install dependencies
   rye sync
   
   # Activate environment
   rye shell
   
   # Run development server
   rye run dev
   ```
2. Implement database models
3. Create basic CRUD endpoints
4. Add business logic
5. Implement validation
6. Add tests
7. Document API

## Common Commands
```bash
# Add a dependency
rye add fastapi

# Add a dev dependency
rye add --dev pytest

# Run tests
rye run test

# Format code
rye run format

# Type checking
rye run typecheck

# Lint code
rye run lint
```

## Success Criteria ✅
- All tests passing
- 90%+ test coverage
- Type hints throughout
- OpenAPI documentation complete
- Performance benchmarks met 