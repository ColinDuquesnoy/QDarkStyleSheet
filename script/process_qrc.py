#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Utility scripts to compile the qrc file. The script will
attempt to compile the qrc file using the following tools:
    - rcc (not used)
    - pyside-rcc
    - pyrcc4
    - pyrcc5

Delete the compiled files that you don't want to use manually after
running this script.
"""
import os


def compile_all():
    """
    Compile style.qrc using rcc, pyside-rcc, pyrcc4 and pyrcc5.
    """
    qrc_dir = '../qdarkstyle'
    print('Changing directory to: ', qrc_dir)
    os.chdir(qrc_dir)

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
