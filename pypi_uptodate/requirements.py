import click
from requirement import Requirement


class Requirements:

    def __init__(self, requirements_file):
        self.file = self.read_file(requirements_file)

    def read_file(self, requirements_file):
        click.secho("\nAttempting to read %s ...\n" % requirements_file, fg='magenta')

        try:
            requirements = open(requirements_file).read().splitlines()
            for line in requirements:
                Requirement(line)

        except OSError:
            return click.secho("Could not find %s. No such file or directory." % (requirements_file), fg='red')
