#!/usr/bin/python3
'''
http status code
'''
from sys import stdin


def print_summary(total_file_size, status_counts):
    """
    Reads logs from standard input and generates reports
    :param total_file_size: handles this .
    :param status_counts: Dictionary counts.
    """
    print("File size: {:d}".format(total_file_size))
    for code, count in sorted(status_counts.items()):
        if count != 0:
            print("{}: {}".format(code, count))


http_status_counts = {'200': 0, '301': 0, '400': 0, '401': 0,
                      '403': 0, '404': 0, '405': 0, '500': 0}

total_file_size = 0
line_count = 0


try:
    for line in stdin:
        line_args = line.split()

        if len(line_args) > 2:
            status_code = line_args[-2]
            file_size = int(line_args[-1])
            if status_code in http_status_counts:
                http_status_counts[status_code] += 1
            total_file_size += file_size
            line_count += 1
            if line_count == 10:
                print_summary(total_file_size, http_status_counts)
                line_count = 0

except KeyboardInterrupt:
    pass

finally:
    print_summary(total_file_size, http_status_counts)
