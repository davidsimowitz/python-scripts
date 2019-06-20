"""Calculate and compare a file's checksum with its expected result."""


import hashlib


def checksum(filename=None, expected=None):
    """Return True if file's checksum matches expected value, else False."""
    hash_obj = hashlib.sha256()
    with open(filename, mode='rb') as file:
        hash_obj.update(file.read())
    return hash_obj.hexdigest() == expected
