import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name="tatsu-parser", version="0.0.1", author="Ken Huang", packages=find_packages())
