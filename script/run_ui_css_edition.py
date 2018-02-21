#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Process qrc and ui files, then run example in while loop."""

from __future__ import absolute_import, print_function

import sys
from subprocess import call


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
        call(['python', 'process_qrc.py'])
        # process ui files
        call(['python', 'process_ui.py'])
        # open dark example
        dark = call(['python', '../example/example.py'] + sys.argv[1:])
        # open no dark example
        no_dark = call(['python', '../example/example.py', '--no_dark'] + sys.argv[1:])

        if dark or no_dark:
            print('Unf! It not worked! Please, check the error(s).')
            break


if __name__ == "__main__":
    sys.exit(main())
