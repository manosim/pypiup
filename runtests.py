#!/usr/bin/env python
import sys
import subprocess
from coverage import coverage


FLAKE8_ARGS = ['pypi_uptodate/', '--ignore=E501']


def exit_on_failure(command, message=None):
    if command:
        sys.exit(command)


def flake8_main(args):
    print('Running: flake8', FLAKE8_ARGS)
    command = subprocess.call(['flake8'] + args)
    print("" if command else "Success. flake8 passed.")
    return command


def run_tests_coverage():
    # Setup Coverage
    cov = coverage(source=["pypi_uptodate"], omit=["pypi_uptodate/__init__.py"])
    cov.start()

    failures = subprocess.call(['python', 'tests/tests.py'])

    if bool(failures):
        cov.erase()
        sys.exit("Tests Failed. Coverage Cancelled.")

    # If success show coverage results
    cov.stop()
    cov.save()
    cov.report()
    cov.html_report(directory='htmlcov')

exit_on_failure(flake8_main(FLAKE8_ARGS))
exit_on_failure(run_tests_coverage())
