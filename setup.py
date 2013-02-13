#!/usr/bin/env python

from distutils.core import setup, Extension

_pyjpeg = Extension(
	'_pyjpeg',
	sources = ['pyjpeg.c'],
	extra_link_args=['-ljpeg'],
)

setup(
	name='pyjpeg',
	version='0.1',
	description='pyjpeg',
	author='Theo Julienne',
	author_email='theo.julienne+pyjpeg@gmail.com',
	py_modules=['pyjpeg'],
	ext_modules=[_pyjpeg]
)