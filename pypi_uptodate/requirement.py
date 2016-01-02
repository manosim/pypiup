import click
import re
import requests


class Requirement:

    def __init__(self, requirement):
        self.setUp(requirement)
        self.name = None
        self.current_version = None
        self.latest_version = None

    def setUp(self, requirement):
        regex = re.split("==", requirement)
        self.name = regex[0]
        self.current_version = regex[1]
        self.get_package_info()

    def get_package_info(self):
        request = requests.get(('https://pypi.python.org/pypi/%s/json' % (self.name)))
        response_json = request.json()

        self.latest_version = response_json["info"]["version"]
        click.echo("Package: %s \n Current: %s Latest: %s\n" % (self.name, self.current_version, self.latest_version))
