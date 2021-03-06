# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     setup
   Description :
   Author :        Asdil
   date：          2018/11/16
-------------------------------------------------
   Change Activity:
                   2019/08/16:
-------------------------------------------------
"""
__author__ = 'Asdil'

from setuptools import setup

setup(name='mofang23',
      version='0.0.1.4',
      description='Tool of Asdil',
      author='Asdil',
      author_email='jpl4job@126.com',
      maintainer='Asdil',
      maintainer_email='jpl4job@126.com',
      license="MIT",
      packages=['mofang23'],
      platforms=["all"],
      url='https://github.com/Asdil/mofang23',
      install_requires=["pandas",
                        "Asdil",
                        "numpy",
                        "matplotlib"],
      classifiers=[
          "Environment :: Web Environment",
          "Intended Audience :: Developers",
          "Operating System :: OS Independent",
          "Topic :: Text Processing :: Indexing",
          "Topic :: Utilities",
          "Topic :: Internet",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7", ])

#  python setup.py check
#  python setup.py sdist
#  python setup.py register -r pypi
#  python setup.py sdist upload -r pypi
