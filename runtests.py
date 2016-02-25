#!/usr/bin/env python
import sys
import subprocess


FLAKE8_ARGS = ['pypiup/', 'tests/', '--ignore=E501']
COVERAGE_ARGS = ['--source=pypiup', '--omit=pypiup/__init__.py', 'python -m unittest -v tests/tests.py']


def exit_on_failure(command, message=None):
    if command:
        sys.exit(command)


def flake8_main(args):
    print('Running: flake8', FLAKE8_ARGS)
    command = subprocess.call(['flake8'] + args)
    print("" if command else "Success. flake8 passed.")
    return command


def run_tests(args):
    command = subprocess.call('coverage run --source=pypiup --omit=pypiup/__init__.py -m unittest tests.tests_cli', shell=True)
    return command


def run_coverage():
    command = subprocess.call(['coverage', 'report'])
    return command


exit_on_failure(flake8_main(FLAKE8_ARGS))
exit_on_failure(run_tests(COVERAGE_ARGS))
exit_on_failure(run_coverage())
