# -*- coding: utf-8 -*-

import os
import sys
from setuptools import setup, find_packages

version = '0.1b1'

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name='z3c.formwidget.geoselect',
    version=version,
    description="A geoselect widget for z3c.form.",
    long_description='\n\n'.join([
        open(os.path.join('docs', 'README.txt')).read(),
        open(os.path.join('docs', 'INSTALL.txt')).read(),
        open(os.path.join('docs', 'LICENSE.txt')).read(),
        open(os.path.join('docs', 'HISTORY.txt')).read(),
    ]),
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Zope3",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Zope",
    ],
    keywords='zope zope3 z3c.form',
    author='Thomas Massmann',
    author_email='thomas.massmann@inqbus.de',
    maintainer='Thomas Massmann',
    maintainer_email='thomas.massmann@inqbus.de',
    url='',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    package_dir={'': 'src'},
    zip_safe=False,
    install_requires=[
      # -*- Extra requirements: -*-
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
    )
