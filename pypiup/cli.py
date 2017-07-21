import os
import click
from pypiup.requirements import Requirements


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@click.command()
@click.option('--requirement', '-r', default='requirements.txt', type=click.STRING, help='Specify the path of the requirements file. Defaults to "requirements.txt".')
@click.option('--demo', '-d', is_flag=True, help='Load the demo requirements.txt file that comes with the package.')
def cli(requirement, demo):
    """
    PyPIup\n
    Check whether your PyPI requirements are up to date.
    """

    print("\n          ______   __  __     ______   __        __  __     ______  ")
    print("         /\  == \ /\ \_\ \   /\  == \ /\ \      /\ \/\ \   /\  == \ ")
    print("         \ \  _-/ \ \____ \  \ \  _-/ \ \ \     \ \ \_\ \  \ \  _-/ ")
    print("          \ \_\    \/\_____\  \ \_\    \ \_\     \ \_____\  \ \_\   ")
    print("           \/_/     \/_____/   \/_/     \/_/      \/_____/   \/_/   ")
    print("\n                                   PyPIup")
    print("                     https://github.com/manosim/pypiup")

    if demo:
        demo_path = os.path.join(BASE_DIR, 'requirements/requirements-demo.txt')
        return Requirements(demo_path)
    Requirements(requirement)

if __name__ == '__main__':
    cli()
