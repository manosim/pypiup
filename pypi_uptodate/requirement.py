# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import click
import re
import requests
import semantic_version


class Requirement(object):
    """
    Steps:
    1. Try to get name and version
    2. Get details from PyPI
    3. Compare Versions
    """

    def __init__(self, requirement):
        self.name = None
        self.current_version = None
        self.latest_version = None
        self.valid = False
        self.setUp(requirement)

    def setUp(self, requirement):
        regex = re.split("==", requirement)
        try:
            self.name = regex[0]
            self.current_version = regex[1]
            self.get_package_info()
        except IndexError:
            # If it cannot find the name and version assume
            # it is not a pypi packages (ie. GitHub Repository)
            pass

    def get_package_info(self):
        pypi_url = "https://pypi.python.org/pypi/%s/json" % (self.name)
        request = requests.get(pypi_url)
        if request.status_code == requests.codes.ok:
            response_json = request.json()
            self.latest_version = response_json["info"]["version"]
            self.valid = True

    def valid_semver(self):
        valid_current = semantic_version.validate(self.current_version)
        valid_latest = semantic_version.validate(self.latest_version)
        return valid_current and valid_latest

    def output_details(self):
        if self.valid and self.valid_semver():
            comparison = semantic_version.compare(self.current_version, self.latest_version)
            if (comparison >= 0):
                click.echo("\n%s\n  %s" % (click.style("✓ %s" % self.name, fg='green'), click.style("Up to date, %s." % self.current_version)))
            else:
                click.echo("\n%s\n  %s" % (click.style("✗ %s" % self.name, fg='red'), click.style("Needs update, From %s to %s." % (self.current_version, self.latest_version))))
        elif self.valid and not self.valid_semver():
            click.secho("✗ %s: Could not compare. Invalid semver, From %s to %s." % (self.name, self.current_version, self.latest_version), fg='cyan')
        else:
            # Invalid Requirement (ie. GitHub Repository)
            pass
