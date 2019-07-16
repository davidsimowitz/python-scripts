#!/usr/bin/env python3


import click
import hashlib


def binary_parser(*, filename=None):
    with open(filename, mode='rb') as file:
        for line in file:
            yield line


def calc_checksum(*, filename=None):
    hash_obj = hashlib.sha256()
    for line in binary_parser(filename=filename):
        hash_obj.update(line)
    return hash_obj.hexdigest()


def checksum(*, filename=None, expected_checksum=None):
    return calc_checksum(filename=filename) == expected_checksum


@click.command()
@click.argument('filename')
@click.argument('expected-checksum')
def cli(*, filename, expected_checksum):
    try:
        if checksum(filename=filename, expected_checksum=expected_checksum):
            click.echo(f'checksums match for file {filename}')
        else:
            click.echo(f'checksums do not match for file {filename}')
    except (FileNotFoundError, IsADirectoryError, PermissionError) as err:
        click.echo(f'ERROR: {err}')


if __name__ == '__main__':
    cli()
