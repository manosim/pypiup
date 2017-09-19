# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from multiprocessing.dummy import Pool as ThreadPool

import click
from pypiup.requirement import Requirement


class Requirements(object):

    def __init__(self, requirements_file):
        self.file = self.read_file(requirements_file)
        self.requirements = []

    def should_ignore_requirement(self, requirement):
        if requirement.startswith("#") or requirement == "":
            return True
        return False

    def read_file(self, requirements_filename):
        click.secho("\nAttempting to read %s ...\n" % requirements_filename, fg='magenta')

        try:
            requirements_file = open(requirements_filename)
            requirements_file_lines = requirements_file.read().splitlines()
            pool = ThreadPool()
            lines = [
                line for line in requirements_file_lines
                if not self.should_ignore_requirement(line)
            ]
            with click.progressbar(
                    length=len(lines),
                    label='Getting requirements details',
                    bar_template='%(label)s %(bar)s | %(info)s',
                    fill_char=click.style(u'█', fg='cyan'),
                    empty_char=' ') as bar:
                # Apply decorator
                req_with_upd = barupdate(bar)(Requirement)
                requirements = pool.map(req_with_upd, lines)
                # cleanup and wait for work to finish
                pool.close()
                pool.join()

                self.requirements = requirements
                self.show_details()
                self.show_stats()
                requirements_file.close()
        except IOError:
            return click.secho("Could not find %s. No such file or directory.\n" % (requirements_filename), fg='red')

    def show_details(self):
        click.echo()
        for requirement in self.requirements:
            requirement.output_details()

    def show_stats(self):
        stat_total = len(self.requirements)
        stat_uptodate = 0
        stat_needs_update = 0
        stat_invalid_semver = 0
        stat_invalid = 0

        for requirement in self.requirements:
            if requirement.valid:
                if requirement.status == "UPTODATE":
                    stat_uptodate += 1
                elif requirement.status == "NEEDS_UPDATE":
                    stat_needs_update += 1
                elif requirement.status == "INVALID_SEMVER":
                    stat_invalid_semver += 1
            else:
                stat_invalid += 1

        click.echo(click.style("\nStatistics", bold=True, underline=True, fg='yellow'))
        click.echo("  Total Requirements: %s" % stat_total)
        click.echo("  Up to date: %s" % stat_uptodate)
        click.echo("  Update available: %s" % stat_needs_update)
        click.echo("  Invalid Semver: %s" % stat_invalid_semver)
        click.echo("  Non PyPI Requirements: %s" % stat_invalid)


def barupdate(bar_obj, size=1):
    """Decorator for updating progressbar after
    object instantiation complete.
    """
    def decorator(cls):
        def inner(*args, **kwargs):
            instance = cls(*args, **kwargs)
            bar_obj.update(size)
            return instance
        return inner
    return decorator
