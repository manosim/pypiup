# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import click
from requirement import Requirement


class Requirements(object):

    def __init__(self, requirements_file):
        self.file = self.read_file(requirements_file)
        self.requirements = []

    def read_file(self, requirements_file):
        click.secho("\nAttempting to read %s ...\n" % requirements_file, fg='magenta')

        try:
            requirements_file = open(requirements_file).read().splitlines()
            with click.progressbar(
                    iterable=requirements_file,
                    label='Getting requirements details',
                    bar_template='%(label)s %(bar)s | %(info)s',
                    fill_char=click.style(u'█', fg='cyan'),
                    empty_char=' ') as bar:
                requirements = []
                for line in bar:
                    requirement = Requirement(line)
                    requirements.append(requirement)
                self.requirements = requirements
                self.show_details()
        except OSError:
            return click.secho("Could not find %s. No such file or directory." % (requirements_file), fg='red')

    def show_details(self):
        click.echo("\n")
        for requirement in self.requirements:
            requirement.output_details()
