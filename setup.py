#!/usr/bin/env python
# vim: fileencoding=utf-8
from setuptools import setup, Extension

setup(
    name='unicode_csv',
    ext_modules=[Extension('_unicode_csv', sources=['_unicode_csv.c'])],
    py_modules=['unicode_csv']
    )

