# -*- coding: utf-8 -*-
"""Script to process QRC files (convert .qrc to _rc.py and .rcc).

The script will attempt to compile the qrc file using the following tools:

    - pyrcc4 for PyQt4 and PyQtGraph (Python)
    - pyrcc5 for PyQt5 and QtPy (Python)
    - pyside-rcc for PySide (Python)
    - pyside2-rcc for PySide2 (Python)
    - rcc for Qt4 and Qt5 (C++)

Delete the compiled files that you don't want to use manually after
running this script.

Links to understand those tools:

    - pyrcc4: http://pyqt.sourceforge.net/Docs/PyQt4/resources.html#pyrcc4
    - pyrcc5: http://pyqt.sourceforge.net/Docs/PyQt5/resources.html#pyrcc5
    - pyside-rcc: https://www.mankier.com/1/pyside-rcc
    - pyside2-rcc: https://doc.qt.io/qtforpython/overviews/resources.html (Documentation Incomplete)
    - rcc on Qt4: http://doc.qt.io/archives/qt-4.8/rcc.html
    - rcc on Qt5: http://doc.qt.io/qt-5/rcc.html

"""

# Standard library imports
from __future__ import absolute_import, print_function
from subprocess import call

import argparse
import glob
import os
import sys

# Third party imports
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

# Local imports
from qdarkstyle.utils import create_qss

# Constants
HERE = os.path.abspath(os.path.dirname(__file__))
REPO_ROOT = os.path.dirname(HERE)
RC_PATH = os.path.join(REPO_ROOT, 'qdarkstyle', 'rc')


class QSSFileHandler(FileSystemEventHandler):
    """QSS File observer."""

    def __init__(self, parser_args):
        """QSS File observer."""
        super(QSSFileHandler, self).__init__()
        self.args = parser_args

    def on_modified(self, event):
        """Handle file system events."""
        if event.src_path.endswith('.qss'):
            run_process(self.args)
            print('\n')


def main(arguments):
    """Process QRC files."""
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--qrc_dir',
                        default=os.path.join(REPO_ROOT, 'qdarkstyle'),
                        type=str,
                        help="QRC file directory, relative to current directory.",)
    parser.add_argument('--create',
                        default='all',
                        choices=['pyqt', 'pyqt5', 'pyside', 'pyside2', 'qtpy', 'pyqtgraph', 'qt', 'qt5', 'all'],
                        type=str,
                        help="Choose which one would be generated.")
    parser.add_argument('--watch', '-w',
                        action='store_true',
                        help="Watch for file changes.")

    args = parser.parse_args(arguments)

    if args.watch:
        path = os.path.join(REPO_ROOT, 'qdarkstyle')
        observer = Observer()
        handler = QSSFileHandler(parser_args=args)
        observer.schedule(handler, path, recursive=True)
        try:
            print('\nWatching QSS file for changes...\nPress Ctrl+C to exit\n')
            observer.start()
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
    else:
        run_process(args)


def run_process(args):
    """Process qrc files."""
    # Generate qrc file based on the content of the resources folder
    generate_qrc_file()

    print('Changing directory to: ', args.qrc_dir)
    os.chdir(args.qrc_dir)

    print('Converting .qrc to _rc.py and/or .rcc ...')

    for qrc_file in glob.glob('*.qrc'):
        # get name without extension
        filename = os.path.splitext(qrc_file)[0]

        print(filename, '...')
        ext = '_rc.py'
        ext_c = '.rcc'

        # Create variables SCSS files and compile SCSS files to QSS
        print('Compiling SCSS/SASS files to QSS ...')
        create_qss()

        # creating names
        py_file_pyqt5 = 'pyqt5_' + filename + ext
        py_file_pyqt = 'pyqt_' + filename + ext
        py_file_pyside = 'pyside_' + filename + ext
        py_file_pyside2 = 'pyside2_' + filename + ext
        py_file_qtpy = 'qtpy_' + filename + ext
        py_file_pyqtgraph = 'pyqtgraph_' + filename + ext

        # calling external commands
        if args.create in ['pyqt', 'pyqtgraph', 'all']:
            print("Compiling for PyQt4 ...")
            try:
                call(['pyrcc4', '-py3', qrc_file, '-o', py_file_pyqt])
            except FileNotFoundError:
                print("You must install pyrcc4")

        if args.create in ['pyqt5', 'qtpy', 'all']:
            print("Compiling for PyQt5 ...")
            try:
                call(['pyrcc5', qrc_file, '-o', py_file_pyqt5])
            except FileNotFoundError:
                print("You must install pyrcc5")

        if args.create in ['pyside', 'all']:
            print("Compiling for PySide ...")
            try:    
                call(['pyside-rcc', '-py3', qrc_file, '-o', py_file_pyside])
            except FileNotFoundError:
                print("You must install pyside-rcc")

        if args.create in ['pyside2', 'all']:
            print("Compiling for PySide 2...")
            try:
                call(['pyside2-rcc', '-py3', qrc_file, '-o', py_file_pyside2])
            except FileNotFoundError:
                print("You must install pyside2-rcc")

        if args.create in ['qtpy', 'all']:
            print("Compiling for QtPy ...")
            # special case - qtpy - syntax is PyQt5
            with open(py_file_pyqt5, 'r') as file:
                filedata = file.read()
            # replace the target string
            filedata = filedata.replace('from PyQt5', 'from qtpy')
            with open(py_file_qtpy, 'w+') as file:
                # write the file out again
                file.write(filedata)

        if args.create in ['pyqtgraph', 'all']:
            print("Compiling for PyQtGraph ...")
            # special case - pyqtgraph - syntax is PyQt4
            with open(py_file_pyqt, 'r') as file:
                filedata = file.read()
            # replace the target string
            filedata = filedata.replace('from PyQt4', 'from pyqtgraph.Qt')
            with open(py_file_pyqtgraph, 'w+') as file:
                # write the file out again
                file.write(filedata)


def generate_qrc_file(resource_prefix='qss_icons', style_prefix='qdarkstyle'):
    """Help."""

    template_header = '''<RCC>
  <qresource prefix="{resource_prefix}">
'''
    template_footer = '''
  </qresource>
  <qresource prefix="{style_prefix}">
      <file>style.qss</file>
  </qresource>
</RCC>
'''
    template_file = '    <file>rc/{fname}</file>'
    files = []
    for fname in sorted(os.listdir(RC_PATH)):
        files.append(template_file.format(fname=fname))

    # Join parts
    qrc_content = (template_header.format(resource_prefix=resource_prefix)
                   + '\n'.join(files)
                   + template_footer.format(style_prefix=style_prefix))

    # Write qrc file
    qrc_path = os.path.join(REPO_ROOT, 'qdarkstyle', 'style.qrc')
    with open(qrc_path, 'w') as fh:
        fh.write(qrc_content)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
