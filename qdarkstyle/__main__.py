#!/usr/bin/env python
# -*- coding: utf-8 -*-

from qdarkstyle import qt_bindings, qt_abstractions, information, __version__
import qdarkstyle
import argparse
import sys

from os.path import abspath, dirname
sys.path.insert(0, abspath(dirname(abspath(__file__)) + '/..'))


def print_list_md(info):
    """Print a list of information, line by line."""
    for item in info:
        print('  - ' + item)


def main():
    """Execute QDarkStyle example."""
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-i', '--information', action='store_true',
                        help="Show information about environment (important for bug report)")
    parser.add_argument('-b', '--bindings', action='store_true',
                        help="Show available bindings for Qt")
    parser.add_argument('-a', '--abstractions', action='store_true',
                        help="Show available abstraction layers for Qt bindings")
    # parser.add_argument('-e', '--example', action='store_true',
    #                     help="Show qdarkstyle example, subcommand.")
    parser.add_argument('-v', '--version', action='store_true',
                        help="Show qdarkstyle version")
    parser.add_argument('--all', action='store_true',
                        help="Show all information options at once")

    # parsing arguments from command line
    args = parser.parse_args()

    parser.print_help()

    if args.information or args.all:
        info = information()
        print('\nInformation about your current environment setup:')
        print_list_md(info)

    if args.bindings or args.all:
        info = qt_bindings()
        print('\nQt bindings available:')
        print_list_md(info)

    if args.abstractions or args.all:
        info = qt_abstractions()
        print('\nQt abstraction layers available:')
        print_list_md(info)

    if args.version:
        info = __version__
        print('\nVersion: %s' % info)

    # if args.example:
    #     example.main()


if __name__ == "__main__":
    sys.exit(main())
