#!python
# -*- coding: utf-8 -*-

"""Script to process UI files.

It compiles .ui files for using PyQt4, PyQt5, PySide, QtPy, PyQtGraph.

To run this script you need to have these tools:
    - pyuic4
    - pyuic5
    - pyside-uic

This is used to compile files for examples.

:since: 2018/02/05
:author: Daniel Cosmo Pizetta
"""

from __future__ import absolute_import
from __future__ import print_function

import argparse
import glob
import os
from subprocess import call
import sys


def main(arguments):
    """Process UI files."""
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--ui_dir', help="UI directory", default='../example/ui', type=str)
    args = parser.parse_args(arguments)

    print('Changing directory to: ', args.ui_dir)
    os.chdir(args.ui_dir)

    print('Converting .ui to .py ...')

    for ui_file in glob.glob('*.ui'):
        # get name without extension
        filename = os.path.splitext(ui_file)[0]
        print(filename, '...')
        ext = '.py'

        # creating names
        py_file_pyqt5 = filename + '_pyqt5_ui' + ext
        py_file_pyqt = filename + '_pyqt_ui' + ext
        py_file_pyside = filename + '_pyside_ui' + ext
        py_file_qtpy = filename + '_qtpy_ui' + ext
        py_file_pyqtgraph = filename + '_pyqtgraph_ui' + ext

        # calling external commands
        call(['pyuic5', '--from-imports', ui_file, '-o', py_file_pyqt5])
        call(['pyuic4', '--from-imports', ui_file, '-o', py_file_pyqt])
        call(['pyside-uic', '--from-imports', ui_file, '-o', py_file_pyside])

        # special case - qtpy - syntax is PyQt5
        with open(py_file_pyqt5, 'r') as file:
            filedata = file.read()
        # replace the target string
        filedata = filedata.replace('from PyQt5', 'from qtpy')
        with open(py_file_qtpy, 'w+') as file:
            # write the file out again
            file.write(filedata)

        # special case - pyqtgraph - syntax is PyQt4
        with open(py_file_pyqt, 'r') as file:
            filedata = file.read()
        # replace the target string
        filedata = filedata.replace('from PyQt4', 'from pyqtgraph.Qt')
        with open(py_file_pyqtgraph, 'w+') as file:
            # write the file out again
            file.write(filedata)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
