# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

packages = find_packages()

setup(name='pyBrematic',
      version='1.0',
      keywords='python telegram bot api wrapper',
      description='Python code for controlling Brematic remote power outlets and potentially other stuff',
      url='https://github.com/d-Rickyy-b/pyBrematic',
      author='d-Rickyy-b',
      author_email='pyBrematic@rickyy.de',
      license='MIT',
      packages=packages,
      zip_safe=False)
