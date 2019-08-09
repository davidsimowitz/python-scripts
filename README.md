# python-scripts

Python scripts for useful tasks.
##### [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)


## Requirements:

+ [Python 3](https://www.python.org/downloads/) is installed. (If you are running a version of Python earlier than 3.6, please download the latest version. This application uses [f-strings](https://www.python.org/dev/peps/pep-0498/) and requires at least version 3.6 to function correctly. It will raise a SyntaxError if it is run using an earlier version.)
  * On a Mac or Linux machine this can be verified by running the following command in the shell:
  ```bash
  $ python3 -V
  ```


## Scripts:
* checksum.py


## Usage:


### checksum.py
* Calculate and compare a file's checksum with its expected result.
  ```bash
  Usage: checksum.py [OPTIONS] FILENAME

  Options:
    -e, --expected TEXT             expected checksum value
    -a, --hash-algo [sha1|sha224|sha256|sha384|sha512|blake2b|blake2s]
                                  calculation used for checksum
    --help                          Show this message and exit.

  ```
