#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Process and convert svg images to png."""

from __future__ import absolute_import, division, print_function

# Standard library imports
import os
import sys

# Third party imports
from qtpy.QtCore import QSize
from qtpy.QtGui import QIcon
from qtpy.QtWidgets import QApplication

# Local imports
from qdarkstyle.qss import Variables

# Constants
HERE = os.path.abspath(os.path.dirname(__file__))
ROOT_PATH = os.path.dirname(HERE)
SVG_PATH = os.path.join(ROOT_PATH, 'svg')
RC_PATH = os.path.join(ROOT_PATH, 'qdarkstyle', 'rc', )


def replace_fill_color(path_svg, color, new_color):
    """"""
    temp_path = ''
    return temp_path


def convert_svg_to_png(path_svg, path_png, width):
    """Convert svg files to png files."""
    size = QSize(width, width)
    img = QIcon(path_svg).pixmap(size).toImage()
    img.save(path_png)


def main():
    """"""
    app = QApplication([])
    sizes = {
        32: '.png',
        64: '@2x.png',
    }
    for size, ext in sizes.items():
        for f in os.listdir(SVG_PATH):
            path_svg = os.path.join(SVG_PATH, f)
            path_png = os.path.join(RC_PATH, f)
            path_png = path_png.replace('.svg', ext)
            convert_svg_to_png(path_svg, path_png, size)
            print(path_png)


if __name__ == "__main__":
    sys.exit(main())
