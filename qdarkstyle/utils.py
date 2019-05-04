#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""QDarkStyle is a dark stylesheet for Python and Qt applications."""

# Standard library imports
import os

# Third party imports
try:
    import qtsass
    QTSASS_INSTALLED = True
except ImportError:
    QTSASS_INSTALLED = False


# Local imports
from qdarkstyle.qss import DarkPalette, PATH_SCSS_MAIN, PATH_SCSS_VARIABLES

# Constants
_HEADER_SCSS = '''// ---------------------------------------------------------------------------
//
//    File created programmatically
//
//    WARNING! All changes made in this file will be lost!
//
//----------------------------------------------------------------------------
'''
_HEADER_QSS = '''/* ---------------------------------------------------------------------------

    Created by the qtsass compiler

    WARNING! All changes made in this file will be lost!

--------------------------------------------------------------------------- */
'''
_HERE = os.path.abspath(os.path.dirname(__file__))
PATH_CSS_STYLES = os.path.join(_HERE, 'style.qss')


def _dict_to_scss(data):
    """Create a scss variables string from a dict."""
    lines = []
    template = "${}: {};"
    for key, value in data.items():
        lines.append(template.format(key, value))

    return '\n'.join(lines)


def _scss_to_dict(string):
    """Parse variables and return a dict."""
    data = {}
    lines = string.split('\n')

    for line in lines:
        line = line.strip()

        if line and line.startswith('$'):
            key, value = line.split(':')
            key = key[1:].strip()
            key = key.replace('-', '_')
            value = value.split(';')[0].strip()

            data[key] = value

    return data


def _create_scss_variables():
    """Create a scss variables file."""
    scss = _dict_to_scss(Variables._to_dict())
    data = _HEADER_SCSS + scss + '\n'

    with open(PATH_SCSS_VARIABLES, 'w') as f:
        f.write(data)


def _create_qss():
    """Create a styles.qss file from qtsass."""
    if QTSASS_INSTALLED:
        qtsass.compile_filename(PATH_SCSS_MAIN, PATH_CSS_STYLES,
                                output_style='expanded')

        with open(PATH_CSS_STYLES, 'r') as f:
            data = f.read()

        data = _HEADER_QSS + data

        with open(PATH_CSS_STYLES, 'w') as f:
            f.write(data)


def create_qss():
    """Create variables files and run qtsass compilation."""
    _create_scss_variables()
    _create_qss()


if __name__ == '__main__':
    create_qss()
