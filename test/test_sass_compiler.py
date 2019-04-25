#!python
# -*- coding: utf-8 -*-
"""Test the qtsass is compiling the SCSS files to QSS."""

# Local imports
from qdarkstyle.utils import create_qss


def test_create_qss():
    # Should not raise a CompileError
    create_qss()
