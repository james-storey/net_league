#!/usr/bin/env python

from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as fh:
    requirements = fh.read().splitlines()

test_requirements = []

setup(
    name="Net_League",
    version='1.0',
    url='https://sysreturn.net/net_league',
    author='James Storey',
    author_email='james@sysreturn.net',
    description=('A hosted Netrunner card and deck database '
                 'that helps a group of players track their deck\'s performance '
                 'and share cards between owners.'),
    license='ISC license',
    packages=['net_league',],
    package_dir={'net_league': 'net_league'},
    include_package_data=True,
    zip_safe=False,
    test_suite='tests',
    tests_require=test_requirements
)
