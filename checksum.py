#!/usr/bin/env python3


import click
import hashlib


def binary_parser(filename):
    with open(filename, mode='rb') as file:
        for line in file:
            yield line


def calc_checksum(file=None):
    hash_obj = hashlib.sha256()
    for line in binary_parser(file):
        hash_obj.update(line)
    return hash_obj.hexdigest()


def checksum(filename=None, expected=None):
    return calc_checksum(filename) == expected


@click.command()
@click.argument('file')
@click.argument('expected')
def cli(file, expected):
    try:
        if checksum(file, expected):
            click.echo(f'checksums match for file {file}')
        else:
            click.echo(f'checksums do not match for file {file}')
    except (FileNotFoundError, IsADirectoryError, PermissionError) as err:
        click.echo(f'ERROR: {err}')


if __name__ == '__main__':
    cli()
