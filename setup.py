#!/usr/bin/env python

import os
import re

from pathlib import Path

from codecs import open
from setuptools import find_packages, setup


here = Path(__file__).parent


# Load the package's __init__.py file as a dictionary.
pkg = {}
with open(here / 'netbox_vpxe_plugin' / '__init__.py', 'r', 'utf-8') as f:
    pkg = {k: v for k, v in re.findall(r"^(__\w+__) = \'(.+)\'", f.read(), re.M)}

# Load the README
readme = ''
if os.path.exists(here / 'README.md'):
    with open(here / 'README.md', 'r', 'utf-8') as f:
        readme = f.read()

setup(
    name=pkg['__title__'],
    version=pkg['__version__'],
    description=pkg['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    license=pkg['__license__'],
    url=pkg['__url__'],
    author=pkg['__author__'],
    author_email=pkg['__author_email__'],
    packages=find_packages(),
    package_data={'': ['LICENSE']},
    python_requires='>=3.6',
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
)
