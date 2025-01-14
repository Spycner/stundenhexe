# Data Models

## Core Entities

### School
```typescript
interface School {
  id: string;
  name: string;
  operatingHours: TimeRange;
  periodDuration: number; // minutes
  breakDuration: number; // minutes
}
```

### Room
```typescript
interface Room {
  id: string;
  name: string;
  capacity: number;
  type: RoomType; // CLASSROOM | LAB | GYM | etc.
  features: string[]; // projector, smartboard, etc.
}
```

### Teacher
```typescript
interface Teacher {
  id: string;
  name: string;
  subjects: Subject[];
  availability: TimeSlot[];
  maxHoursPerDay: number;
  preferences: TeacherPreferences;
}
```

### Class
```typescript
interface Class {
  id: string;
  name: string; // e.g., "10A"
  grade: number;
  size: number;
  subjects: SubjectRequirement[];
}
```

### Subject
```typescript
interface Subject {
  id: string;
  name: string;
  requiresSpecialRoom: boolean;
  roomType?: RoomType;
  difficulty: number; // 1-10
}
```

### TimeSlot
```typescript
interface TimeSlot {
  day: Day;
  period: number;
  duration: number;
}
```

### CurriculumRequirement
```typescript
interface CurriculumRequirement {
  id: string;
  grade: number;
  subject: Subject;
  hoursPerWeek: number;
  isCompulsory: boolean;
  minGroupSize?: number;  // for optional subjects/electives
  maxGroupSize?: number;
}
```

### GradeCurriculum
```typescript
interface GradeCurriculum {
  grade: number;
  academicYear: string;  // e.g., "2023/2024"
  requirements: CurriculumRequirement[];
  totalWeeklyHours: number;
  notes?: string;
}
```

## Relationships

### SubjectRequirement
```typescript
interface SubjectRequirement {
  subject: Subject;
  hoursPerWeek: number;
  preferredTeachers: Teacher[];
}
```

### Schedule
```typescript
interface Schedule {
  class: Class;
  teacher: Teacher;
  subject: Subject;
  room: Room;
  timeSlot: TimeSlot;
}
```

## Database Schema
The system will use PostgreSQL with the following schema structure:
- Tables mirror the core entities
- Foreign keys maintain referential integrity
- Indexes on frequently queried fields
- JSON columns for flexible preferences storage
- Curriculum requirements stored with grade-based partitioning for efficient queries 