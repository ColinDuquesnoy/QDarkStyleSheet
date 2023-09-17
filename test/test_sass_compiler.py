# -*- coding: utf-8 -*-
"""Test the qtsass is compiling the SCSS files to QSS."""

# Standard library imports
import tempfile

# Local imports
from qdarkstyle.dark.palette import DarkPalette
from qdarkstyle.light.palette import LightPalette
from qdarkstyle.palette import Palette
from qdarkstyle.utils.scss import create_custom_qss, create_qss, create_custom_qss_from_palette


def test_create_qss_dark():
    # Should not raise a CompileError
    create_qss(DarkPalette)


def test_create_qss_light():
    # Should not raise a CompileError
    create_qss(LightPalette)


# TODO: update this test and create_custom_qss for the new Palette class
# def test_create_custom_qss():
#     # Should not raise a CompileError

#     qss = create_custom_qss(
#         'MyAwesomePalette',
#         tempfile.mkdtemp(),
#         '#ff0000',
#         '#cc0000',
#         '#aa0000',
#         '#00ff00',
#         '#00cc00',
#         '#00aa00',
#         '#0000ff',
#         '#0000cc',
#         '#0000aa',
#         '0px',
#     )
#     assert qss
