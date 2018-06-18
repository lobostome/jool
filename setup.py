#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='jool',
      version='0.1',
      description='Feature generation for bug prediction',
      author='Peter Damianov',
      author_email='pddamianov@gmail.com',
      url='https://github.com/lobostome/jool',
      license='MIT',
      packages=find_packages(exclude=['docs', 'tests*']),
      install_requires=['pygit2==0.27.0', 'pandas==0.22.0', 'nltk==3.2.5'],
      python_requires='>=3.6',
      entry_points={
          'console_scripts': [
              'jool=jool:main',
          ],
      }
      )
