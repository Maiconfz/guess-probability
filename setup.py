#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(name='guessprobability',
      version='0.1.0',
      description='Guess Prabability tests',
      author='Maicon Fonseca Zanco',
      author_email='maiconfz@gmail.com',
      url='https://github.com/Maiconfz/guess-probability',
      packages=find_packages(exclude=('tests', 'docs'))
     )
