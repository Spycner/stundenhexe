# ADR 001: Using Google OR-Tools for Constraint Solving

## Status
Accepted

## Context
We need a robust constraint solving system for generating school timetables that can handle:
- Complex hard and soft constraints
- Large problem spaces (many classes, teachers, rooms)
- Performance requirements (generate schedules in minutes)
- Integration with Python backend

## Decision
We will use Google OR-Tools as our constraint programming solver, specifically:
- CP-SAT solver for constraint programming
- Python API for integration
- Custom wrapper for our domain-specific constraints

## Consequences
### Positive
- Industry-proven solver with excellent performance
- Well-maintained by Google
- Free and open-source
- Rich documentation and community
- Python native integration
- Handles both optimization and satisfaction problems

### Negative
- Learning curve for team
- May need to simplify some constraints for performance
- Limited direct support for soft constraints (needs custom implementation)

## Alternatives Considered
1. **Z3 Theorem Prover**
   - More general purpose
   - Slower for our specific use case
   - More complex to implement

2. **Custom Genetic Algorithm**
   - More flexible for soft constraints
   - Would require significant development time
   - Performance uncertain

3. **Constraint Logic Programming (ECLiPSe, SWI-Prolog)**
   - Powerful constraint expression
   - Poor Python integration
   - Smaller community

## References
- [OR-Tools Documentation](https://developers.google.com/optimization)
- [CP-SAT Solver Guide](https://developers.google.com/optimization/cp/cp_solver)
- [Academic Paper on School Timetabling with CP-SAT]() 