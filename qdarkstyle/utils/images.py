#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Process and convert svg images to png using palette colors."""

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
from qdarkstyle.qss import DarkPalette

# Constants
HERE = os.path.abspath(os.path.dirname(__file__))
ROOT_PATH = os.path.dirname(HERE)
SVG_PATH = os.path.join(ROOT_PATH, 'svg')
RC_PATH = os.path.join(ROOT_PATH, 'qdarkstyle', 'rc', )
BASE_COLOR = '#ff0000'


def get_file_color_map(fname, palette=DarkPalette):
    """Return map of files to color from given palette."""
    color_normal = palette.COLOR_FOREGROUND_DARK
    color_focus = palette.COLOR_SELECTION_LIGHT
    color_disabled = palette.COLOR_BACKGROUND_NORMAL
    files_map = {
        'checkbox_checked.svg': {
            'checkbox_checked.svg': color_normal,
            'checkbox_checked_focus.svg': color_focus,
            'checkbox_checked_disabled.svg': color_disabled,
        },
        'checkbox_indeterminate.svg': {
            'checkbox_indeterminate.svg': color_normal,
            'checkbox_indeterminate_focus.svg': color_focus,
            'checkbox_indeterminate_disabled.svg': color_disabled,
        },
        'checkbox_unchecked.svg': {
            'checkbox_unchecked.svg': color_normal,
            'checkbox_unchecked_focus.svg': color_focus,
            'checkbox_unchecked_disabled.svg': color_disabled,
        },
        'radio_checked.svg': {
            'radio_checked.svg': color_normal,
            'radio_checked_focus.svg': color_focus,
            'radio_checked_disabled.svg': color_disabled,
        },
        'radio_unchecked.svg': {
            'radio_unchecked.svg': color_normal,
            'radio_unchecked_focus.svg': color_focus,
            'radio_unchecked_disabled.svg': color_disabled,
        }
    }
    for f, file_colors in files_map.items():
        if f == fname:
            break

    assert file_colors

    return file_colors


def create_colored_svg(svg_path, temp_svg_path, base_color, new_color):
    """Replace base svg with new fill color."""
    with open(svg_path, 'r') as fh:
        data = fh.read()

    new_data = data.replace(base_color, new_color)

    with open(temp_svg_path, 'w') as fh:
        fh.write(new_data)


def convert_svg_to_png(svg_path, png_path, height, width):
    """Convert svg files to png files using Qt."""
    size = QSize(height, width)
    icon = QIcon(svg_path)
    pixmap = icon.pixmap(size)
    img = pixmap.toImage()
    img.save(png_path)


def create_palette_image():
    """Create palette image on repo root."""
    base_palette_svg_path = os.path.join(SVG_PATH, 'palette.svg')
    palette_svg_path = os.path.join(ROOT_PATH, 'palette.svg')
    palette_png_path = os.path.join(ROOT_PATH, 'palette.png')

    with open(base_palette_svg_path, 'r') as fh:
        data = fh.read()

    color_palette = DarkPalette.color_palette()
    for color_name, color_value in color_palette.items():
        data = data.replace('{{ ' + color_name + ' }}', color_value.lower())

    with open(palette_svg_path, 'w') as fh:
        fh.write(data)

    convert_svg_to_png(palette_svg_path, palette_png_path, 4000, 4000)
    return palette_svg_path, palette_png_path


def main():
    """Run main image processing routine."""
    app = QApplication([])

    palette_svg_path, palette_png_path = create_palette_image()
    print('\n' + palette_svg_path)
    print(palette_png_path)
    print('\n')

    temp_dir = tempfile.mkdtemp()
    svg_fnames = [f for f in os.listdir(SVG_PATH) if f.endswith('.svg')]

    # See: https://doc.qt.io/qt-5/scalability.html
    heights = {
        32: '.png',
        64: '@2x.png',
    }
    for height, ext in heights.items():
        for svg_fname in svg_fnames:
            print('\n' + svg_fname)
            svg_path = os.path.join(SVG_PATH, svg_fname)

            color_files = get_file_color_map(svg_fname)
            for color_svg_name, color in color_files.items():
                temp_svg_path = os.path.join(temp_dir, color_svg_name)
                print('\n    ' + temp_svg_path)
                base_color = BASE_COLOR
                create_colored_svg(svg_path, temp_svg_path, base_color, color)

                width = height
                png_fname = color_svg_name.replace('.svg', ext)
                png_path = os.path.join(RC_PATH, png_fname)
                convert_svg_to_png(temp_svg_path, png_path, height, width)
                print('    ' + png_path)
    print('\n')


if __name__ == "__main__":
    sys.exit(main())
