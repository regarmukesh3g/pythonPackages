#!/usr/bin/env python
"""
Setup for distribution package.
"""
from setuptools import setup

setup(name='dist_pdf',
      version='SNAPSHOT',
      description='Distribution of data',
      packages=['distributions'],
      zip_sage=False)
