#!/usr/bin/python3
"""mod documentation"""
import sys
import signal

total_file_size = 0
status_code_counts = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
line_count = 0


def print_stats():
    """
    mod documentation mod documentation
    """
    print("File size: {}".format(total_file_size))
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print("{}: {}".format(code, status_code_counts[code]))


def signal_handler(sig, frame):
    """
    mod documentation mod documentation
    """
    print_stats()
    sys.exit(0)


def main():
    """
    mod documentation mod documentation
    """
    global total_file_size, line_count
    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) < 7:
                continue

            status_code = parts[-2]
            file_size = parts[-1]

            try:
                total_file_size += int(file_size)
            except ValueError:
                continue

            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_stats()
    except KeyboardInterrupt:
        print_stats()
        sys.exit(0)

    print_stats()


if __name__ == "__main__":
    main()
