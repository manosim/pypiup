#!/usr/bin/env python
import sys
import subprocess


FLAKE8_ARGS = ['pypi_uptodate/', 'tests/', '--ignore=E501']
COVERAGE_ARGS = ['--source=pypi_uptodate', '--omit=pypi_uptodate/__init__.py', 'python -m unittest -v tests/tests.py']


def exit_on_failure(command, message=None):
    if command:
        sys.exit(command)


def flake8_main(args):
    print('Running: flake8', FLAKE8_ARGS)
    command = subprocess.call(['flake8'] + args)
    print("" if command else "Success. flake8 passed.")
    return command


def run_tests_coverage(args):
    command = subprocess.call('coverage run --source=pypi_uptodate --omit=pypi_uptodate/__init__.py -m unittest -v tests/tests.py', shell=True)
    command = subprocess.call(['coverage', 'report'])
    return command

# exit_on_failure(flake8_main(FLAKE8_ARGS))
exit_on_failure(run_tests_coverage(COVERAGE_ARGS))
