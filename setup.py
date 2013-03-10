#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# QDarkStyle - A dark style sheet for Qt applications
#
# Copyright 2012, 2013 Colin Duquesnoy <colin.duquesnoy@gmail.com>
#
# This software is released under the LGPLv3 license.
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
"""
QDarkStyle is a darks stylesheet for python qt applications
"""
from setuptools import setup, find_packages

setup(
    name='QDarkStyle',
    version='1.0.1',
    packages=find_packages(),
    package_data={'qdarkstyle': ["*.qss", "*.qrc", "rc/*.png"]},
    url='https://github.com/ColinDuquesnoy/QDarkStyleSheet',
    license='LGPLv3',
    author='Colin Duquesnoy',
    author_email='colin.duquesnoy@gmail.com',
    description='A dark stylesheet for pyside/pyqt applications',
    long_description="""
    This package provides a dark style sheet for PySide/PyQt applications.
    All you have to do is the following::

        import qdarkstyle
        QtGui.QApplication().instance().setStyleSheet(qdarkstyle.load_stylesheet())
    """,
)
