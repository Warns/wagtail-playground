#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="mysite",
    install_requires=["Django>=3.1,<3.2", "wagtail>=2.11,<2.12",],
    packages=["home", "mysite", "search", "home.migrations", "mysite.settings",],
    py_modules=["manage",],
)
