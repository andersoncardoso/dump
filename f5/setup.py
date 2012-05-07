#!/usr/bin/env python

import sys
import os
from distutils.core import setup

setup(name='f5',
	version='0.1',
	description='utility/boilerplate for working on tornado web',
	# long_description='',
	author='Anderson Pierre Cardoso',
	author_email='apierre.cardoso@gmail.com',
	# url='',
	packages=['f5'],
	install_requires=[
		'WTForms',
		'mongoengine',
		'pymongo',
		'tornado',
		'wsgiref',
	],
	license='MIT',
	platforms = 'any',
	classifiers=['Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Topic :: Software Development :: Libraries :: Application Frameworks',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
	]
)