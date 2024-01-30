#!/usr/bin/env python3
import sys

print("Printing out User Data:\n")

for line in sys.stdin:
    # Strip whitespace and skip empty lines or lines starting with '#'
    line = line.strip()
    if not line or line.startswith('#'):
        continue

    # Split the line and check if it has exactly 4 parts
    parts = line.split(':')
    if len(parts) != 4:
        print(f"Skipping invalid line: {line}")
        continue

    username, password, userid, groupid = parts
    print(f"The user {username} has a password of {password} and has userid {userid} and groupid {groupid}")

print("\nEnd of User Data")

