#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Process qrc and ui files, then run example in while loop."""

# Standard library imports
from __future__ import absolute_import, print_function
from subprocess import call
import os
import sys

# Constants
HERE = os.path.abspath(os.path.dirname(__file__))
REPO_ROOT = os.path.dirname(HERE)


def main():
    """Process qrc and ui files, then run example in while loop."""
    dark = None
    no_dark = None

    while True:
        try:
            dark.kill()
        except AttributeError:
            print('Dark not running!')
        except Exception:
            print('Dark still running!')
        else:
            print('Dark was killed!')

        try:
            no_dark.kill()
        except AttributeError:
            print('No Dark not running!')
        except Exception:
            print('No Dark still running!')
        else:
            print('No Dark was killed!')

        print(sys.argv)

        # process qrc files
        process_qrc = os.path.join(HERE, 'process_qrc.py')
        call(['python', process_qrc])
        # process ui files
        process_ui = os.path.join(HERE, 'process_ui.py')
        call(['python', process_ui])
        # open dark example
        example = os.path.join(REPO_ROOT, 'example', 'example.py')
        dark = call(['python', example] + sys.argv[1:])
        # open no dark example
        no_dark = call(['python', example, '--no_dark'] + sys.argv[1:])

        if dark or no_dark:
            print('Unf! It not worked! Please, check the error(s).')
            break


if __name__ == "__main__":
    sys.exit(main())
