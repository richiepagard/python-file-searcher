"""
file_search.py

Threaded file search module.

This module is responsible for searching for a target file inside a directory
structure using threading and condition synchronization. It is intended to
support concurrent traversal of directories while notifying worker threads
when the desired file is found.

The current implementation is a placeholder for a threaded search utility.
"""
from os import listdir
from os.path import isdir, join
from threading import Lock
import logging

from logging_conf import base_logger
from threads_conf import FileSearchThread


# Set logger
logger = logging.getLogger(__name__)
base_logger(logger)

lock = Lock()
matches = []  # List to store matching file paths


def file_search(directory: str, target_file: str) -> list:
    """
    Search for a target file in the given directory and its subdirectories.

    Arguments:
        directory (str): Starts from this directory and traverses all subdirectories.
        target_file (str): The name of the file to search for.

    Returns:
        list: A list of paths to the matching files found.
    """
    logger.debug('Searching in directory: %s for file: %s', directory, target_file)

    for file in listdir(directory):
        file_path = join(directory, file)

        if target_file in file:
            with lock:
                matches.append(file_path)
                logger.info('Found match: %s', file_path)

        elif isdir(file_path):
            # Create a new thread for searching in the subdirectory
            search_thread = FileSearchThread(
                target=file_search,
                directory=file_path,
                target_file=target_file
            )
            search_thread.start()
            search_thread.join()  # Wait for the thread to finish
