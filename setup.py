from setuptools import setup

setup(
    name='pypi-uptodate',
    version='0.0.1',
    packages=['pypi-uptodate'],
    include_package_data=True,
    install_requires=[
        'click',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        pypi-uptodate=pypi-uptodate.cli:cli
    ''',
)
