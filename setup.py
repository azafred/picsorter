# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

exec(open('loony/version.py').read())

setup(
    name='picsorter',
    version=__version__,
    description='Sorting pictures and Videos by date',
    long_description=readme,
    author='Fred Vassard',
    author_email='azafred@gmail.com',
    url='https://github.com/azafred/picsorter',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=['pyyaml', 'quik', 'pyobjc-framework-Cocoa'],
    tests_require=['nose', 'testfixtures', 'mock'],
    test_suite="nose.collector",
    entry_points={
        'console_scripts': [
          'picsorter = picsorter.main:main',
        ],
      },
      classifiers=[
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Operating System :: MacOS',
      ],
     )
)

