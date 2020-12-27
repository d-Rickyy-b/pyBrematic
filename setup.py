# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

setup_path = os.path.dirname(os.path.abspath(__file__))
packages = find_packages(exclude=["tests*"])

with open(os.path.join(setup_path, "README.md"), "r", encoding="utf-8") as file:
    readme = file.read()

# Check if we are running on CI
CI = os.environ.get("CI")
if CI:
    version = ""
    TRAVIS_TAG = os.environ.get("TRAVIS_TAG")
    GITHUB_ACTIONS = os.environ.get("GITHUB_ACTIONS")

    if TRAVIS_TAG:
        print("Running on Travis!")
        version = TRAVIS_TAG.replace("v", "")
    elif GITHUB_ACTIONS:
        print("Running on GitHub Actions!")
        GITHUB_REF = os.environ.get("GITHUB_REF")
        tag = GITHUB_REF.split("/")[-1]
        version = tag.replace("v", "")
else:
    # Taken from https://packaging.python.org/guides/single-sourcing-package-version/
    version_dict = {}
    version_file = os.path.join(setup_path, "pyBrematic", "version.py")
    with open(version_file, "r", encoding="utf-8") as file:
        exec(file.read(), version_dict)
    version = version_dict["__version__"]

print("Building version '{0}' of pyBrematic".format(version))

setup(name="pyBrematic",
      version=version,
      keywords="python telegram bot api wrapper",
      description="Python code for controlling Brematic remote power outlets and potentially other stuff",
      long_description=readme,
      long_description_content_type="text/markdown",
      url="https://github.com/d-Rickyy-b/pyBrematic",
      author="d-Rickyy-b",
      author_email="pyBrematic@rico-j.de",
      license="MIT",
      packages=packages,
      include_package_data=True,
      zip_safe=False,
      classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: Internet",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            ],
      )
