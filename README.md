# Glacier List

A Python package that provides a disk-backed list implementation for handling large datasets efficiently. When your data gets too large for memory, glacier-list automatically chunks it into pickle files on disk, only loading relevant chunks when needed.

## Features

- **Memory Efficient**: Only keeps a small portion of data in memory
- **Automatic Chunking**: Transparently splits large datasets into manageable chunks
- **List-like Interface**: Supports indexing, slicing, and iteration like regular Python lists
- **Parallel Processing**: Built-in map and serialization functions with multi-threading support
- **Type Safety**: Designed for dictionaries with comprehensive type hints
- **Context Manager**: Automatic cleanup of temporary files

## Requirements

- Python 3.9 or higher
- No external dependencies for core functionality

## Installation

Install from PyPI:

```bash
pip install glacier-list
```

**Note:** Python 3.9+ is required. If you're using an older Python version, please upgrade before installing.

## Python Version Compatibility

glacier-list supports Python 3.9 and later versions:

- ✅ Python 3.9+ (recommended)
- ✅ Python 3.10+
- ✅ Python 3.11+
- ✅ Python 3.12+

The package is tested across multiple Python versions and operating systems (Linux, Windows, macOS) to ensure compatibility.

### Testing Compatibility

To test compatibility on your system:

```bash
# Install with development dependencies
pip install glacier-list[dev]

# Run compatibility tests
python -m pytest tests/test_python_compatibility.py -v

# Or use the standalone compatibility script
python scripts/test_compatibility.py
```

### Multi-Version Testing

For developers, you can test across multiple Python versions using tox:

```bash
# Install tox
pip install tox

# Test on available Python versions
tox

# Test on specific Python version
tox -e py39

# Run linting and formatting checks
tox -e flake8,black,mypy
```

**Note**: The `tox` command will automatically skip Python versions that aren't installed on your system.

Install from source:

```bash
git clone https://github.com/christensendaniel/glacier-list.git
cd glacier-list
pip install -e .
```

## Quick Start

```python
from glacier_list import GlacierList

# Create a disk-backed list
cl = GlacierList(chunk_size=50000, disk_path="data")

# Add data - will automatically chunk to disk when needed
for i in range(100000):
    cl.append({"id": i, "value": f"item_{i}", "score": i * 1.5})

# Access data like a regular list
print(cl[0])  # First item
print(cl[-1])  # Last item
print(cl[1000:1010])  # Slice of 10 items

# Update items
cl[5] = {"id": 5, "value": "updated", "score": 99.9}


# Apply transformations to all data (uses threading)
def double_score(record):
    record["score"] *= 2
    return record


cl.map(double_score)

# Serialize complex data types to JSON strings
cl.serialize()

# Clean up when done
cl.cleanup_chunks()
```

## Use Cases

- **Large Dataset Processing**: Handle datasets that don't fit in memory
- **Data Pipelines**: Process streaming data with automatic disk overflow
- **ETL Operations**: Transform large datasets chunk by chunk
- **Data Analysis**: Analyze large datasets without memory constraints
- **Caching**: Implement persistent, memory-efficient caches

## Advanced Usage

### Context Manager (Recommended)

```python
from glacier_list import GlacierList

with GlacierList(chunk_size=10000) as cl:
    # Add lots of data
    for i in range(1000000):
        cl.append({"data": f"item_{i}"})

    # Process data
    result = cl[500000:500010]

    # Automatic cleanup on exit
```

### Custom Serialization

```python
# Serialize complex Python objects to JSON strings
cl.append(
    {
        "id": 1,
        "metadata": {"tags": ["python", "data"], "active": True},
        "scores": [1.2, 3.4, 5.6],
    }
)

cl.serialize()  # Converts lists, dicts, and bools to JSON strings
```

### Parallel Processing

```python
# Process data in parallel across chunks
def process_record(record):
    record["processed"] = True
    record["timestamp"] = "2024-01-01"
    return record


cl.map(process_record, max_workers=4)  # Use 4 threads
```

## Performance

GlacierList is designed for scenarios where:

- Your dataset is too large for memory
- You need random access to data
- You want to process data in chunks
- Memory usage is more important than raw speed

Typical performance characteristics:

- **Memory usage**: O(chunk_size) instead of O(total_items)
- **Access time**: O(1) for sequential access, O(log chunks) for random access
- **Disk usage**: Temporary pickle files (cleaned up automatically)

## Development

For development setup, see [CONTRIBUTING.md](CONTRIBUTING.md).

Run tests:

```bash
pytest
```

Run examples:

```bash
python -m glacier_list demo      # Small demonstration
python -m glacier_list example   # Full example with 1M items
```

## About the Author

glacier-list was created by **Christensen Daniel**, a passionate data engineer who specializes in building tools that make working with large datasets more efficient and enjoyable.

### Connect

- **LinkedIn**: [dbchristensen](https://www.linkedin.com/in/dbchristensen/) - For data engineering insights and project updates
- **GitHub**: [christensendaniel](https://github.com/christensendaniel) - Explore more projects and contributions
- **Email**: christensen.daniel+glacierlist@outlook.com

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
