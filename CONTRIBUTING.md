# Contribution Guidelines

Thank you for your interest in contributing to 语嫣AI员工管家 (Yuyan AI Employee Manager)! This document provides guidelines and instructions for contributing.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/yuyan-ai.git`
3. Create a virtual environment: `python -m venv venv`
4. Activate it: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
5. Install dependencies: `pip install -r requirements.txt -r requirements-dev.txt`

## Development Workflow

1. Create a new branch for your feature: `git checkout -b feature/your-feature-name`
2. Make your changes
3. Run tests: `pytest`
4. Run linting: `flake8 src`
5. Format code: `black src`
6. Commit your changes: `git commit -m "Add feature: description"`
7. Push to your fork: `git push origin feature/your-feature-name`
8. Create a Pull Request

## Code Style

- Follow PEP 8 guidelines
- Use type hints where appropriate
- Write docstrings for functions and classes
- Keep functions focused and small
- Use meaningful variable names

## Commit Messages

- Use present tense: "Add feature" not "Added feature"
- Use imperative mood: "Move cursor to..." not "Moves cursor to..."
- Limit first line to 72 characters
- Reference issues and PRs where appropriate

## Testing

- Write tests for new features
- Ensure all tests pass before submitting PR
- Aim for high test coverage

## Pull Request Process

1. Update documentation if needed
2. Add entry to CHANGELOG.md
3. Ensure CI checks pass
4. Request review from maintainers
5. Address review comments

## Reporting Issues

When reporting issues, please include:

- Operating system and version
- Python version
- Steps to reproduce
- Expected behavior
- Actual behavior
- Error messages or screenshots

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Respect different viewpoints

## Questions?

Feel free to open an issue for questions or join our discussions.

Thank you for contributing!
