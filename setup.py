#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'onshapepy',
    'version': '0.0.4',
    'description': 'Drive part configurations from Python.',
    'long_description': open('README.md').read(),
    'author': 'Ty-Lucas Kelley, Ethan Keller',
    'url': 'https://github.com/onshapepy/onshapepy/tree/master/python',
    'license': open('LICENSE').read(),
    'packages': [
        'onshapepy'
    ],
    'install_requires': ['requests', 'pint'],
    'classifiers': [
        'Programming Language :: Python',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
}

setup(**config)
