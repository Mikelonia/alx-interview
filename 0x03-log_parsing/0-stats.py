#!/usr/bin/python3
'''A script that generates random HTTP request logs.
'''
import sys
import re

def process_line(line):
    # Define the regular expression pattern for matching the input format
    pattern = re.compile(r'^(\d+\.\d+\.\d+\.\d+) - \[.*\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$')

    match = pattern.match(line)
    if match:
        ip_address, status_code, file_size = match.groups()
        return int(status_code), int(file_size)
    else:
        return None, None

def print_metrics(total_size, status_counts):
    print(f"Total file size: {total_size}")
    for code in sorted(status_counts):
        print(f"{code}: {status_counts[code]}")

def main():
    total_size = 0
    status_counts = {}

    try:
        for line_number, line in enumerate(sys.stdin, start=1):
            status_code, file_size = process_line(line.strip())

            if status_code is not None and file_size is not None:
                total_size += file_size
                status_counts[status_code] = status_counts.get(status_code, 0) + 1

            if line_number % 10 == 0:
                print_metrics(total_size, status_counts)

    except KeyboardInterrupt:
        print_metrics(total_size, status_counts)

if __name__ == "__main__":
    main()

