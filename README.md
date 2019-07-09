# python-scripts

Python scripts for useful tasks.


## Requirements:

+ [Python 3](https://www.python.org/downloads/) is installed. (If you are running a version of Python earlier than 3.6, please download the latest version. This application uses [f-strings](https://www.python.org/dev/peps/pep-0498/) and requires at least version 3.6 to function correctly. It will raise a SyntaxError if it is run using an earlier version.)
  * On a Mac or Linux machine this can be verified by running the following command in the shell:
  ```bash
  $ python -V
  ```


## Scripts:
* checksum.py


## Usage:


### checksum.py
* Calculate and compare a file's checksum with its expected result.
  ```bash
  $ python3 checksum.py [file] [expected_checksum]
  ```
  or:
  ```bash
  $ ./checksum.py [file] [expected_checksum]
  ```
