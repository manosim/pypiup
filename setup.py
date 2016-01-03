from setuptools import find_packages, setup

setup(
    name='pypi-uptodate',
    version=__import__('pypi_uptodate').__version__,
    author="Emmanouil Konstantinidis",
    author_email="manos@iamemmanouil.com",
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/ekonstantinidis/pypi-uptodate",
    license='BSD',
    description="Check whether your PyPI requirements are up to date.",
    long_description=open("README.md").read(),
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
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
)
