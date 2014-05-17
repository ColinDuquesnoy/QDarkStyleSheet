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
Utility scripts to compile the qrc file. The script will
attempt to compile the qrc file using the following tools:
    - rcc
    - pyside-rcc
    - pyrcc4

Delete the compiled files that you don't want to use 
manually after running this script.
"""
import os


def compile_all():
    """
    Compile style.qrc using rcc, pyside-rcc and pyrcc4
    """
    # print("Compiling for Qt: style.qrc -> style.rcc")
    # os.system("rcc style.qrc -o style.rcc")
    print("Compiling for PyQt4: style.qrc -> pyqt_style_rc.py")
    os.system("pyrcc4 -py3 style.qrc -o pyqt_style_rc.py")
    print("Compiling for PyQt5: style.qrc -> pyqt5_style_rc.py")
    os.system("pyrcc5 style.qrc -o pyqt5_style_rc.py")
    print("Compiling for PySide: style.qrc -> pyside_style_rc.py")
    os.system("pyside-rcc -py3 style.qrc -o pyside_style_rc.py")


if __name__ == "__main__":
    compile_all()
