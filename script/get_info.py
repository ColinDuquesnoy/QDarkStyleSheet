
# -*- coding: utf-8 -*-
"""Script to get system information.
"""

from __future__ import absolute_import, print_function

import os
import sys
import qdarkstyle

def get_info():
    """Process UI files."""
    info = []
    info.append('QDarkStyle: ', qdarkstyle.__version__)
    info.append('OS: ', sys.platform)
    info.append('Python: ', sys.version)
    info.append('QT_API: ', os.getenv['QT_API'])
    info.append('PYQTGRAPH_QT_LIB: ', os.getenv['PYQTGRAPH_QT_LIB'])
    for item in info:
        print(item)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
