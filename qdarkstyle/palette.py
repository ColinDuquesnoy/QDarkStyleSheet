#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""QDarkStyle default palette."""

# Standard library imports
from collections import OrderedDict


class DarkPalette(object):
    """Theme variables."""

    # Color
    """COLOR_BACKGROUND_LIGHT = '#505F69'
    COLOR_BACKGROUND_NORMAL = '#32414B'
    COLOR_BACKGROUND_DARK = '#19232D'

    COLOR_FOREGROUND_LIGHT = '#F0F0F0'
    COLOR_FOREGROUND_NORMAL = '#AAAAAA'
    COLOR_FOREGROUND_DARK = '#787878'

    COLOR_SELECTION_LIGHT = '#148CD2'
    COLOR_SELECTION_NORMAL = '#1464A0'
    COLOR_SELECTION_DARK = '#14506E'"""

    OPACITY_TOOLTIP = 230

    # Size
    SIZE_BORDER_RADIUS = '4px'

    # Borders
   """ BORDER_LIGHT = '1px solid $COLOR_BACKGROUND_LIGHT'
    BORDER_NORMAL = '1px solid $COLOR_BACKGROUND_NORMAL'
    BORDER_DARK = '1px solid $COLOR_BACKGROUND_DARK'

    BORDER_SELECTION_LIGHT = '1px solid $COLOR_SELECTION_LIGHT'
    BORDER_SELECTION_NORMAL = '1px solid $COLOR_SELECTION_NORMAL'
    BORDER_SELECTION_DARK = '1px solid $COLOR_SELECTION_DARK'

    # Example of additional widget specific variables
    W_STATUS_BAR_BACKGROUND_COLOR = COLOR_SELECTION_DARK"""
    
    # Color
    # Background
    COLOR_BACKGROUND_1 = 'GRAY_10'
    COLOR_BACKGROUND_2 = 'GRAY_20'
    COLOR_BACKGROUND_3 = 'GRAY_40'
    COLOR_BACKGROUND_4 = 'GRAY_60'
    COLOR_BACKGROUND_5 = 'GRAY_60'

    #Text
    COLOR_TEXT_1 = 'GRAY_150'
    COLOR_TEXT_2 = 'GRAY_140'
    COLOR_TEXT_3 = 'GRAY_120'
    COLOR_TEXT_4 = 'GRAY_100'
    
    #Inverse Text
    COLOR_INVERSE_TEXT_1 = 'GRAY_150'
    COLOR_INVERSE_TEXT_2 = 'GRAY_140'
    COLOR_INVERSE_TEXT_3 = 'GRAY_120'
    COLOR_INVERSE_TEXT_4 = 'GRAY_100'

    #Accent
    COLOR_ACCENT_1 = 'BLUE_50'
    COLOR_ACCENT_2 = 'BLUE_70'
    COLOR_ACCENT_3 = 'BLUE_90'
    COLOR_ACCENT_4 = 'BLUE_110'

    #Border
    COLOR_BORDER_1 = 'GRAY_40'
    COLOR_BORDER_2 = 'GRAY_50'
    COLOR_BORDER_3 = 'GRAY_60'
    COLOR_BORDER_4 = 'GRAY_70'

    #Below colors may belong only to Spyder?

    #Feedback
    COLOR_SUCCESS_1 = 'GREEN_40'
    COLOR_SUCCESS_2 = 'GREEN_70'
    COLOR_SUCCESS_3 = 'GREEN_110'
    COLOR_ERROR_1 = 'RED_40'
    COLOR_ERROR_2 = 'RED_70'
    COLOR_ERROR_3 = 'RED_110'
    COLOR_WARN_1 = 'ORANGE_40'
    COLOR_WARN_2 = 'ORANGE_70'
    COLOR_WARN_3 = 'ORANGE_110'

    #Icon
    COLOR_ICON_1 = 'GRAY_140'
    COLOR_ICON_2 = 'BLUE_70'
    COLOR_ICON_3 = 'GREEN_70'
    COLOR_ICON_4 = 'RED_70'
    COLOR_ICON_5 = 'ORANGE_70'
    COLOR_ICON_6 = 'GRAY_30'

    #Highlight
    COLOR_HIGHLIGHT_1 = 'GRAY_50' #90%
    COLOR_HIGHLIGHT_2 = 'GRAY_60' #90%
    COLOR_HIGHLIGHT_3 = 'GRAY_70' #90%
    COLOR_HIGHLIGHT_4 = 'GRAY_80' #90%

    #Find
    COLOR_FIND_1 = 'BLUE_50' #90
    COLOR_FIND_2 = 'BLUE_60' #90
    COLOR_FIND_3 = 'BLUE_70' #90
    COLOR_FIND_4 = 'BLUE_80' #90

    #Group
    COLOR_GROUP_1 = '#E11C1C'
    COLOR_GROUP_2 = '#FF8A00'
    COLOR_GROUP_3 = '#88BA00'
    COLOR_GROUP_4 = '#2DB500'
    COLOR_GROUP_5 = '#3FC6F0'
    COLOR_GROUP_6 = '#107EEC'
    COLOR_GROUP_7 = '#5C47E0'
    COLOR_GROUP_8 = '#7F27C5'
    COLOR_GROUP_9 = '#C88AFA'
    COLOR_GROUP_10 = '#AF2294'
    COLOR_GROUP_11 = '#DB4D8E'
    COLOR_GROUP_12 = '#38D4A4'
    
    # Paths
    PATH_RESOURCES = "':/qss_icons'"

    @classmethod
    def to_dict(cls, colors_only=False):
        """Convert variables to dictionary."""
        order = [
            'COLOR_BACKGROUND_1',
            'COLOR_BACKGROUND_2',
            'COLOR_BACKGROUND_3',
            'COLOR_BACKGROUND_4',
            'COLOR_BACKGROUND_5',
            'COLOR_TEXT_1',
            'COLOR_TEXT_2',
            'COLOR_TEXT_3',
            'COLOR_TEXT_4',
            'COLOR_INVERSE_TEXT_1',
            'COLOR_INVERSE_TEXT_2',
            'COLOR_INVERSE_TEXT_3',
            'COLOR_INVERSE_TEXT_4',
            'COLOR_ACCENT_1',
            'COLOR_ACCENT_2',
            'COLOR_ACCENT_3',
            'COLOR_ACCENT_4',
            'COLOR_BORDER_1',
            'COLOR_BORDER_2',
            'COLOR_BORDER_3',
            'COLOR_BORDER_4',
    #Below colors may belong only to Spyder?
            'COLOR_SUCCESS_1',
            'COLOR_SUCCESS_2',
            'COLOR_SUCCESS_3',
            'COLOR_ERROR_1',
            'COLOR_ERROR_2',
            'COLOR_ERROR_3',
            'COLOR_WARN_1',
            'COLOR_WARN_2',
            'COLOR_WARN_3',
            'COLOR_ICON_1',
            'COLOR_ICON_2',
            'COLOR_ICON_3',
            'COLOR_ICON_4',
            'COLOR_ICON_5',
            'COLOR_ICON_6',
            'COLOR_HIGHLIGHT_1',
            'COLOR_HIGHLIGHT_2',
            'COLOR_HIGHLIGHT_3',
            'COLOR_HIGHLIGHT_4',
            'COLOR_FIND_1',
            'COLOR_FIND_2',
            'COLOR_FIND_3',
            'COLOR_FIND_4',
            'COLOR_GROUP_1',
            'COLOR_GROUP_2',
            'COLOR_GROUP_3',
            'COLOR_GROUP_4',
            'COLOR_GROUP_5',
            'COLOR_GROUP_6',
            'COLOR_GROUP_7',
            'COLOR_GROUP_8',
            'COLOR_GROUP_9',
            'COLOR_GROUP_10',
            'COLOR_GROUP_11',
            'COLOR_GROUP_12',
        #Pre-existing non colors
            'OPACITY_TOOLTIP',
            'SIZE_BORDER_RADIUS',
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
