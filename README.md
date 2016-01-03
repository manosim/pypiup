# pypi-uptodate [![travis][travis-image]][travis-url] [![pypi][pypi-image]][pypi-url]
Check whether your PyPI requirements are up to date.

### Development

    pyvenv env
    source env/bin/activate

    pip install -r requirements.txt
    python pypi_uptodate/cli.py --help
    python pypi_uptodate/cli.py --demo


### Installation
You can install `pypi-uptodate` through pypi.

    sudo pip install pypi-uptodate


### Usage
You can either use `pypiuptodate` or `pypi-uptodate`. Use `--help` to see all the available options.

    > pypiuptodate --help
    Usage: pypiuptodate [OPTIONS]

      PyPI Up-to-date
      Check whether your PyPI requirements are up to date.

    Options:
      -r, --requirement TEXT  Specify the path of the requirements file. Defaults
                              to "requirements.txt".
      -d, --demo              Load the demo requirements.txt file that comes with
                              the package.
      --help                  Show this message and exit.


### Tests
In order to run the tests you will have to run:

    python runtests.py


[travis-image]: https://travis-ci.com/ekonstantinidis/pypi-uptodate.svg?token=9QR4ewbqbkEmHps6q5sq&branch=master
[travis-url]: https://travis-ci.com/ekonstantinidis/pypi-uptodate

[pypi-image]: https://badge.fury.io/py/pypi-uptodate.svg
[pypi-url]: https://pypi.python.org/pypi/pypi-uptodate/
