#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

from pyhamcrest_toolbox import __version__
version = __version__

requirements = [
    "pyhamcrest>=1.9"
]

with open('README.rst') as f:
    long_description = f.read()


setup(
    name='pyhamcrest_toolbox',
    version=version,
    description=(
        'A library that makes writing pyhamcrest matchers easier and more fun.'
    ),
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author='Timofey Danshin',
    author_email='t.danshin@gmail.com',
    url='https://github.com/ibolit/pyhamcrest_toolbox',
    packages=[
        'pyhamcrest_toolbox',
    ],
    python_requires='>=2.7',
    install_requires=requirements,
    license='BSD',
    zip_safe=False,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
    ],
    keywords=(
        "pyhamcrest", "hamcrest", "testing", "matchers", "test",
        "pytest", "unittest"),
)
