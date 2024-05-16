#!/usr/bin/python3
"""
Simulates random web server access logs for 10,000 requests.

This script generates and prints simulated web server access log entries
in a common format. It includes the following details for each request:

- IP address (randomized)
- Timestamp (current date and time)
- HTTP method (GET)
- Requested resource path (/projects/260)
- HTTP version (HTTP/1.1)
- Status code (randomly chosen from common codes)
- Content size (randomized)

The script iterates 10,000 times, generating a new log entry with random
values for each iteration. It uses sleep statements to introduce random
delays between simulated requests.
"""
import random
import sys
from time import sleep
import datetime


def main():
    """
    The main function for generating simulated web server access logs.

    This function iterates 10,000 times, generating and printing a single
    simulated access log entry in each iteration.
    """

    for _ in range(10000):
        # Simulate random delay between requests
        sleep(random.random())

        # Generate random IP address components
        ip1 = random.randint(1, 255)
        ip2 = random.randint(1, 255)
        ip3 = random.randint(1, 255)
        ip4 = random.randint(1, 255)

        # Get current date and time
        timestamp = datetime.datetime.now()

        # Choose a random HTTP status code
        status_code = random.choice([200, 301, 400, 401, 403, 404, 405, 500])

        # Generate random content size
        content_size = random.randint(1, 1024)

        # Format and print the log entry
        log_entry = "{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}".format(
            ip1, ip2, ip3, ip4, timestamp, status_code, content_size
        )
        print(log_entry, flush=True)


if __name__ == "__main__":
    main()

