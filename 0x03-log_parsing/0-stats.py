#!/usr/bin/env python3
"""
Web Server Log Analyzer (stdin)

This script processes web server access log data provided through standard
input (stdin), line by line. It calculates and outputs the following
metrics:

* Total file size across all processed log entries (assuming file size is
  included in each line).
* Counts of occurrences for various HTTP status codes (200, 301, 400 series,
  and 500).

The script offers progress updates every 10 lines and gracefully handles
keyboard interrupts (CTRL+C) by displaying the current metrics before exiting.
"""

import sys
import signal
from typing import Dict, Union


def process_log_entry(line: str) -> bool:
    """
    Processes a single web server access log entry line.

    This function validates the entry format (assuming at least 7 parts)
    and extracts the status code and file size. It updates the global
    counters for total file size and status code occurrences.

    Args:
        line (str): The log entry line read from stdin.

    Returns:
        bool: True if the line was processed successfully, False otherwise.
    """

    try:
        parts = line.split()
        if len(parts) < 7:
            return False

        status_code = parts[-2]
        file_size = int(parts[-1])

        global total_file_size, status_code_counts
        total_file_size += file_size
        status_code_counts[status_code] += 1
        return True

    except (ValueError, IndexError):
        return False


def print_stats():
    """
    Prints the current statistics: total file size and status code counts.
    """

    print(f"Total file size: {total_file_size}")
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f"Status Code {code}: {count}")


def signal_handler(sig, frame):
    """
    Handles the keyboard interrupt signal (CTRL+C).

    This function gracefully exits the program upon receiving the signal
    by printing the current metrics and exiting with status code 0.
    """

    print_stats()
    sys.exit(0)


if __name__ == "__main__":
    """
    Main function that reads stdin, processes entries, and prints statistics.
    """

    global total_file_size, status_code_counts
    total_file_size = 0
    status_code_counts: Dict[str, int] = {"200": 0, "301": 0, "400": 0,
                                          "401": 0, "403": 0, "404": 0,
                                          "405": 0, "500": 0}

    signal.signal(signal.SIGINT, signal_handler)

    try:
        processed_lines = 0
        for line in sys.stdin:
            if process_log_entry(line):
                processed_lines += 1
                if processed_lines % 10 == 0:
                    print_stats()

    except KeyboardInterrupt:
        print_stats()
        sys.exit(0)

    print_stats()
