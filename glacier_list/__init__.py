"""
glacier-list: Professional disk-backed list implementation for Python.

This package provides GlacierList, a high-performance disk-backed list class designed for
handling large datasets that exceed available memory. Data is intelligently chunked and
stored as pickle files on disk, with automatic memory management that loads only relevant
chunks when accessed.

Key Features:
    - Memory-efficient storage for datasets larger than available RAM
    - Transparent disk-backed operations with list-like interface
    - Automatic chunking with configurable chunk sizes
    - Parallel processing capabilities for data transformations
    - Context manager support for automatic resource cleanup
    - Type-safe operations with comprehensive type hints

Example:
    >>> from glacier_list import GlacierList
    >>> with GlacierList(chunk_size=10000) as gl:
    ...     for i in range(1000000):
    ...         gl.append({"id": i, "data": f"record_{i}"})
    ...     print(f"Stored {len(gl)} records using minimal memory")
"""

__version__ = "0.1.0"
__author__ = "Christensen, Daniel"
__email__ = "christensen.daniel+glacierlist@outlook.com"

# Import main functionality
from .glacier_list import GlacierList, append_data, example_usage

__all__ = ["GlacierList", "append_data", "example_usage"]
