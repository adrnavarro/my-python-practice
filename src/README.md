
# Source Directory

This directory contains all Python source code modules and tests for this project.

## Structure

- **modules/** – Reusable Python modules and packages
- **tests/** – Test files for modules and scripts

## Usage

### Modules
Place reusable Python modules and packages in the `modules/` directory. These are meant to be imported and used by other code.

### Scripts
Executable Python scripts are located in the top-level `scripts/` directory (at the project root, not under `src`). These are standalone programs that can be run directly.

#### How to Run Scripts

**Recommended:** Run scripts using the `-m` option from the project root or `src` directory:

```
python3 -m scripts.vector_app
```

**Why use `-m`?**
- The `-m` option runs the module as a script, ensuring that Python sets up the module search path correctly.
- This allows imports like `from modules.vetor_operations import ...` to work, since the `src` directory is treated as a package root.
- Running scripts directly (e.g., `python scripts/vector_app.py`) may cause `ModuleNotFoundError` for local imports, especially in projects with a package structure.

**Tip:** Always activate your virtual environment before running scripts to ensure dependencies are available.

### Tests
Place all test files in the `tests/` directory. Follow the naming convention `test_*.py` for test files.
