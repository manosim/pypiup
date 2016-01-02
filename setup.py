from setuptools import setup

setup(
    name='pypi-uptodate',
    version=__import__('pypi_uptodate').__version__,
    packages=['pypi_uptodate'],
    include_package_data=True,
    install_requires=[
        'click',
        'requests',
        'semantic_version'
    ],
    entry_points='''
        [console_scripts]
        pypiuptodate=pypi_uptodate.cli:cli
        pypi_uptodate=pypi_uptodate.cli:cli
    ''',
)
