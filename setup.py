#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 11:40:38 2019

@author:
Maximilian N. Günther
MIT Kavli Institute for Astrophysics and Space Research, 
Massachusetts Institute of Technology,
77 Massachusetts Avenue,
Cambridge, MA 02109, 
USA
Email: maxgue@mit.edu
Web: www.mnguenther.com
"""

from setuptools import find_namespace_packages, setup

setup(
    name = 'allesfitter',      # The name of the PyPI-package.
    packages = find_namespace_packages(include=['allesfitter*']),
    version = '0.8.0',    # Update the version number for new releases
    #scripts=['allesfitter'],  # The name of the included script(s), and also the command used for calling it
    description = 'Inference framework for photometric and radial-velocity data',
    author = 'Maximilian N. Günther & Tansu Daylan',
    author_email = 'maxgue@mit.edu',
    url = 'https://github.com/MNGuenther/allesfitter',
    download_url = 'https://github.com/MNGuenther/allesfitter',
    classifiers = []
      #install_requires=['astropy>=1.1','fitsio>=0.9','numpy>=1.10'],
      #include_package_data = True
    )



