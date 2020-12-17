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
    BACKGROUND_1 = 'GRAY_10'
    BACKGROUND_2 = 'GRAY_20'
    BACKGROUND_3 = 'GRAY_40'
    BACKGROUND_4 = 'GRAY_60'
    BACKGROUND_5 = 'GRAY_60'

    #Text
    TEXT_1 = 'GRAY_150'
    TEXT_2 = 'GRAY_140'
    TEXT_3 = 'GRAY_120'
    TEXT_4 = 'GRAY_100'
    
    #Inverse Text
    INVERSE_TEXT_1 = 'GRAY_150'
    INVERSE_TEXT_2 = 'GRAY_140'
    INVERSE_TEXT_3 = 'GRAY_120'
    INVERSE_TEXT_4 = 'GRAY_100'

    #Accent
    ACCENT_1 = 'BLUE_50'
    ACCENT_2 = 'BLUE_70'
    ACCENT_3 = 'BLUE_90'
    ACCENT_4 = 'BLUE_110'

    #Border
    BORDER_1 = 'GRAY_40'
    BORDER_2 = 'GRAY_50'
    BORDER_3 = 'GRAY_60'
    BORDER_4 = 'GRAY_70'

    #Below colors may belong only to Spyder?

    #Feedback
    SUCCESS_1 = 'GREEN_40'
    SUCCESS_2 = 'GREEN_70'
    SUCCESS_3 = 'GREEN_110'
    ERROR_1 = 'RED_40'
    ERROR_2 = 'RED_70'
    ERROR_3 = 'RED_110'
    WARN_1 = 'ORANGE_40'
    WARN_2 = 'ORANGE_70'
    WARN_3 = 'ORANGE_110'

    #Icon
    ICON_1 = 'GRAY_140'
    ICON_2 = 'BLUE_70'
    ICON_3 = 'GREEN_70'
    ICON_4 = 'RED_70'
    ICON_5 = 'ORANGE_70'
    ICON_6 = 'GRAY_30'

    #Highlight
    HIGHLIGHT_1 = 'GRAY_50' #90%
    HIGHLIGHT_2 = 'GRAY_60' #90%
    HIGHLIGHT_3 = 'GRAY_70' #90%
    HIGHLIGHT_4 = 'GRAY_80' #90%

    #Find
    FIND_1 = 'BLUE_50' #90
    FIND_2 = 'BLUE_60' #90
    FIND_3 = 'BLUE_70' #90
    FIND_4 = 'BLUE_80' #90

    #Group
    GROUP_1 = '#E11C1C'
    GROUP_2 = '#FF8A00'
    GROUP_3 = '#88BA00'
    GROUP_4 = '#2DB500'
    GROUP_5 = '#3FC6F0'
    GROUP_6 = '#107EEC'
    GROUP_7 = '#5C47E0'
    GROUP_8 = '#7F27C5'
    GROUP_9 = '#C88AFA'
    GROUP_10 = '#AF2294'
    GROUP_11 = '#DB4D8E'
    GROUP_12 = '#38D4A4'
    
    # Paths
    PATH_RESOURCES = "':/qss_icons'"

    @classmethod
    def to_dict(cls, colors_only=False):
        """Convert variables to dictionary."""
        order = [
            'BACKGROUND_1',
            'BACKGROUND_2',
            'BACKGROUND_3',
            'BACKGROUND_4',
            'BACKGROUND_5',
            'TEXT_1',
            'TEXT_2',
            'TEXT_3',
            'TEXT_4',
            'INVERSE_TEXT_1',
            'INVERSE_TEXT_2',
            'INVERSE_TEXT_3',
            'INVERSE_TEXT_4',
            'ACCENT_1',
            'ACCENT_2',
            'ACCENT_3',
            'ACCENT_4',
            'BORDER_1',
            'BORDER_2',
            'BORDER_3',
            'BORDER_4',
    #Below colors may belong only to Spyder?
            'SUCCESS_1',
            'SUCCESS_2',
            'SUCCESS_3',
            'ERROR_1',
            'ERROR_2',
            'ERROR_3',
            'WARN_1',
            'WARN_2',
            'WARN_3',
            'ICON_1',
            'ICON_2',
            'ICON_3',
            'ICON_4',
            'ICON_5',
            'ICON_6',
            'HIGHLIGHT_1',
            'HIGHLIGHT_2',
            'HIGHLIGHT_3',
            'HIGHLIGHT_4',
            'FIND_1',
            'FIND_2',
            'FIND_3',
            'FIND_4',
            'GROUP_1',
            'GROUP_2',
            'GROUP_3',
            'GROUP_4',
            'GROUP_5',
            'GROUP_6',
            'GROUP_7',
            'GROUP_8',
            'GROUP_9',
            'GROUP_10',
            'GROUP_11',
            'GROUP_12',
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
