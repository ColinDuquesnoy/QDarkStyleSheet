#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from qdarkstyle import __version__
from qdarkstyle import __doc__ as long_desc

setup(
    name='QDarkStyle',
    version=__version__,
    packages=find_packages(),
    url='https://github.com/ColinDuquesnoy/QDarkStyleSheet',
    license='MIT',
    author='Colin Duquesnoy',
    author_email='colin.duquesnoy@gmail.com',
    description='A dark stylesheet for Python and Qt applications',
    long_description=long_desc,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: X11 Applications :: Qt',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Application Frameworks'
    ],
    zip_safe=False,  # don't use eggs
    entry_points={"console_scripts": ["qdarkstyle=qdarkstyle.__main__:main"]}
)
