#!/usr/bin/env python3

from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='docker-plugin-api',
    version='0.0-git',
    use_scm_version=True,
    description='Python interface to Docker Plugin API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Jacek Kowalski',
    author_email='Jacek@jacekk.info',
    url='https://github.com/jacekkow/docker-plugin-api',
    license='BSD',
    setup_requires=['setuptools_scm', 'wheel'],
    install_requires=['Flask'],
    packages=['docker_plugin_api'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
    ],
    python_requires='>=3.6',
)
