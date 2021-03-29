#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Process qrc, ui, image, and screenshot files, then run example in while loop.
"""

# Standard library imports
from __future__ import absolute_import, print_function

import argparse
from subprocess import call
import os
import sys
import tempfile

# Constants
SCRIPTS_PATH = os.path.abspath(os.path.dirname(__file__))

def main():
    """Process qrc and ui files, then run example in while loop."""
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--palette',
                        default='dark',
                        choices=['dark', 'light'],
                        type=str,
                        help="Palette to display",)

    # Parsing arguments from command line
    args = parser.parse_args()
    palette = args.palette

    dark = None
    no_dark = None
    themes = {'Dark': dark, 'No Dark': no_dark}
    while True:
        for theme_name, theme_process in themes.items():
            try:
                theme_process.kill()
            except AttributeError:
                print(theme_name + ' not running!')
            except Exception:
                print(theme_name + ' still running!')
            else:
                print(theme_name + ' was killed!')

        print(sys.argv)

        # Process qrc files
        process_qrc = os.path.join(SCRIPTS_PATH, '../qdarkstyle/utils/__main__.py')
        call(['python', process_qrc])

        # Show window
        example = os.path.join(SCRIPTS_PATH, '../qdarkstyle/example/__main__.py')
        call(['python', example, '--screenshots', '--palette', palette])
        call(['python', example, '--no_dark', '--screenshots'])

        # Open dark example
        dark = call(['python', example] + sys.argv[1:])

        # Open no dark example
        no_dark = call(['python', example, '--no_dark'] + sys.argv[1:])

        if dark or no_dark:
            print('Unf! It not worked! Please, check the error(s).')
            break


if __name__ == "__main__":
    sys.exit(main())
