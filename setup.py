#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A dark style sheet for QtWidgets application.
"""

# Standard library imports
from setuptools import setup, find_packages

# Local imports
from qdarkstyle import __version__
from qdarkstyle import __doc__ as long_desc


install_requires = ['helpdev>=0.6.2']

extras_require = {
    'develop': ['qtsass', 'watchdog'],
    'docs': ['sphinx', 'm2r', 'sphinx_rtd_theme'],
    'example': ['pyqt5', 'pyside2', 'qtpy>=1.7']
}

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
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Application Frameworks'
    ],
    zip_safe=False,  # don't use eggs
    entry_points={"console_scripts": ["qdarkstyle=qdarkstyle.__main__:main"]},
    extras_require=extras_require,
    install_requires=install_requires,
    project_urls={
        "Issues": "https://github.com/ColinDuquesnoy/QDarkStyleSheet/issues",
        "Docs": "https://qdarkstylesheet.readthedocs.io/en/stable",
    }
)
