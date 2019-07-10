# python-scripts

Python scripts for useful tasks.


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
  usage: checksum.py [-h] file expected

  verify file's checksum with expected result

  positional arguments:
    file        file to be verified
    expected    expected checksum result

  optional arguments:
    -h, --help  show this help message and exit
  ```
