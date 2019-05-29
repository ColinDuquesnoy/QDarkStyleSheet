#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Utilities to process and convert svg images to png using palette colors.
"""

# Standard library imports
from __future__ import absolute_import, division, print_function

import logging
import os
import tempfile

# Third party imports
from qtpy.QtCore import QSize
from qtpy.QtGui import QIcon
from qtpy.QtWidgets import QApplication

# Local imports
from qdarkstyle import IMAGES_PATH, RC_PATH, SVG_PATH
from qdarkstyle.palette import DarkPalette

IMAGE_BLACKLIST = ['base_palette']

_logger = logging.getLogger(__name__)


def _get_file_color_map(fname, palette):
    """Return map of files to color from given palette."""
    color_disabled = palette.COLOR_BACKGROUND_NORMAL
    color_focus = palette.COLOR_SELECTION_LIGHT
    color_pressed = palette.COLOR_SELECTION_NORMAL
    color_normal = palette.COLOR_FOREGROUND_DARK

    name, ext = fname.split('.')

    files_map = {
        fname: {
            fname: color_normal,
            name + '_disabled.' + ext: color_disabled,
            name + '_focus.' + ext: color_focus,
            name + '_pressed.' + ext: color_pressed,
        }
    }

    for f, file_colors in files_map.items():
        if f == fname:
            break

    assert file_colors

    return file_colors


def _create_colored_svg(svg_path, temp_svg_path, color):
    """Replace base svg with fill color."""
    with open(svg_path, 'r') as fh:
        data = fh.read()

    base_color = '#ff0000'  # Hardcoded in base svg files
    new_data = data.replace(base_color, color)

    with open(temp_svg_path, 'w') as fh:
        fh.write(new_data)


def convert_svg_to_png(svg_path, png_path, height, width):
    """Convert svg files to png files using Qt."""
    size = QSize(height, width)
    icon = QIcon(svg_path)
    pixmap = icon.pixmap(size)
    img = pixmap.toImage()
    img.save(png_path)


def create_palette_image(base_svg_path=SVG_PATH, path=IMAGES_PATH,
                         palette=DarkPalette):
    """Create palette image svg and png image on specified path."""
    # Needed to use QPixmap
    _ = QApplication([])

    base_palette_svg_path = os.path.join(base_svg_path, 'base_palette.svg')
    palette_svg_path = os.path.join(path, 'palette.svg')
    palette_png_path = os.path.join(path, 'palette.png')

    _logger.info("Creating palette image ...")
    _logger.info("Base: %s" % base_palette_svg_path)
    _logger.info("From: %s" % palette_svg_path)
    _logger.info("To  : %s" % palette_png_path)

    with open(base_palette_svg_path, 'r') as fh:
        data = fh.read()

    color_palette = palette.color_palette()

    for color_name, color_value in color_palette.items():
        data = data.replace('{{ ' + color_name + ' }}', color_value.lower())

    with open(palette_svg_path, 'w+') as fh:
        fh.write(data)

    convert_svg_to_png(palette_svg_path, palette_png_path, 4000, 4000)

    return palette_svg_path, palette_png_path


def create_images(base_svg_path=SVG_PATH, rc_path=RC_PATH,
                  palette=DarkPalette):
    """
    Create resources `rc` png image files from base svg files and palette.
    """
    # Needed to use QPixmap
    app = QApplication([])

    temp_dir = tempfile.mkdtemp()
    svg_fnames = [f for f in os.listdir(base_svg_path) if f.endswith('.svg')]

    # See: https://doc.qt.io/qt-5/scalability.html
    heights = {
        32: '.png',
        64: '@2x.png',
    }

    _logger.info("Creating images ...")
    _logger.info("SVG folder: %s" % base_svg_path)
    _logger.info("TMP folder: %s" % temp_dir)
    _logger.info("PNG folder: %s" % rc_path)

    num_svg = len(svg_fnames)
    num_png = 0
    num_ignored = 0

    for height, ext in heights.items():

        for svg_fname in svg_fnames:
            svg_name = svg_fname.split('.')[0]

            if svg_name not in IMAGE_BLACKLIST:
                svg_path = os.path.join(base_svg_path, svg_fname)
                color_files = _get_file_color_map(svg_fname, palette=palette)

                _logger.debug(" Working: %s"
                                % os.path.basename(svg_path))

                for color_svg_name, color in color_files.items():
                    temp_svg_path = os.path.join(temp_dir, color_svg_name)
                    _create_colored_svg(svg_path, temp_svg_path, color)

                    _logger.debug("  Temporary: %s"
                                    % os.path.basename(temp_svg_path))

                    width = height
                    png_fname = color_svg_name.replace('.svg', ext)
                    png_path = os.path.join(rc_path, png_fname)
                    num_png += 1

                    convert_svg_to_png(temp_svg_path, png_path, height, width)

                    _logger.debug("  Creating: %s"
                                    % os.path.basename(png_path))
            else:
                num_ignored += 1
                _logger.debug(" Ignored blacklist: %s"
                                % os.path.basename(svg_path))

    _logger.info("# SVG files: %s" % num_svg)
    _logger.info("# PNG files: %s" % num_png)
    _logger.info("# SVG ignored: %s" % num_ignored)
