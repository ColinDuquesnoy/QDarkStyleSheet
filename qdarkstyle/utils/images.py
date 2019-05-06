#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Utilities to process and convert svg images to png using palette colors.
"""

# Standard library imports
from __future__ import absolute_import, division, print_function
import os
import sys
import tempfile

# Third party imports
from qtpy.QtCore import QSize
from qtpy.QtGui import QIcon
from qtpy.QtWidgets import QApplication

# Local imports
from qdarkstyle import _logger, RC_PATH, REPO_PATH, SVG_PATH
from qdarkstyle.palette import DarkPalette


def _get_file_color_map(fname, palette):
    """Return map of files to color from given palette."""
    color_disabled = palette.COLOR_BACKGROUND_NORMAL
    color_focus = palette.COLOR_SELECTION_LIGHT
    color_normal = palette.COLOR_FOREGROUND_DARK

    files_map = {
        'checkbox_checked.svg': {
            'checkbox_checked.svg': color_normal,
            'checkbox_checked_disabled.svg': color_disabled,
            'checkbox_checked_focus.svg': color_focus,
        },
        'checkbox_indeterminate.svg': {
            'checkbox_indeterminate.svg': color_normal,
            'checkbox_indeterminate_disabled.svg': color_disabled,
            'checkbox_indeterminate_focus.svg': color_focus,
        },
        'checkbox_unchecked.svg': {
            'checkbox_unchecked.svg': color_normal,
            'checkbox_unchecked_disabled.svg': color_disabled,
            'checkbox_unchecked_focus.svg': color_focus,
        },
        'radio_checked.svg': {
            'radio_checked.svg': color_normal,
            'radio_checked_disabled.svg': color_disabled,
            'radio_checked_focus.svg': color_focus,
        },
        'radio_unchecked.svg': {
            'radio_unchecked.svg': color_normal,
            'radio_unchecked_disabled.svg': color_disabled,
            'radio_unchecked_focus.svg': color_focus,
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


def create_palette_image(base_svg_path=SVG_PATH, path=REPO_PATH,
                         palette=DarkPalette):
    """Create palette image svg and png image on specified path."""
    # Needed to use QPixmap
    app = QApplication([])

    base_palette_svg_path = os.path.join(base_svg_path, 'palette.svg')
    palette_svg_path = os.path.join(path, 'palette.svg')
    palette_png_path = os.path.join(path, 'palette.png')

    with open(base_palette_svg_path, 'r') as fh:
        data = fh.read()

    color_palette = palette.color_palette()
    for color_name, color_value in color_palette.items():
        data = data.replace('{{ ' + color_name + ' }}', color_value.lower())

    with open(palette_svg_path, 'w') as fh:
        fh.write(data)

    convert_svg_to_png(palette_svg_path, palette_png_path, 4000, 4000)

    _logger().info(palette_svg_path)
    _logger().info(palette_png_path)

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
    for height, ext in heights.items():
        for svg_fname in svg_fnames:
            _logger().info(svg_fname)
            svg_path = os.path.join(base_svg_path, svg_fname)

            color_files = _get_file_color_map(svg_fname, palette=palette)
            for color_svg_name, color in color_files.items():
                temp_svg_path = os.path.join(temp_dir, color_svg_name)
                _logger().info(temp_svg_path)
                _create_colored_svg(svg_path, temp_svg_path, color)
                width = height
                png_fname = color_svg_name.replace('.svg', ext)
                png_path = os.path.join(rc_path, png_fname)
                convert_svg_to_png(temp_svg_path, png_path, height, width)
                _logger().info(png_path)
