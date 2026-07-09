"""
This module contains the thread class for searching a file in a certain path.
It defines a subclass of Thread that is responsible for searching for a target file
in a specified directory and its subdirectories. The thread class takes a target function,
the root directory to start the search from, the target filename to look for, and a wait group for synchronization.
The run method of the thread class executes the target function with the provided parameters.
"""
from threading import Thread
from typing import Callable
from pathlib import Path


class FileSearchThread(Thread):
    """
    Subclass for searching a file in a certain path.
    Handles the search operation in a separate thread, allowing for concurrent file searches.
    """

    def __init__(
        self,
        target: Callable[[str, str], None],
        directory: str | Path,
        target_file: str,
    ) -> None:
        """
        Initialize the file search thread class for new instances,
        it will looking for 'target_file' in 'directory' path.

        Arguments:
            target (Callable[[str, str], None]): The function to be executed by the thread for searching the file.
            directory (str | Path): The path should start looking for the file from.
            target_file (str): The target filename should find.
        """
        super().__init__()

        self.target = target
        self.directory = directory
        self.target_file = target_file

    def run(self) -> None:
        """
        Runs the main searcher method to finding the target file
        in the reminding path.
        Calls the 'target' method to looking for the target file.
        """

        self.target(
            self.directory,
            self.target_file
        )
