#!/usr/bin/env python

from distutils.core import setup
from glob import glob
from os.path import splitext, basename


from setuptools import find_packages

setup(
    name="Most Frequent Words",
    version="1.0.0",
    description="Dekalabs Challenge for the Python Workshop",
    author="Dekalabs",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
)
