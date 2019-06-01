#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""QDarkStyle default palette."""

# Standard library imports
from collections import OrderedDict


class DarkPalette(object):
    """Theme variables."""

    # Color
    COLOR_BACKGROUND_LIGHT = '#505F69'
    COLOR_BACKGROUND_NORMAL = '#32414B'
    COLOR_BACKGROUND_DARK = '#19232D'

    COLOR_FOREGROUND_LIGHT = '#F0F0F0'
    COLOR_FOREGROUND_NORMAL = '#AAAAAA'
    COLOR_FOREGROUND_DARK = '#787878'

    COLOR_SELECTION_LIGHT = '#148CD2'
    COLOR_SELECTION_NORMAL = '#1464A0'
    COLOR_SELECTION_DARK = '#14506E'

    OPACITY_TOOLTIP = 230

    # Size
    SIZE_BORDER_RADIUS = '4px'

    # Borders
    BORDER_LIGHT = '1px solid $COLOR_BACKGROUND_LIGHT'
    BORDER_NORMAL = '1px solid $COLOR_BACKGROUND_NORMAL'
    BORDER_DARK = '1px solid $COLOR_BACKGROUND_DARK'

    BORDER_SELECTION_LIGHT = '1px solid $COLOR_SELECTION_LIGHT'
    BORDER_SELECTION_NORMAL = '1px solid $COLOR_SELECTION_NORMAL'
    BORDER_SELECTION_DARK = '1px solid $COLOR_SELECTION_DARK'

    # Example of additional widget specific variables
    W_STATUS_BAR_BACKGROUND_COLOR = COLOR_SELECTION_DARK

    # Paths
    PATH_RESOURCES = "':/qss_icons'"

    @classmethod
    def to_dict(cls, colors_only=False):
        """Convert variables to dictionary."""
        order = [
            'COLOR_BACKGROUND_LIGHT',
            'COLOR_BACKGROUND_NORMAL',
            'COLOR_BACKGROUND_DARK',
            'COLOR_FOREGROUND_LIGHT',
            'COLOR_FOREGROUND_NORMAL',
            'COLOR_FOREGROUND_DARK',
            'COLOR_SELECTION_LIGHT',
            'COLOR_SELECTION_NORMAL',
            'COLOR_SELECTION_DARK',
            'OPACITY_TOOLTIP',
            'SIZE_BORDER_RADIUS',
            'BORDER_LIGHT',
            'BORDER_NORMAL',
            'BORDER_DARK',
            'BORDER_SELECTION_LIGHT',
            'BORDER_SELECTION_NORMAL',
            'BORDER_SELECTION_DARK',
            'W_STATUS_BAR_BACKGROUND_COLOR',
            'PATH_RESOURCES',
        ]
        dic = OrderedDict()
        for var in order:
            value = getattr(cls, var)

            if colors_only:
                if not var.startswith('COLOR'):
                    value = None

            if value:
                dic[var] = value

        return dic

    @classmethod
    def color_palette(cls):
        """Return the ordered colored palette dictionary."""
        return cls.to_dict(colors_only=True)
