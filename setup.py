#!/usr/bin/env python
import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

#Dependencies - python eggs
install_requires = [
        'setuptools',
        'Django',
]

setup(name='django-currency',
    version='5.0.1',
    description='Currencies for Django',
    author='Arpaso',
    author_email='arvid@arpaso.com',
    long_description=read('README.md'),
    url='http://github.com/Arpaso/django-currency.git',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data = True,    # include everything in source control
    zip_safe=False,
    install_requires=install_requires,
    classifiers=(
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
    ),
)
