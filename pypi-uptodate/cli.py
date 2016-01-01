# coding: utf-8
import click


@click.command()
@click.option('--requirement', '-r', default='requirements.txt', help='Specify the path of the requirements file.')
def cli(requirement):
    """
    PyPI Up-to-date\n
    Check whether your PyPI requirements are up to date.
    """

    # click.echo("Hello World!")
    click.echo("Opening: %s" % requirement)

    try:
        requirements = open(requirement).read().splitlines()
        for line in requirements:
            click.echo(line)

    except OSError:
        click.secho("Could not find %s. No such file or directory." % (requirement), fg='red')

if __name__ == '__main__':
    cli()
