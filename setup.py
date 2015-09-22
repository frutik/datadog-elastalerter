# -*- coding: utf-8 -*-
import os

from setuptools import find_packages
from setuptools import setup


base_dir = os.path.dirname(__file__)
setup(
    name='datadog_elastalerter',
    version='0.0.1',
    description='Datadog alerter for ElastAlerter',
    author='Andrew Kornilov',
    author_email='frutik@gmail.com',
    setup_requires='setuptools',
    license='FreeBSD License',
    packages=['datadog_elastalerter'],
    install_requires=[
        'datadog',
    ]
)
