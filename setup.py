from setuptools import setup

setup(
    name='pypi-uptodate',
    version=__import__('rest_framework_docs').__version__,
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
