#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup for the ADS-B Cursor-on-Target Gateway.

Source:: https://github.com/ampledata/adsbcot
"""

import os
import sys

import setuptools

__title__ = 'adsbcot'
__version__ = '1.0.0b1'
__author__ = 'Greg Albrecht W2GMD <oss@undef.net>'
__copyright__ = 'Copyright 2020 Orion Labs, Inc.'
__license__ = 'Apache License, Version 2.0'


def publish():
    """Function for publishing package to pypi."""
    if sys.argv[-1] == 'publish':
        os.system('python setup.py sdist')
        os.system('twine upload dist/*')
        sys.exit()


publish()


setuptools.setup(
    name=__title__,
    version=__version__,
    description='ADS-B Cursor-on-Target Gateway.',
    author='Greg Albrecht',
    author_email='oss@undef.net',
    packages=[__title__],
    package_data={'': ['LICENSE']},
    package_dir={__title__: __title__},
    license=open('LICENSE').read(),
    long_description=open('README.rst').read(),
    url='https://github.com/ampledata/adsbcot',
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'pycot >= 2.3.1'
    ],
    classifiers=[
        'Topic :: Communications :: Ham Radio',
        'Programming Language :: Python',
        'License :: OSI Approved :: Apache Software License'
    ],
    keywords=[
        'ADS-B', 'ADSB', 'Cursor on Target', 'ATAK', 'TAK', 'CoT'
    ],
    entry_points={'console_scripts': ['adsbcot = adsbcot.commands:cli']}
)