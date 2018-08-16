from setuptools import setup


long_description = '''Access OnShape part configurations from your python interpreter! Allows you to use Numpy, Scipy, and any other python packages you may need to accurately configure your part. An open source alternative to CADWolf or SwiftCalcs.'''

setup(
    name= 'onshapepy',
    version= '0.0.6',
    description= 'Drive part configurations from Python.',
    long_description= long_description,
    author= 'Ethan Keller',
    url= 'https://aguaclara.github.io/onshapepy/',
    license= "The MIT License (MIT)",
    packages= [
        'onshapepy'
    ],
    install_requires= ['requests', 'pint', 'ruamel.yaml'],
)

