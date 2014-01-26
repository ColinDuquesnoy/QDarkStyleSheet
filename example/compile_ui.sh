#!/bin/sh
# Compile example.ui for PyQt and PySide.
pyuic4 --from-imports example.ui >  example_pyqt_ui.py
pyside-uic --from-imports example.ui >  example_pyside_ui.py