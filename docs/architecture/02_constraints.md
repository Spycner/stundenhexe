# Timetable Constraints

## Hard Constraints
Must be satisfied for a valid schedule:

1. **Resource Conflicts**
   - A teacher cannot be in multiple places at once
   - A room cannot host multiple classes simultaneously
   - A class cannot have multiple subjects at the same time

2. **Time Constraints**
   - Classes must be scheduled within school hours
   - Required number of periods per subject must meet curriculum requirements for each grade
   - Break periods must be respected
   - Total weekly hours must not exceed grade's curriculum specification
   - Compulsory subjects must be scheduled for all students in grade

3. **Room Constraints**
   - Room capacity must not be exceeded
   - Specialized subjects must be in appropriate rooms (e.g., labs)

4. **Curriculum Constraints**
   - All compulsory subjects must be scheduled
   - Optional subjects must meet minimum group size requirements
   - Class sizes must not exceed maximum group size for specialized subjects
   - Grade-specific subject requirements must be met exactly

## Soft Constraints
Preferences that improve schedule quality:

1. **Teacher Preferences**
   - Preferred teaching hours
   - Minimized gaps between classes
   - Even distribution of classes across the week

2. **Pedagogical Considerations**
   - Difficult subjects in morning slots
   - Balanced daily workload for students
   - Subject variety throughout the day

3. **Administrative Preferences**
   - Efficient use of resources
   - Balanced teacher workload
   - Buffer time for room transitions

## Constraint Weights
- Hard constraints: Must be satisfied (weight: infinite)
- Soft constraints: Configurable weights (1-10)
  - Teacher preferences: 8
  - Pedagogical considerations: 7
  - Administrative preferences: 5 