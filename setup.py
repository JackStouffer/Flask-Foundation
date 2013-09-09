#! ../env/bin/python

import os
import sys
import mypackage

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

README = open('README.rst').read()
LICENSE = open("LICENSE").read()

setup(
    name='bootstrapy',
    version=mypackage.__version__,
    description='A python bootstrap application, so that you can focus on writing code',
    long_description=(README),
    license=LICENSE,
    author='Kiran Gangadharan',
    author_email='kiran.daredevil@gmail.com',
    url='http://github.com/kirang89/bootstrapy',
    install_requires=[''],
    packages=[],
    include_package_data=True,
    scripts=[''],
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
    ),
    keywords='python, project, project template, bootstrap',
    tests_require=['nose'],
    test_suite='tests',
)