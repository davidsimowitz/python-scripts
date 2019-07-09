"""Calculate and compare a file's checksum with its expected result."""


import hashlib
import sys


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


def cli(filename=None, expected_checksum=None):
    """command line interface"""
    if not (filename and expected_checksum):
        return(f'missing variables(s): '
               f'{"filename" if not filename else ""}'
               f'{", " if not (filename or expected_checksum) else ""}'
               f'{"expected_checksum" if not expected_checksum else ""}')
    try:
        if checksum(filename, expected_checksum):
            return f'checksums match for file {filename}'
        else:
            return f'checksums do not match for file {filename}'
    except (FileNotFoundError, IsADirectoryError, PermissionError) as err:
        return f'ERROR: {err}'


if __name__ == '__main__':
    if sys.argv and len(sys.argv) == 3:
        print(cli(sys.argv[1], sys.argv[2]))
    else:
        print('usage: checksum.py [file] [expected_checksum]')
