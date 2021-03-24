# -*- coding: utf-8 -*-
"""Script to process UI files (convert .ui to .py).

It compiles .ui files to be used with PyQt4, PyQt5, PySide, QtPy, PyQtGraph.
You just need to run (it has default values) from script folder.

To run this script you need to have these tools available on system:

    - pyuic4 for PyQt4 and PyQtGraph
    - pyuic5 for PyQt5 and QtPy
    - pyside-uic for Pyside
    - pyside2-uic for Pyside2

Links to understand those tools:

    - pyuic4: http://pyqt.sourceforge.net/Docs/PyQt4/designer.html#pyuic4
    - pyuic5: http://pyqt.sourceforge.net/Docs/PyQt5/designer.html#pyuic5
    - pyside-uic: https://www.mankier.com/1/pyside-uic
    - pyside2-uic: https://wiki.qt.io/Qt_for_Python_UiFiles (Documentation Incomplete)

"""

# Standard library imports
from __future__ import absolute_import, print_function
from subprocess import call
import argparse
import glob
import os
import shutil
import string
import sys
import tempfile

# Constants
HERE = os.path.abspath(os.path.dirname(__file__))
REPO_ROOT = os.path.dirname(HERE)
DEFAULT_EXAMPLE_DIR = os.path.join(REPO_ROOT, 'example')
DEFAULT_UI_DIR = os.path.join(DEFAULT_EXAMPLE_DIR, 'ui')
EXAMPLE_TMP_DIR = os.path.join(tempfile.gettempdir(), 'qdarkstyle_example')


def main(arguments):
    """Process UI files."""
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--ui_dir',
                        default=DEFAULT_UI_DIR,
                        type=str,
                        help="UI files directory, relative to current directory.",)
    parser.add_argument('--create',
                        default='qtpy',
                        choices=['pyqt', 'pyqt5', 'pyside', 'pyside2', 'qtpy', 'pyqtgraph', 'all'],
                        type=str,
                        help="Choose which one would be generated.")
    parser.add_argument('--palette',
                        default='dark',
                        choices=['dark', 'light'],
                        type=str,
                        help="Palette to display",)

    args = parser.parse_args(arguments)

    if args.ui_dir == DEFAULT_UI_DIR:
        shutil.rmtree(EXAMPLE_TMP_DIR, ignore_errors=True)
        shutil.copytree(DEFAULT_EXAMPLE_DIR, EXAMPLE_TMP_DIR)
        ui_dir = os.path.join(EXAMPLE_TMP_DIR, 'ui')
    else:
        ui_dir = args.ui_dir

    print('Changing directory to: ', ui_dir)
    os.chdir(ui_dir)

    print('Converting .ui to .py ...')

    for ui_file in glob.glob('*.ui'):

        # Replace palette identifier placeholders
        if args.ui_dir == DEFAULT_UI_DIR:
            with open(ui_file, 'r+') as f:
                contents = f.read()
                template = string.Template(contents)
                contents = template.substitute(ID=args.palette)
                f.seek(0)
                f.write(contents)
                f.truncate()

        # get name without extension
        filename = os.path.splitext(ui_file)[0]
        print(filename, '...')
        ext = '.py'

        # creating names
        py_file_pyqt5 = filename + '_pyqt5_ui' + ext
        py_file_pyqt = filename + '_pyqt_ui' + ext
        py_file_pyside = filename + '_pyside_ui' + ext
        py_file_pyside2 = filename + '_pyside2_ui' + ext
        py_file_qtpy = filename + '_ui' + ext
        py_file_pyqtgraph = filename + '_pyqtgraph_ui' + ext

        # calling external commands
        if args.create in ['pyqt', 'pyqtgraph', 'all']:
            try:
                call(['pyuic4', '--import-from=qdarkstyle', ui_file, '-o', py_file_pyqt])
            except Exception as er:
                print("You must install pyuic4 %s" % str(er))
            else:
                print("Compiling using pyuic4 ...")

        if args.create in ['pyqt5', 'qtpy', 'all']:
            try:
                call(['pyuic5', '--import-from=qdarkstyle', ui_file, '-o', py_file_pyqt5])
            except Exception as er:
                print("You must install pyuic5 %s" % str(er))
            else:
                print("Compiling using pyuic5 ...")

        if args.create in ['pyside', 'all']:
            try:
                call(['pyside-uic', '--import-from=qdarkstyle', ui_file, '-o', py_file_pyside])
            except Exception as er:
                print("You must install pyside-uic %s" % str(er))
            else:
                print("Compiling using pyside-uic ...")

        if args.create in ['pyside2', 'all']:
            try:
                call(['pyside2-uic', '--import-from=qdarkstyle', ui_file, '-o', py_file_pyside2])
            except Exception as er:
                print("You must install pyside2-uic %s" % str(er))
            else:
                print("Compiling using pyside2-uic ...")

        if args.create in ['qtpy', 'all']:
            print("Creating also for qtpy ...")
            # special case - qtpy - syntax is PyQt5
            with open(py_file_pyqt5, 'r') as file:
                filedata = file.read()

            # replace the target string
            filedata = filedata.replace('from PyQt5', 'from qtpy')

            with open(py_file_qtpy, 'w+') as file:
                # write the file out again
                file.write(filedata)

            if args.create not in ['pyqt5']:
                os.remove(py_file_pyqt5)

        if args.create in ['pyqtgraph', 'all']:
            print("Creating also for pyqtgraph ...")
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
