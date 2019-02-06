# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='fastball',
    version='0.1',
    py_modules=['fastball'],
    install_requires=[
        'Click',
        'Requests'
    ],
    entry_points='''
        [console_scripts]
        fastball=fastball:fastball
    ''',
)