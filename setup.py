
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import model_ident

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = model_ident.__version__

#readme = open('README.rst').read()
readme = "Write README"
setup(
    name='django-model-ident',
    version=version,
    description="""App for generating forms allowing users to build model queries""",
    long_description=readme,
    author='Chaim Kirby',
    author_email='chaim.kirby@gmail.com',
    url='https://github.com/ckirby/django-model-ident',
    packages=[
        'model_ident',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-model-ident',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)