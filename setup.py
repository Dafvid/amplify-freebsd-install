# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, '%s/amplify' % os.getcwd())

from setuptools import setup, find_packages

__author__ = "David W"
__copyright__ = "Nope"
__license__ = ""
__maintainer__ = "David W"
__email__ = "david at dafnet.se"

setup(
    name="nginx-amplify-agent",
    version="1.7.0",
    author="Mike Belov",
    author_email="dedm@nginx.com",
    description="NGINX Amplify Agent",
    keywords="amplify agent nginx",
    url="https:/amplify.nginx.com/",
    packages=find_packages(exclude=[
        "*.test", "*.test.*", "test.*", "test",
        "tools", "tools.*", "packages", "packages.*"]),
    scripts=[
        'nginx-amplify-agent.py'
    ],
    entry_points={},
    long_description='NGINX Amplify Agent',
)
