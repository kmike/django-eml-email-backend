#!/usr/bin/env python
from distutils.core import setup

for cmd in ('egg_info', 'develop'):
    import sys
    if cmd in sys.argv:
        from setuptools import setup

version='0.1'

setup(
    name='django-eml-email-backend',
    version=version,
    author='Mikhail Korobov',
    author_email='kmike84@gmail.com',

    packages=['eml_email_backend'],

    url='https://bitbucket.org/kmike/django-eml-email-backend/',
    license = 'MIT license',
    description = """ Django email backend that saves emails to .eml files. Such files can be opened directly in Outlook or Mail.app. """,

    long_description = open('README.rst').read(),
    requires = ['django (>= 1.3)'],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
