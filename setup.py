from setuptools import setup


# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))

def read(file_name):
    with open(path.join(this_directory, file_name), encoding='utf-8') as f:
        return f.read()


setup(
    name= 'onshapepy',
    version= '0.0.5',
    description= 'Drive part configurations from Python.',
    long_description= read("README.md"),
    author= 'Ethan Keller',
    url= 'https://github.com/onshapepy/onshapepy/tree/master/python',
    license= read("LICENSE"),
    packages= [
        'onshapepy'
    ],
    install_requires= ['requests', 'pint', 'ruamel.yaml'],
)

