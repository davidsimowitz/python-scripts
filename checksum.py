"""Calculate and compare a file's checksum with its expected result."""


import hashlib


def binary_parser(filename):
    """Parse binary file."""
    with open(filename, mode='rb') as file:
        for line in file:
            yield line


def checksum(filename=None, expected=None):
    """Return True if file's checksum matches expected value, else False."""
    hash_obj = hashlib.sha256()
    for line in binary_parser(filename):
        hash_obj.update(line)
    return hash_obj.hexdigest() == expected
