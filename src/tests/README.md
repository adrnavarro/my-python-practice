# Tests

This directory contains test files for the modules and scripts.

## Guidelines

- Follow the naming convention: `test_*.py`
- Use a testing framework like `pytest` or `unittest`
- Organize tests to mirror the structure of the code being tested
- Aim for good test coverage

## Example Structure

```
tests/
├── test_my_module.py
└── test_my_script.py
```

## Running Tests

```bash
# Using pytest
pytest src/tests/

# Using unittest
python -m unittest discover src/tests/
```
