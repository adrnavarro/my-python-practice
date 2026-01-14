# scripts Directory

This folder contains standalone Python scripts for interactive use and demonstrations.

## Purpose
Scripts in this directory are designed to be run as command-line applications. For example, `vector_app.py` provides an interactive menu for performing vector operations using the functions defined in the `src/modules` package.

## How to Run Scripts

**Recommended:** Run scripts using the `-m` option from the project root or `src` directory:

```
python3 -m scripts.vector_app
```

### Why use `-m`?
- The `-m` option runs the module as a script, ensuring that Python sets up the module search path correctly.
- This allows imports like `from modules.vector_operations import ...` to work, since the `src` directory is treated as a package root.
- Running scripts directly (e.g., `python scripts/vector_app.py`) may cause `ModuleNotFoundError` for local imports, especially in projects with a package structure.

**Tip:** Always activate your virtual environment before running scripts to ensure dependencies are available.
