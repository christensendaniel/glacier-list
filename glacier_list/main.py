"""
Command-line interface and demonstration utilities for glacier-list.

This module provides entry points for running demonstrations and examples
of the professional disk-backed list implementation.
"""

from .glacier_list import GlacierList, example_usage


def demo():
    """Run a demonstration of the GlacierList functionality."""
    print("GlacierList Demo:")
    print("================")

    # Create a small demo list
    cl = GlacierList(chunk_size=5, disk_path="demo_data")

    # Add some data
    for i in range(10):
        cl.append({"id": i, "name": f"item_{i}", "value": i * 10})

    print(f"Created list with {len(cl)} items")
    print(f"First item: {cl[0]}")
    print(f"Last item: {cl[-1]}")
    print(f"Slice [3:7]: {cl[3:7]}")

    # Cleanup
    cl.cleanup_chunks()
    print("Demo completed and cleaned up!")


def main():
    """Main entry point for the package."""
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "demo":
        demo()
    elif len(sys.argv) > 1 and sys.argv[1] == "example":
        example_usage()
    else:
        print(
            "glacier-list: A disk-backed list implementation for handling large datasets efficiently"
        )
        print("\nAvailable commands:")
        print("  demo    - Run a small demonstration")
        print("  example - Run the full example with 1M items")


if __name__ == "__main__":
    main()
