# toy-bug-repo

`toy-bug-repo` is a synthetic benchmark repository designed for testing automated bug-fixing agents.

## Overview

The repository contains 4 small, isolated Python modules under 30 lines each. Every module contains exactly one deliberate bug that can be fixed strictly within that file. Corresponding pytest test suites are included, which currently fail against the buggy code but will pass once fixed.

## Modules & Bug Categories

- `calc.py`: Calculation helper for discounts (Bug category: Wrong comparison operator)
- `validator.py`: Username input validator (Bug category: Missing None/empty-input guard)
- `parser.py`: Text parser for multiline input (Bug category: Off-by-one loop index error)
- `inventory.py`: Inventory stock monitor (Bug category: Inverted boolean logic)

## Running Tests

Run the test suite using pytest:

```bash
pytest
```

Each module has a corresponding issue report in `issues/<module_name>.md`.
