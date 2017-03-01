# -*- coding: utf-8 -*-

from setuptools import setup

import versioneer

setup(
    name='pygoogleanalytics',
    packages=['pygoogleanalytics'],
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Wrapper for Google Analytics API python call',
    author='Aurélien Demilly',
    author_email='demilly.aurelien@gmail.com',
    url="https://github.com/ademilly/pygoogleanalytics",
    keywords=['data', 'analytics', 'google', 'python'],
    classifiers=[],
    install_requires=[
        'google-api-python-client',
        'pyopenssl',
    ]
)
