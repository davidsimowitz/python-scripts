#!/usr/bin/env python3


import click
import hashlib


def binary_parser(*, filename=None):
    with open(filename, mode="rb") as file:
        for line in file:
            yield line


def checksum(*, filename=None, hash_algo="sha256"):
    hash_obj = eval(f"hashlib.{hash_algo}()")
    for line in binary_parser(filename=filename):
        hash_obj.update(line)
    return hash_obj.hexdigest()


@click.command()
@click.argument("filename")
@click.option(
    "-e", "--expected", "expected_checksum", type=str, help="expected checksum value"
)
@click.option(
    "-a",
    "--hash-algo",
    type=click.Choice(
        ["sha1", "sha224", "sha256", "sha384", "sha512", "blake2b", "blake2s"]
    ),
    default="sha256",
    help="calculation used for checksum",
)
def cli(*, filename, expected_checksum, hash_algo):
    try:
        calculated = checksum(filename=filename, hash_algo=hash_algo)
    except (FileNotFoundError, IsADirectoryError, PermissionError) as err:
        msg = f"ERROR: {err}"
    else:
        if expected_checksum and calculated == expected_checksum:
            msg = f"checksums match for file {filename}"
        elif not expected_checksum and calculated:
            msg = f"{calculated}"
        else:
            msg = f"checksums do not match for file {filename}"
    finally:
        click.echo(f"{msg}")


if __name__ == "__main__":
    cli()
