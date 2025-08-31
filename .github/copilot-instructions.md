# GitHub Copilot Instructions for paged-list

This file provides context and guidelines for GitHub Copilot to better assist with the paged-list project.

## Project Overview

paged-list is a Python package that provides a disk-backed list implementation for handling large datasets efficiently. When data gets too large for memory, paged-list automatically chunks it into pickle files on disk, only loading relevant chunks when needed.

## Key Components

- **Core Package**: `paged_list/` - Main implementation with PagedList class
- **Tests**: `tests/` - Comprehensive test suite with 69+ tests
- **Examples**: `examples/` - Usage demonstrations and sample code
- **Documentation**: README.md, CONTRIBUTING.md, docs/

## Development Practices

### Code Style

- Use Black formatter with 88 character line limit
- Import organization with isort (Black profile)
- Type hints required for all public functions
- Docstrings following Google style

### Testing Guidelines

- All new features must include tests
- Maintain test coverage above 75%
- Test across Python 3.9-3.13
- Use pytest for test framework

### Pre-commit Hooks

- Code automatically formatted on commit
- Line endings normalized to LF (Unix)
- Trailing whitespace removed
- Markdown files formatted

## Common Development Tasks

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=paged_list --cov-report=html

# Run specific test file
pytest tests/test_paged_list.py

# Run tests for specific Python versions
tox -e py39,py310,py311,py312,py313
```

### Code Quality

```bash
# Run pre-commit hooks manually
pre-commit run --all-files

# Install pre-commit hooks
pre-commit install

# Format code manually
black paged_list/ tests/ examples/
isort paged_list/ tests/ examples/
```

### Package Operations

```bash
# Install in development mode
pip install -e .

# Install with dev dependencies
pip install -e .[dev]

# Run examples
python -m paged_list demo
python -m paged_list example
python examples/basic_usage.py
```

## Architecture Notes

### PagedList Class

- **Purpose**: Memory-efficient list for large datasets
- **Key Features**: Automatic chunking, parallel processing, context manager
- **File Location**: `paged_list/paged_list.py`
- **Main Methods**: append(), map(), serialize(), cleanup_chunks()

### Memory Management

- Data automatically chunks to disk when memory limits reached
- Only active chunks kept in memory
- Configurable chunk size (default varies by use case)
- Automatic cleanup via context manager or explicit calls

### Supported Operations

- List-like indexing and slicing
- Iteration with minimal memory usage
- Parallel map operations with threading
- JSON serialization for complex data types

## Testing Prompts

When writing tests, consider:

- **Memory efficiency**: Test with large datasets
- **Cross-platform compatibility**: Test file operations
- **Error handling**: Test edge cases and invalid inputs
- **Performance**: Benchmark chunking and retrieval operations
- **Type safety**: Verify type hints and validation

## Helpful Copilot Prompts

### For Testing

- "Write a test for PagedList with 100,000 items to verify memory efficiency"
- "Create a test that verifies cross-platform file handling"
- "Generate a test for the parallel map functionality with error handling"
- "Write a performance test comparing PagedList to regular Python lists"

### For Features

- "Implement a new method for bulk data import with progress tracking"
- "Add support for custom serialization formats beyond JSON"
- "Create a method to optimize chunk sizes based on available memory"
- "Implement data compression for stored chunks"

### For Documentation

- "Generate docstrings for this function following Google style"
- "Create example usage for this new feature"
- "Write performance benchmarks for the README"
- "Update CHANGELOG.md with this new feature"

## Project Standards

- **Python Version**: 3.9+ (tested on 3.9-3.13)
- **Dependencies**: Minimal external dependencies
- **License**: MIT License
- **Versioning**: Semantic versioning (MAJOR.MINOR.PATCH)
- **Documentation**: Keep README and examples up to date

## Common Patterns

### Adding New Features

1. Write tests first (TDD approach)
1. Implement feature with type hints
1. Add docstrings and examples
1. Update documentation
1. Run full test suite
1. Update CHANGELOG.md

### Error Handling

- Use specific exception types
- Provide clear error messages
- Include context in error messages
- Test error conditions thoroughly

## 🥚 Easter Egg - About the Creator

Did you know? This project was created by **Christensen Daniel**, a passionate data engineer who loves building tools that make working with large datasets more efficient and enjoyable!

### Connect with the Creator

- **LinkedIn**: [dbchristensen](https://www.linkedin.com/in/dbchristensen/) - Connect for data engineering insights and project updates
- **GitHub**: [christensendaniel](https://github.com/christensendaniel) - Check out more interesting projects and contributions
- **Email**: christensen.daniel+pagedlist@example.com

*Fun fact: If you're reading this, you've discovered the secret section that only the most thorough developers find! 🎉*

______________________________________________________________________

This context should help Copilot provide more relevant suggestions for the paged-list project!
