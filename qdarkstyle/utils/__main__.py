# -*- coding: utf-8 -*-
"""Script to process QRC files (convert .qrc to _rc.py and .rcc).

The script will attempt to compile the qrc file using the following tools:

    - `pyside6-rcc` for PySide6 and QtPy (Python) (Official)
    - There is no specific rcc compiler for PyQt6, use `pyside6-rcc` (Python)
    - `pyrcc5` for PyQt5 (Python)
    - `pyside2-rcc` for PySide2 (Python)
    - `rcc` for Qt5/Qt6 (C++)

Delete the compiled files that you don't want to use manually after
running this script.

Links to understand those tools:

    - `pyside6-rcc`: https://doc.qt.io/qtforpython/tutorials/basictutorial/qrcfiles.html (Official)
    - `pyrcc5`: http://pyqt.sourceforge.net/Docs/PyQt5/resources.html#pyrcc5 (Official)
    - `pyside2-rcc`: https://doc.qt.io/qtforpython/overviews/resources.html (Documentation Incomplete)
    - `rcc` on Qt6: https://doc.qt.io/qt-6/resources.html (Official)
    - `rcc` on Qt5: http://doc.qt.io/qt-5/rcc.html (Official)

"""

# Standard library imports
import argparse
import importlib.util
import logging
import sys

# Third party imports
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

# Local imports
from qdarkstyle import PACKAGE_PATH, SVG_PATH, IMAGES_PATH
from qdarkstyle.palette import Palette
from qdarkstyle.dark.palette import DarkPalette
from qdarkstyle.light.palette import LightPalette
from qdarkstyle.utils import process_palette

_logger = logging.getLogger(__name__)


class QSSFileHandler(FileSystemEventHandler):
    """QSS File observer."""

    def __init__(self, parser_args):
        """QSS File observer."""
        super(QSSFileHandler, self).__init__()
        self.args = parser_args

    def on_modified(self, event):
        """Handle file system events."""
        if event.src_path.endswith("palette.py"):
            # TODO: needs implementation for new palettes
            for palette in [DarkPalette, LightPalette]:
                process_palette(palette=palette, compile_for=self.args.create)
            _logger.info("\n")


# Based on https://sumit-ghosh.com/posts/parsing-dictionary-key-value-pairs-kwargs-argparse-python/
class CustomPaletteParser(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, dict())
        for value in values:
            key, value = value.split("=")
            getattr(namespace, self.dest)[key] = value


def import_from_file(module_name, file_path):
    """
    Taken from: https://gist.github.com/mportesdev/
    afb2ec26021ccabee0f67d6f7d18be3f
    """
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)

    return module


def main():
    """Process QRC files."""
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--base-path",
        default=PACKAGE_PATH,
        type=str,
        help="Base directory where palette assets will be generated.",
    )
    parser.add_argument(
        "--base-svg-path",
        default=SVG_PATH,
        type=str,
        help="Base path were source .svg files are located.",
    )
    parser.add_argument(
        "--palette-images",
        default=False,
        type=bool,
        help="Whether the palette preview files (`palette.svg` and "
        "`palette.png`) should be generated. They will be generated in "
        "the path provided through the `--palette-images-path` argument."
    )
    parser.add_argument(
        "--palette-images-path",
        default=IMAGES_PATH,
        type=str,
        help="Path where palette preview images (`palette.svg` and "
        "`palette.png`) will be located.",
    )
    parser.add_argument(
        "--resource-prefix",
        default="qdarkstyle",
        type=str,
        help="Prefix used for this style.",
    )
    parser.add_argument(
        "--style-prefix",
        default="qss_icons",
        type=str,
        help="Prefix used in resources.",
    )
    parser.add_argument(
        "--custom-palette-file",
        type=str,
        help="Path to a Python file with a custom Palette subclass "
        "definition. It needs to be used alongside "
        "`--custom-palette-class-name` to work.",
    )
    parser.add_argument(
        "--custom-palette-class-name",
        type=str,
        help="Importable class name from a given Python file with a custom "
        "palette subclass definition. It needs to be used alongside "
        "`--custom-palette-file` to work.",
    )
    parser.add_argument(
        "--create",
        default="qtpy",
        choices=[
            "pyqt5",
            "pyqt6",
            "pyside2",
            "pyside6",
            "qtpy",
            "pyqtgraph",
            "qt",
            "qt5",
            "all",
        ],
        type=str,
        help="Choose which one would be generated.",
    )
    parser.add_argument(
        "--watch",
        "-w",
        action="store_true",
        help="Watch for `palette.py` changes (currently only supports bundled "
             "`DarkPalette` and `LightPalette` changes)."
    )

    args = parser.parse_args()

    if args.watch:
        path = PACKAGE_PATH
        observer = Observer()
        handler = QSSFileHandler(parser_args=args)
        observer.schedule(handler, path, recursive=True)
        try:
            print("\nWatching QSS file for changes...\nPress Ctrl+C to exit\n")
            observer.start()
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
    elif args.custom_palette_file and args.custom_palette_class_name:
        custom_palette_module = import_from_file(
            "palette", args.custom_palette_file,
        )
        custom_palette_class = getattr(
            custom_palette_module, args.custom_palette_class_name,
        )
        process_palette(
            palette=custom_palette_class,
            compile_for=args.create,
            base_svg_path=args.base_svg_path,
            palette_images=args.palette_images,
            palette_images_path=args.palette_images_path,
            base_path=args.base_path,
        )
    else:
        for palette in [DarkPalette, LightPalette]:
            process_palette(
                palette=palette,
                compile_for=args.create,
                base_svg_path=args.base_svg_path,
                palette_images=args.palette_images,
                palette_images_path=args.palette_images_path,
                base_path=args.base_path,
            )


if __name__ == "__main__":
    sys.exit(main())
