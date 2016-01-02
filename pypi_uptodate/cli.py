import click
from requirements import Requirements


@click.command()
@click.option('--requirement', '-r', default='requirements.txt', help='Specify the path of the requirements file.')
def cli(requirement):
    """
    PyPI Up-to-date\n
    Check whether your PyPI requirements are up to date.
    """

    Requirements(requirement)

if __name__ == '__main__':
    cli()
