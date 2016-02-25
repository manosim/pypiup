# pypiup [![travis][travis-image]][travis-url] [![pypi][pypi-image]][pypi-url]
Check whether your PyPI requirements are up to date.

[![press][press-image]][press-url]

### Installation
You can install `pypiup` through pypi.

    sudo pip install pypiup


### Usage
The command you can use is `pypiup`. Use `--help` to see all the available options.

    > pypiup --help
    Usage: pypiup [OPTIONS]

      PyPIup
      Check whether your PyPI requirements are up to date.

    Options:
      -r, --requirement TEXT  Specify the path of the requirements file. Defaults
                              to "requirements.txt".
      -d, --demo              Load the demo requirements.txt file that comes with
                              the package.
      --help                  Show this message and exit.


### Development

    pyvenv env
    source env/bin/activate

    pip install -r requirements.txt
    python pypiup/cli.py --help
    python pypiup/cli.py --demo


### Tests
In order to run the tests you will have to run:

    python runtests.py


### Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request
6. Make sure tests are passing


[travis-image]: https://travis-ci.com/ekonstantinidis/pypiup.svg?token=9QR4ewbqbkEmHps6q5sq&branch=master
[travis-url]: https://travis-ci.com/ekonstantinidis/pypiup

[pypi-image]: https://badge.fury.io/py/pypiup.svg
[pypi-url]: https://pypi.python.org/pypi/pypiup/


[press-image]: https://cloud.githubusercontent.com/assets/6333409/12076913/1f9454dc-b1b9-11e5-87c3-09a8570f21fc.png
[press-url]: https://github.com/ekonstantinidis/pypiup
