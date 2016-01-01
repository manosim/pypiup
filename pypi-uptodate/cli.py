# coding: utf-8
import click


@click.command()
def cli():
    """
    PyPI Up-to-date\n
    Check whether your PyPI requirements are up to date.
    """
    click.echo("Hello World!")
    pass

if __name__ == '__main__':
    cli()
