# my-python-practice

Repository to hold Python modules and scripts for practicing and learning.

## Project Structure

```
my-python-practice/
├── .github/          # GitHub-specific configuration (workflows, templates)
├── src/              # Source code directory
│   ├── modules/      # Reusable Python modules and packages
│   ├── scripts/      # Standalone executable Python scripts
│   └── tests/        # Test files for modules and scripts
├── .gitignore        # Git ignore rules
├── LICENSE           # Project license
└── README.md         # This file
```

## Getting Started

### Python Environment & VS Code Setup

#### Using the Virtual Environment in VS Code

This project uses a local Python virtual environment located at `.venv` in the project root. To ensure consistent Python interpreter usage across all platforms (macOS, Linux, Windows), the following setting is included in `.vscode/settings.json`:

```json
{
	"python.defaultInterpreterPath": "${workspaceFolder}/.venv"
}
```

**How it works:**

- VS Code will automatically detect the correct Python interpreter inside `.venv` for your operating system:
	- On macOS/Linux: `.venv/bin/python`
	- On Windows: `.venv\Scripts\python.exe`
- You do **not** need to specify the full path; VS Code resolves it automatically.
- This makes the project portable and avoids interpreter issues when switching between platforms or collaborating.

**To use the virtual environment:**

1. If `.venv` does not exist, create it with:
	 - `python3 -m venv .venv` (macOS/Linux)
	 - `python -m venv .venv` (Windows)
2. Open the project in VS Code. The Python extension will automatically use the interpreter from `.venv`.
3. Install packages using the VS Code terminal or command palette. They will be installed in `.venv`.

**Note:** If you ever need to activate the environment manually in a terminal:
- On macOS/Linux: `source .venv/bin/activate`
- On Windows: `.venv\Scripts\activate`

### Modules
Place reusable Python modules in `src/modules/`. These are meant to be imported and used by other code.

### Scripts
Place executable Python scripts in `src/scripts/`. These are standalone programs that can be run directly.

### Tests
Place all test files in `src/tests/`. Follow the naming convention `test_*.py` for test files.

## Contributing

This is a personal practice repository, but feel free to explore the code and suggest improvements!
