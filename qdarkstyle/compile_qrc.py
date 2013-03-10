#!/usr/bin/env python
"""
Utiliy scripts to compile the qrc file. The script will 
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
    print("Compiling for Qt: style.qrc -> style.rcc")
    os.system("rcc style.qrc -o style.rcc")
    print("Compiling for PyQt4: style.qrc -> pyqt_style_rc.py")
    os.system("pyrcc4 style.qrc -o pyqt_style_rc.py")
    print("Compiling for PySide: style.qrc -> pyside_style_rc.py")
    os.system("pyside-rcc style.qrc -o pyside_style_rc.py")


if __name__ == "__main__":
    compile_all()

