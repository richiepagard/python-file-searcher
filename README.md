# Python File Searcher

A simple multithreaded command-line program that searches for files inside a directory and all of its subdirectories.

The purpose of this project is to practice Python concurrency by implementing a recursive file search using the `threading` module instead of relying on high-level concurrency libraries.

## How it works

Starting from a root directory, the program:

1. Scans the current directory.
2. Creates a new thread for each subdirectory.
3. Searches directories concurrently.
4. Waits until all worker threads finish.
5. Prints every matching file.

## Why this project?

This project was built to explore:

- Python threading
- Thread synchronization with `Condition`
- Recursive directory traversal
- Concurrent program design
- Logging and project organization

It is intended as a learning project rather than a production-ready file search tool.

