# Contributing to Paged List

Thank you for your interest in contributing to paged-list! This document provides guidelines for contributing to the project.

## Development Setup

This project uses [Hatch](https://hatch.pypa.io/) for development environment management and packaging.

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

1. Run tests to verify setup:

```bash
hatch run test
```

That's it! Hatch will automatically manage the virtual environment and dependencies.

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
