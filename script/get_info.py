
# -*- coding: utf-8 -*-
"""Script to get system information."""

# Standard library imports
from __future__ import absolute_import, print_function
import os
import sys

# Local imports
import qdarkstyle


def get_info():
    """Process UI files."""
    info = []
    info.append('QDarkStyle: %s' % qdarkstyle.__version__)
    info.append('OS: %s' % sys.platform)
    info.append('Python: %s' % sys.version)
    info.append('QT_API: %s' % os.environ.get('QT_API', None))
    info.append('PYQTGRAPH_QT_LIB: %s' % os.environ.get('PYQTGRAPH_QT_LIB', None))
    for item in info:
        print(item)

if __name__ == '__main__':
    sys.exit(get_info())
