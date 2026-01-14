# Copilot Instructions

These are basic rules for using GitHub Copilot in this repository:

1. Always create a TODO file before writing any code. The TODO file must outline detailed phases for the proposed changes, allowing work to be applied in small and controlled steps.
2. Update the progress of the changes in the TODO file as each phase is implemented and approved by the user.
3. When there are multiple options for names, algorithms, layouts, or any other situation, include a phase in the TODO file to question the user and decide on the preferred option before proceeding.
4. Use clear, descriptive commit messages for all changes.
5. Prefer readable, well-documented code over clever but obscure solutions.
6. Follow PEP8 style guidelines for Python code.
7. Add type hints to functions and methods where possible.
8. Write tests for new features and bug fixes in the `src/tests/` directory.
9. Do not commit secrets, credentials, or sensitive data.
10. Use comments to explain non-obvious logic or design decisions.
11. Keep dependencies up to date in `requirements.txt`.
12. Review Copilot suggestions for correctness and security before accepting.
13. Ask for help or clarification if Copilot's output is unclear or incorrect.

## Review Guidelines
When reviewing code generated or assisted by Copilot, consider the following:
- Enforcement of coding standards and best practices.
- Analyze performance implications of the code.
- Security considerations and potential vulnerabilities.
- Correctness and completeness of the implementation.

## Coding Standards

### Python Standards

#### Naming Conventions
Follow the official Python naming conventions:
- **Modules**: short, all-lowercase names. Underscores can be used if it improves readability (e.g., my_module).
- **Packages**: short, all-lowercase names, no underscores (e.g., mypackage).
- **Classes**: CapitalizedWords (CamelCase), e.g., MyClass.
- **Functions**: lowercase, with words separated by underscores (snake_case), e.g., my_function.
- **Variables**: lowercase, with words separated by underscores (snake_case), e.g., my_variable.
- **Constants**: all uppercase with words separated by underscores, e.g., MY_CONSTANT.
- **Method names**: lowercase, with words separated by underscores (snake_case), e.g., my_method.
- **Instance variables**: lowercase, with words separated by underscores (snake_case), e.g., self.my_variable.
- **Global variables**: lowercase, with words separated by underscores (snake_case), e.g., global_variable.
- **Private variables/methods**: prefix with a single underscore, e.g., _private_var.
- **Special methods**: use double underscores before and after the name, e.g., __init__, __str__.

#### Documentation
All Python code should include proper and standard docstrings:
- **Functions and Methods**: Use docstrings to describe the purpose, parameters, return values, exceptions raised, and any important notes. Follow PEP 257 and Google or NumPy style.
- **Classes**: Include a class-level docstring describing the class's purpose, attributes, and usage.
- **Modules**: Add a module-level docstring at the top of each file describing its contents and usage.
- **Scripts**: Provide a docstring at the top explaining the script's functionality and usage.
- **Other objects**: Add docstrings to any object that benefits from documentation for clarity and maintainability.
- Docstrings should be concise, clear, and follow the project's chosen style (Google, NumPy, or reStructuredText).
- Update docstrings as the code evolves to ensure they remain accurate and relevant.

#### Comments
- Avoid in-line comments when possible; prefer placing comments one line before the code they describe.
- Use multiline comments if a longer explanation is needed.
- Always include a descriptive comment before any statement that starts a block of code (such as function definitions, loops, conditionals, try, or class declarations).
- Ensure comments are clear, concise, and relevant to the code they describe.
- Make sure comments are preceeded by a blank line for better readability. Exacept when the comment is at the start of a code block.
- Update comments as the code evolves to ensure they remain accurate and relevant.