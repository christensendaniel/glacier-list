# Contributing to Glacier List

Thank you for your interest in contributing to glacier-list! This document provides guidelines for contributing to the project.

## Development Setup

1. Clone the repository:

```bash
git clone https://github.com/christensendaniel/glacier-list.git
cd glacier-list
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the package in development mode:

```bash
pip install -e ".[dev]"
```

## Running Tests

Run the test suite:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=glacier_list
```

## Code Style

This project uses several tools for code quality:

- **Black** for code formatting
- **flake8** for linting
- **mypy** for type checking

Run all checks:

```bash
black glacier_list tests examples
flake8 glacier_list tests examples
mypy glacier_list
```

## Pull Request Process

1. Fork the repository
1. Create a feature branch: `git checkout -b feature-name`
1. Make your changes
1. Add tests for new functionality
1. Run the test suite and ensure all tests pass
1. Update documentation if needed
1. Submit a pull request

## Reporting Issues

Please use the GitHub issue tracker to report bugs or request features.
