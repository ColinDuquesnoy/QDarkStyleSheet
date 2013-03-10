#!/usr/bin/env python
"""
Compiles the qrc file using rcc, pyside-rcc and pyrcc4.
"""
import os

# Compile for use with Qt (c++)
print("Compiling for Qt: style.qrc -> style.rcc")
os.system("rcc style.qrc -o style.rcc")

# Compile for use with PyQt4
print("Compiling for PyQt4: style.qrc -> style_pyqt_rc.py")
os.system("pyrcc4 style.qrc -o style_pyqt_rc.py")

# Compile for use with PySide
print("Compiling for PySide: style.qrc -> style_pyside_rc.py")
os.system("pyside-rcc style.qrc -o style_pyside_rc.py")

