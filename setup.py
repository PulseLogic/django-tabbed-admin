#! /usr/bin/env python
from distutils.core import setup
from setuptools import find_packages
import sys

# python2 and python3 support
try:
    reload
except NameError:
    # py3k has unicode by default
    pass
else:
    reload(sys).setdefaultencoding('utf-8')


setup(
    name='django-tabbed-admin',
    version='1.0.5',
    author='Guillaume Pousseo, PulseLogic BV',
    author_email='guillaumepousseo@revsquare.com, info@pulselogic.be',
    description='Easily add tabs to django admin forms.',
    long_description=open('README.rst').read(),
    url='http://www.revsquare.com, https://www.pulselogic.be',
    license='BSD License',
    platforms=['OS Independent'],
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
    ],
)
