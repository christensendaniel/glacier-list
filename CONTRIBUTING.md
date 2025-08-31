# Contributing to Paged List

Thank you for your interest in contributing to paged-list! This document provides guidelines for contributing to the project.

## Development Setup

This project uses [Hatch](https://hatch.pypa.io/) for development environment management and packaging, and includes pre-commit hooks for automatic code formatting.

### Option 1: Using Hatch (Recommended)

1. Clone the repository:

```bash
git clone https://github.com/christensendaniel/paged-list.git
cd paged-list
```

1. Install Hatch:

```bash
pip install hatch
```

1. Install pre-commit hooks:

```bash
pip install pre-commit
pre-commit install
```

1. Run tests to verify setup:

```bash
hatch run test
```

That's it! Hatch will automatically manage the virtual environment and dependencies, and pre-commit will format your code automatically on each commit.

### Option 2: Traditional Setup

1. Clone the repository:

```bash
git clone https://github.com/christensendaniel/paged-list.git
cd paged-list
```

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

1. Install the package in development mode:

```bash
pip install -e ".[dev]"
```

## Running Tests

### Testing with Hatch (Recommended)

```bash
# Run tests
hatch run test

# Run tests with coverage
hatch run test-cov

# Run tests across all Python versions
hatch run test:run
```

### Testing with Traditional Tools

```bash
# Run the test suite
pytest

# Run tests with coverage
pytest --cov=paged_list
```

## Code Style

This project uses several tools for code quality:

- **Black** for code formatting
- **isort** for import sorting
- **flake8** for linting
- **mypy** for type checking

### Code Quality with Hatch (Recommended)

```bash
# Format code
hatch run format

# Check code quality
hatch run lint

# Run everything (format, lint, test with coverage)
hatch run all
```

### Code Quality with Traditional Tools

```bash
black paged_list tests examples
isort paged_list tests examples
flake8 paged_list tests examples
mypy paged_list
```

## Documentation

This project uses Sphinx for documentation, hosted on Read the Docs.

### Building Documentation Locally

```bash
# Install documentation dependencies
hatch run docs:build

# Or using traditional tools
pip install -e ".[docs]"
sphinx-build -b html docs docs/_build/html

# Serve documentation locally
hatch run docs:serve
# Or: python -m http.server 8000 --directory docs/_build/html
```

### Documentation Guidelines

- Use Google-style docstrings for all public functions and classes
- Update API documentation when adding new features
- Include examples in docstrings where helpful
- Update the changelog for significant changes

## Pre-commit Hooks

This project uses pre-commit hooks to automatically format code and check for issues:

- **Black**: Code formatting
- **isort**: Import sorting
- **Trim trailing whitespace**: Remove extra whitespace
- **Fix end of files**: Ensure files end with newlines
- **Check YAML**: Validate YAML files
- **Check for large files**: Prevent accidentally committing large files
- **Mixed line ending**: Normalize line endings
- **mdformat**: Format Markdown files

The hooks run automatically on `git commit`. To run manually:

```bash
pre-commit run --all-files
```

## Pull Request Process

1. Fork the repository
1. Create a feature branch: `git checkout -b feature-name`
1. Make your changes
1. Add tests for new functionality
1. Update documentation if adding new features or changing APIs
1. Run the test suite and ensure all tests pass: `hatch run all`
1. Ensure pre-commit hooks pass (they run automatically on commit)
1. Update the changelog for significant changes
1. Submit a pull request with a clear description of changes

### Checklist for Contributors

- [ ] Tests added/updated for new functionality
- [ ] Documentation updated (docstrings, API docs, examples)
- [ ] Code follows project style (handled by pre-commit hooks)
- [ ] All tests pass locally
- [ ] Changelog updated for significant changes

## Reporting Issues

Please use the GitHub issue tracker to report bugs or request features.
