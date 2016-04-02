#!/usr/bin/env python
import sys
import subprocess


FLAKE8_ARGS = ['pypiup/', 'tests/', '--ignore=E501']
NOSE2_ARGS = [
    '--with-coverage',
    '--coverage', 'pypiup',
    '--coverage-report', 'term-missing',
    '--coverage-report', 'html',
    '--verbose'
]


def exit_on_failure(command, message=None):
    if command:
        sys.exit(command)


def flake8_main(args):
    print('Running: flake8 %s' % FLAKE8_ARGS)
    command = subprocess.call(['flake8'] + args)
    print("" if command else "Success. flake8 passed.\n")
    return command


def run_tests(args):
    print('Running: nose2 -v %s' % " ".join(args))
    command = subprocess.call(['nose2'] + args)
    return command

exit_on_failure(flake8_main(FLAKE8_ARGS))
exit_on_failure(run_tests(NOSE2_ARGS))
