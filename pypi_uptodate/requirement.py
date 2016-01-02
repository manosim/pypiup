import click
import re
import requests


class Requirement(object):

    def __init__(self, requirement):
        self.name = None
        self.current_version = None
        self.latest_version = None
        self.is_invalid = False
        self.setUp(requirement)

    def setUp(self, requirement):
        regex = re.split("==", requirement)
        try:
            self.name = regex[0]
            self.current_version = regex[1]
            self.get_package_info()
        except IndexError:
            self.is_invalid = True

    def get_package_info(self):
        pypi_url = "https://pypi.python.org/pypi/%s/json" % (self.name)
        request = requests.get(pypi_url)
        if request.status_code == requests.codes.ok:
            response_json = request.json()
            self.latest_version = response_json["info"]["version"]
        else:
            self.is_invalid = True

    def output_details(self):
        if not self.is_invalid:
            click.echo("\nPackage: %s \n Current: %s Latest: %s" % (self.name, self.current_version, self.latest_version))
        else:
            click.secho("\nSkipping non PyPI requirement...\n", fg='blue')
