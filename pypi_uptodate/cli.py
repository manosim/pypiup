import os
import click
from requirements import Requirements


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@click.command()
@click.option('--requirement', '-r', default='requirements.txt', type=click.STRING, help='Specify the path of the requirements file.')
@click.option('--demo', '-d', is_flag=True)
def cli(requirement, demo):
    """
    PyPI Up-to-date\n
    Check whether your PyPI requirements are up to date.
    """
    if demo:
        demo_path = os.path.join(BASE_DIR, 'requirements-demo.txt')
        return Requirements(demo_path)
    Requirements(requirement)

if __name__ == '__main__':
    cli()
