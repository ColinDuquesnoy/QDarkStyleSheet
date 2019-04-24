#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""QDarkStyle is a dark stylesheet for Python and Qt applications."""

# Standard library imports
import os

_HERE = os.path.abspath(os.path.dirname(__file__))
PATH_SCSS_VARIABLES = os.path.join(_HERE, '_variables.scss')
PATH_SCSS_MAIN = os.path.join(_HERE, 'main.scss')
VARIABLES = {
    'COLOR_BACKGROUND_LIGHT': '#505F69',
    'COLOR_BACKGROUND_NORMAL': '#32414B',
    'COLOR_BACKGROUND_DARK': '#19232D',
    'COLOR_FOREGROUND_LIGHT': '#F0F0F0',
    'COLOR_FOREGROUND_DARK': '#787878',
    'COLOR_SELECTION_LIGHT': '#148CD2',
    'COLOR_SELECTION_NORMAL': '#1464A0',
    'COLOR_SELECTION_DARK': '#14506E',
    'OPACITY_TOOLTIP': '230',
    'SIZE_BORDER_RADIUS': '4px',
}
