#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
# Copyright (c) <2013-2014> <Colin Duquesnoy>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
"""
QDarkStyle is a darks stylesheet for python qt applications
"""
from setuptools import setup, find_packages
from qdarkstyle import __version__

setup(
    name='QDarkStyle',
    version=__version__,
    packages=find_packages(),
    url='https://github.com/ColinDuquesnoy/QDarkStyleSheet',
    license='MIT',
    author='Colin Duquesnoy',
    author_email='colin.duquesnoy@gmail.com',
    description='A dark stylesheet for PyQt/PySide applications',
    long_description="""
This package provides a dark style sheet for PySide/PyQt4/PyQt5 applications.

All you have to do is the following::

    import qdarkstyle
    app = QtGui.QApplication().instance()
    # PySide
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    # PyQt4
    app.setStyleSheet(qdarkstyle.load_stylesheet(pyside=False))
    # PyQt5
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

""",
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
          'Topic :: Software Development :: Libraries :: Application Frameworks'])
