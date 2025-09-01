#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Custom Themes Demo for QDarkStyleSheet

This module demonstrates how to create and use custom themes in QDarkStyleSheet.
It showcases the complete workflow from palette definition to theme generation
and application.

Key Concepts Demonstrated:
1. Custom Palette Creation - Defining color schemes with proper structure
2. Theme Asset Generation - Using qdarkstyle.utils to create QSS and icons
3. Theme Application - Loading and applying custom themes to Qt applications

The demo includes three complete theme examples:
- Ocean Theme: Blue-toned themes with cyan accents
- Forest Theme: Green themes mixing custom and built-in Gray system colors
- Sunset Theme: Warm-colored themes with red/orange/yellow palette

Each theme demonstrates different approaches to color system design:
- Pure custom hex colors (Ocean)
- Mixed custom and built-in colors (Forest)
- Custom color system with warm tones (Sunset)

Usage:
    python scripts/custom_themes_demo.py

This will generate all theme variants and launch a demo application where
you can switch between themes to see the results.

See Also:
    - qdarkstyle.palette.Palette: Base class for custom palettes
    - qdarkstyle.colorsystem: Built-in color systems (Gray, etc.)
    - qdarkstyle.utils: CLI tool for theme generation
    - docs/custom_palettes.rst: Comprehensive documentation
"""

import sys
import os
import tempfile
import shutil
import subprocess
import logging
from pathlib import Path

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

try:
    from PyQt5.QtWidgets import (
        QApplication,
        QMainWindow,
        QVBoxLayout,
        QHBoxLayout,
        QWidget,
        QPushButton,
        QLabel,
        QComboBox,
        QMessageBox,
        QStatusBar,
        QFrame,
        QGroupBox,
        QCheckBox,
        QRadioButton,
        QSlider,
        QProgressBar,
        QLineEdit,
        QTextEdit,
        QTabWidget,
        QSpinBox,
        QListWidget,
        QTreeWidget,
        QTreeWidgetItem,
        QToolButton,
    )
    from PyQt5.QtCore import Qt
    from PyQt5.QtGui import QFont
    from qdarkstyle.palette import Palette
    from qdarkstyle.colorsystem import Gray
except ImportError as e:
    print(f"❌ Required dependencies not available: {e}")
    print("Please install: PyQt5, qdarkstyle")
    sys.exit(1)


# Custom palette examples demonstrating different approaches
class OceanDarkPalette(Palette):
    """
    Ocean-inspired dark theme with blue tones.
    
    This palette demonstrates pure custom hex color definition.
    All colors are manually specified using hex values to create
    a cohesive blue-toned theme.
    
    Color Strategy:
    - Backgrounds: Deep ocean blues (#0a1a2e to #35547c)
    - Text: Light blue-tinted whites (#e6f3ff to #66c5ff)
    - Accents: Cyan family (#00d4ff to #006699)
    
    This approach gives complete control over the color scheme
    but requires careful color selection for consistency.
    """
    
    ID = "dark"  # Standard dark theme identifier

    # Background colors - deep ocean blues
    COLOR_BACKGROUND_1 = "#0a1a2e"  # Deep ocean blue
    COLOR_BACKGROUND_2 = "#16213e"  # Dark blue
    COLOR_BACKGROUND_3 = "#1e2d4f"  # Medium blue
    COLOR_BACKGROUND_4 = "#253a5e"  # Lighter blue
    COLOR_BACKGROUND_5 = "#2d476d"  # Light blue
    COLOR_BACKGROUND_6 = "#35547c"  # Lightest blue

    # Text colors - light with blue tint
    COLOR_TEXT_1 = "#e6f3ff"  # Almost white with blue tint
    COLOR_TEXT_2 = "#cce7ff"  # Light blue-white
    COLOR_TEXT_3 = "#99d6ff"  # Medium blue-white
    COLOR_TEXT_4 = "#66c5ff"  # Darker blue-white

    # Accent colors - cyan family
    COLOR_ACCENT_1 = "#00d4ff"  # Bright cyan
    COLOR_ACCENT_2 = "#00b8e6"  # Medium cyan
    COLOR_ACCENT_3 = "#009ccc"  # Darker cyan
    COLOR_ACCENT_4 = "#0080b3"  # Dark cyan
    COLOR_ACCENT_5 = "#006699"  # Very dark cyan

    COLOR_DISABLED = "#4a6b8a"
    OPACITY_TOOLTIP = 230


class OceanLightPalette(Palette):
    """
    Ocean-inspired light theme.
    
    This is the light variant of the Ocean theme, demonstrating
    how to create complementary light/dark theme pairs.
    
    Color Strategy:
    - Backgrounds: Very light blues (#f0f8ff to #bec7ff)
    - Text: Dark ocean blues (#0a1a2e to #253a5e)
    - Accents: Same cyan family as dark theme for consistency
    
    Note: Accent colors are kept identical between light and dark
    variants to maintain brand consistency across themes.
    """
    
    ID = "light"  # Standard light theme identifier

    # Light background colors
    COLOR_BACKGROUND_1 = "#f0f8ff"  # Very light blue
    COLOR_BACKGROUND_2 = "#e6f3ff"  # Light blue-white
    COLOR_BACKGROUND_3 = "#dce8ff"  # Medium light blue
    COLOR_BACKGROUND_4 = "#d2ddff"  # Light blue
    COLOR_BACKGROUND_5 = "#c8d2ff"  # Medium blue
    COLOR_BACKGROUND_6 = "#bec7ff"  # Darker blue

    # Dark text colors for light background
    COLOR_TEXT_1 = "#0a1a2e"  # Deep ocean blue
    COLOR_TEXT_2 = "#16213e"  # Dark blue
    COLOR_TEXT_3 = "#1e2d4f"  # Medium blue
    COLOR_TEXT_4 = "#253a5e"  # Lighter blue

    # Accent colors (same as dark theme for consistency)
    COLOR_ACCENT_1 = "#00d4ff"  # Bright cyan
    COLOR_ACCENT_2 = "#00b8e6"  # Medium cyan
    COLOR_ACCENT_3 = "#009ccc"  # Darker cyan
    COLOR_ACCENT_4 = "#0080b3"  # Dark cyan
    COLOR_ACCENT_5 = "#006699"  # Very dark cyan

    COLOR_DISABLED = "#4a6b8a"
    OPACITY_TOOLTIP = 230


class ForestDarkPalette(Palette):
    """
    Forest-inspired dark theme mixing custom and built-in colors.
    
    This palette demonstrates how to combine custom hex colors with
    the built-in Gray color system for consistency and maintainability.
    
    Color Strategy:
    - Backgrounds: Custom greens mixed with built-in Gray system
    - Text: Built-in Gray system for consistency (Gray.B150 to Gray.B120)
    - Accents: Custom green family (#4ade80 to #166534)
    
    Benefits of this approach:
    - Custom colors for theme identity (greens)
    - Built-in system for consistency (grays)
    - Reduced maintenance through system reuse
    """
    
    ID = "dark"  # Standard dark theme identifier

    # Custom colors
    COLOR_BACKGROUND_1 = "#1a2f1a"  # Custom dark green
    COLOR_BACKGROUND_2 = "#2d4a2d"  # Custom medium green
    COLOR_BACKGROUND_3 = "#406040"  # Custom dark olive green
    COLOR_BACKGROUND_4 = "#507050"  # Custom medium olive green
    COLOR_BACKGROUND_5 = "#608060"  # Custom muted green
    COLOR_BACKGROUND_6 = "#708070"  # Custom gray-green

    # Use built-in colors
    COLOR_TEXT_1 = Gray.B150
    COLOR_TEXT_2 = Gray.B140
    COLOR_TEXT_3 = Gray.B130
    COLOR_TEXT_4 = Gray.B120

    # Custom accent colors
    COLOR_ACCENT_1 = "#4ade80"  # Bright green
    COLOR_ACCENT_2 = "#22c55e"  # Medium green
    COLOR_ACCENT_3 = "#16a34a"  # Dark green
    COLOR_ACCENT_4 = "#15803d"  # Darker green
    COLOR_ACCENT_5 = "#166534"  # Very dark green

    COLOR_DISABLED = Gray.B70
    OPACITY_TOOLTIP = 230


class ForestLightPalette(Palette):
    """
    Forest-inspired light theme.
    
    Light variant of the Forest theme, demonstrating how to create
    light versions of mixed custom/built-in color themes.
    
    Color Strategy:
    - Backgrounds: Light greens with green tint (#f0f8f0 to #bec7be)
    - Text: Dark greens for light background (#1a2f1a to #517451)
    - Accents: Same green family as dark theme for consistency
    
    The light variant maintains the green theme identity while
    providing appropriate contrast for light backgrounds.
    """
    
    ID = "light"  # Standard light theme identifier

    # Light backgrounds with green tint
    COLOR_BACKGROUND_1 = "#f0f8f0"  # Very light green
    COLOR_BACKGROUND_2 = "#e6f3e6"  # Light green
    COLOR_BACKGROUND_3 = "#dce8dc"  # Medium light green
    COLOR_BACKGROUND_4 = "#d2ddd2"  # Light green
    COLOR_BACKGROUND_5 = "#c8d2c8"  # Medium green
    COLOR_BACKGROUND_6 = "#bec7be"  # Darker green

    # Dark text for light background
    COLOR_TEXT_1 = "#1a2f1a"  # Dark green
    COLOR_TEXT_2 = "#2d4a2d"  # Medium green
    COLOR_TEXT_3 = "#3f5f3f"  # Lighter green
    COLOR_TEXT_4 = "#517451"  # Light green

    # Same accent colors for consistency
    COLOR_ACCENT_1 = "#4ade80"
    COLOR_ACCENT_2 = "#22c55e"
    COLOR_ACCENT_3 = "#16a34a"
    COLOR_ACCENT_4 = "#15803d"
    COLOR_ACCENT_5 = "#166534"

    COLOR_DISABLED = Gray.B70
    OPACITY_TOOLTIP = 230


class SunsetDarkPalette(Palette):
    """
    Warm sunset-inspired dark theme.
    
    This palette demonstrates a custom color system approach using
    warm colors (reds, oranges, yellows) for a cohesive sunset theme.
    
    Color Strategy:
    - Backgrounds: Warm grays transitioning to reds/oranges
    - Text: Warm yellows and oranges (#FFFF99 to #ADADAD)
    - Accents: Red family with warm progression (#FF6347 to #8C8C8C)
    
    This approach shows how to create themed color systems that
    maintain visual harmony through color temperature consistency.
    """
    
    ID = "dark"  # Standard dark theme identifier

    # Warm dark backgrounds
    COLOR_BACKGROUND_1 = "#2F2F2F"  # Very dark warm gray
    COLOR_BACKGROUND_2 = "#4A4A4A"  # Dark warm gray
    COLOR_BACKGROUND_3 = "#6B6B6B"  # Medium warm gray
    COLOR_BACKGROUND_4 = "#8B0000"  # Dark red
    COLOR_BACKGROUND_5 = "#FF4500"  # Orange red
    COLOR_BACKGROUND_6 = "#FF8C00"  # Dark orange

    # Warm text colors
    COLOR_TEXT_1 = "#FFFF99"  # Light yellow
    COLOR_TEXT_2 = "#FFD700"  # Gold
    COLOR_TEXT_3 = "#FFA500"  # Orange
    COLOR_TEXT_4 = "#ADADAD"  # Very light gray

    # Warm accent colors
    COLOR_ACCENT_1 = "#FF6347"  # Tomato
    COLOR_ACCENT_2 = "#DC143C"  # Crimson
    COLOR_ACCENT_3 = "#8B0000"  # Dark red
    COLOR_ACCENT_4 = "#FF4500"  # Orange red
    COLOR_ACCENT_5 = "#8C8C8C"  # Light gray

    COLOR_DISABLED = "#6B6B6B"
    OPACITY_TOOLTIP = 230


class SunsetLightPalette(Palette):
    """
    Warm sunset-inspired light theme.
    
    Light variant of the Sunset theme, demonstrating how to adapt
    warm color systems for light backgrounds.
    
    Color Strategy:
    - Backgrounds: Very light warm tones (#fff8f0 to #ffd0be)
    - Text: Dark warm grays (#2F2F2F to #8C8C8C)
    - Accents: Same warm color family as dark theme
    
    The light variant maintains the warm sunset feeling while
    providing appropriate contrast and readability.
    """
    
    ID = "light"  # Standard light theme identifier

    # Light warm backgrounds
    COLOR_BACKGROUND_1 = "#fff8f0"  # Very light warm
    COLOR_BACKGROUND_2 = "#fff0e6"  # Light warm
    COLOR_BACKGROUND_3 = "#ffe8dc"  # Medium light warm
    COLOR_BACKGROUND_4 = "#ffe0d2"  # Light warm
    COLOR_BACKGROUND_5 = "#ffd8c8"  # Medium warm
    COLOR_BACKGROUND_6 = "#ffd0be"  # Darker warm

    # Dark text for light background
    COLOR_TEXT_1 = "#2F2F2F"  # Very dark text
    COLOR_TEXT_2 = "#4A4A4A"  # Dark text
    COLOR_TEXT_3 = "#6B6B6B"  # Medium text
    COLOR_TEXT_4 = "#8C8C8C"  # Light text

    # Same accent colors for consistency
    COLOR_ACCENT_1 = "#FF6347"
    COLOR_ACCENT_2 = "#DC143C"
    COLOR_ACCENT_3 = "#8B0000"
    COLOR_ACCENT_4 = "#FF4500"
    COLOR_ACCENT_5 = "#8C8C8C"

    COLOR_DISABLED = "#6B6B6B"
    OPACITY_TOOLTIP = 230


def create_palette_file(temp_dir, palette_class, theme_name, variant):
    """
    Create a palette file for theme generation.
    
    This function generates a Python file containing the palette class
    definition that can be used by qdarkstyle.utils for theme generation.
    
    Args:
        temp_dir (str): Temporary directory for file creation
        palette_class (class): The palette class to serialize
        theme_name (str): Name of the theme (e.g., "Ocean", "Forest")
        variant (str): Theme variant ("dark" or "light")
    
    Returns:
        str: Path to the created palette file
        
    The generated file includes:
    - Proper imports (including Gray system if used)
    - Complete palette class definition
    - All color constants and metadata
    """
    palette_file = os.path.join(temp_dir, f"{theme_name}_{variant}_palette.py")

    content = f'''# -*- coding: utf-8 -*-
"""{palette_class.__doc__}"""

from qdarkstyle.palette import Palette
'''

    # Add built-in imports if needed
    if "Gray.B" in str(palette_class.__dict__):
        content += "from qdarkstyle.colorsystem import Gray\n\n"
    else:
        content += "\n"

    content += f'''class {palette_class.__name__}(Palette):
    """{palette_class.__doc__}"""
    
    ID = '{palette_class.ID}'
    
    # Background colors
    COLOR_BACKGROUND_1 = '{palette_class.COLOR_BACKGROUND_1}'
    COLOR_BACKGROUND_2 = '{palette_class.COLOR_BACKGROUND_2}'
    COLOR_BACKGROUND_3 = '{palette_class.COLOR_BACKGROUND_3}'
    COLOR_BACKGROUND_4 = '{palette_class.COLOR_BACKGROUND_4}'
    COLOR_BACKGROUND_5 = '{palette_class.COLOR_BACKGROUND_5}'
    COLOR_BACKGROUND_6 = '{palette_class.COLOR_BACKGROUND_6}'
    
    # Text colors
    COLOR_TEXT_1 = '{palette_class.COLOR_TEXT_1}'
    COLOR_TEXT_2 = '{palette_class.COLOR_TEXT_2}'
    COLOR_TEXT_3 = '{palette_class.COLOR_TEXT_3}'
    COLOR_TEXT_4 = '{palette_class.COLOR_TEXT_4}'
    
    # Accent colors
    COLOR_ACCENT_1 = '{palette_class.COLOR_ACCENT_1}'
    COLOR_ACCENT_2 = '{palette_class.COLOR_ACCENT_2}'
    COLOR_ACCENT_3 = '{palette_class.COLOR_ACCENT_3}'
    COLOR_ACCENT_4 = '{palette_class.COLOR_ACCENT_4}'
    COLOR_ACCENT_5 = '{palette_class.COLOR_ACCENT_5}'
    
    COLOR_DISABLED = '{palette_class.COLOR_DISABLED}'
    OPACITY_TOOLTIP = {palette_class.OPACITY_TOOLTIP}
'''

    with open(palette_file, "w") as f:
        f.write(content)

    return palette_file


def generate_theme(temp_dir, palette_class, theme_name, variant):
    """
    Generate a custom theme using qdarkstyle.utils.
    
    This function orchestrates the complete theme generation process:
    1. Creates a palette file with the class definition
    2. Calls qdarkstyle.utils CLI to generate theme assets
    3. Verifies the generated QSS file exists and is valid
    
    Args:
        temp_dir (str): Base temporary directory
        palette_class (class): The palette class to generate theme from
        theme_name (str): Name of the theme (e.g., "Ocean", "Forest")
        variant (str): Theme variant ("dark" or "light")
    
    Returns:
        str or None: Path to generated QSS file, or None if generation failed
        
    Generated Assets:
    - QSS stylesheet file (darkstyle.qss or lightstyle.qss)
    - PNG icon files with custom colors (150+ files)
    - Qt resource files (.qrc and _rc.py)
    - SCSS source files for further customization
    
    The theme is generated in a subdirectory structure:
    temp_dir/theme_name_variant/dark/ or temp_dir/theme_name_variant/light/
    """
    print(f"🎨 Generating {theme_name} {variant} theme...")

    # Create theme-specific directory
    theme_dir = os.path.join(temp_dir, f"{theme_name}_{variant}")
    os.makedirs(theme_dir, exist_ok=True)

    # Create palette file
    palette_file = create_palette_file(
        temp_dir, palette_class, theme_name, variant
    )

    # Generate theme using qdarkstyle.utils CLI
    cmd = [
        "python",
        "-m",
        "qdarkstyle.utils",
        "--custom-palette-file",
        palette_file,
        "--custom-palette-class-name",
        palette_class.__name__,
        "--base-path",
        theme_dir,
    ]

    try:
        _ = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"✅ {theme_name} {variant} theme generated successfully!")

        # Check for generated QSS file
        qss_file = os.path.join(theme_dir, variant, f"{variant}style.qss")
        if os.path.exists(qss_file):
            with open(qss_file, "r") as f:
                qss_content = f.read()
            print(f"📁 QSS file: {qss_file} ({len(qss_content)} chars)")
            return qss_file
        else:
            print(f"❌ QSS file not found: {qss_file}")
            return None

    except subprocess.CalledProcessError as e:
        print(f"❌ {theme_name} {variant} theme generation failed: {e}")
        if e.stderr:
            print("STDERR:", e.stderr)
        return None


class CustomThemeDemo(QMainWindow):
    """Enhanced demo window for custom themes with comprehensive UI."""

    def __init__(self, available_themes):
        super().__init__()
        self.available_themes = available_themes
        self.current_theme = None
        self.init_ui()

    def init_ui(self):
        """Initialize the UI."""
        self.setWindowTitle("QDarkStyleSheet Custom Themes Demo")
        self.setGeometry(100, 100, 1200, 800)

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Header
        header_frame = QFrame()
        header_frame.setFrameStyle(QFrame.Box)
        header_layout = QVBoxLayout(header_frame)

        title_label = QLabel("🎨 Custom Themes Demo")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont("Arial", 16, QFont.Bold))
        header_layout.addWidget(title_label)

        info_label = QLabel(
            "Select a theme to apply it to the demo application"
        )
        info_label.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(info_label)

        main_layout.addWidget(header_frame)

        # Theme selector
        self.create_theme_selector(main_layout)

        # Demo widgets
        self.create_demo_widgets(main_layout)

        # Status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.update_status(
            f"Ready - {len(self.available_themes)} custom themes available"
        )

    def create_theme_selector(self, layout):
        """Create theme selection controls."""
        selector_frame = QFrame()
        selector_frame.setFrameStyle(QFrame.StyledPanel)
        selector_layout = QHBoxLayout(selector_frame)

        selector_layout.addWidget(QLabel("Available Themes:"))

        self.theme_combo = QComboBox()
        self.theme_combo.addItem("Default Theme")
        for theme_name in sorted(self.available_themes.keys()):
            self.theme_combo.addItem(theme_name)
        self.theme_combo.currentTextChanged.connect(self.on_theme_changed)
        selector_layout.addWidget(self.theme_combo)

        selector_layout.addStretch()

        # Info button
        info_button = QPushButton("Show Theme Info")
        info_button.clicked.connect(self.show_theme_info)
        selector_layout.addWidget(info_button)

        layout.addWidget(selector_frame)

    def create_demo_widgets(self, layout):
        """Create comprehensive demo widgets."""
        demo_frame = QFrame()
        demo_layout = QHBoxLayout(demo_frame)

        # Left panel - Basic controls
        left_panel = QGroupBox("Basic Controls")
        left_layout = QVBoxLayout(left_panel)

        # Text input
        left_layout.addWidget(QLabel("Text Input:"))
        line_edit = QLineEdit("Sample text input")
        left_layout.addWidget(line_edit)

        # Buttons
        left_layout.addWidget(QLabel("Buttons:"))
        button1 = QPushButton("Primary Button")
        button2 = QPushButton("Secondary Button")
        left_layout.addWidget(button1)
        left_layout.addWidget(button2)

        # Checkboxes and radios
        left_layout.addWidget(QLabel("Checkboxes:"))
        checkbox1 = QCheckBox("Option 1")
        checkbox2 = QCheckBox("Option 2")
        checkbox1.setChecked(True)
        left_layout.addWidget(checkbox1)
        left_layout.addWidget(checkbox2)

        left_layout.addWidget(QLabel("Radio Buttons:"))
        radio1 = QRadioButton("Choice A")
        radio2 = QRadioButton("Choice B")
        radio1.setChecked(True)
        left_layout.addWidget(radio1)
        left_layout.addWidget(radio2)

        # Slider and progress
        left_layout.addWidget(QLabel("Slider:"))
        slider = QSlider(Qt.Horizontal)
        slider.setRange(0, 100)
        slider.setValue(75)
        left_layout.addWidget(slider)

        left_layout.addWidget(QLabel("Progress Bar:"))
        progress = QProgressBar()
        progress.setValue(65)
        left_layout.addWidget(progress)

        left_layout.addStretch()
        demo_layout.addWidget(left_panel)

        # Right panel - Advanced widgets
        right_panel = QGroupBox("Advanced Widgets")
        right_layout = QVBoxLayout(right_panel)

        # Tab widget
        tab_widget = QTabWidget()

        # Tab 1 - Text
        text_tab = QWidget()
        text_layout = QVBoxLayout(text_tab)
        text_edit = QTextEdit()
        text_edit.setPlainText(
            "This is a sample text area.\n\nYou can type here to test the theme styling."
        )
        text_layout.addWidget(text_edit)
        tab_widget.addTab(text_tab, "Text Editor")

        # Tab 2 - Info
        info_tab = QWidget()
        info_layout = QVBoxLayout(info_tab)
        info_text = QLabel(
            "🎨 Custom Themes Demo\n\n"
            "This demonstrates:\n"
            "• Custom palette examples from documentation\n"
            "• Asset generation with qdarkstyle.utils CLI\n"
            "• Custom color system integration\n"
            "• PNG icon generation with custom colors\n"
            "• Complete QSS stylesheet compilation\n"
            "• Real-world UI element styling"
        )
        info_text.setWordWrap(True)
        info_layout.addWidget(info_text)
        tab_widget.addTab(info_tab, "Information")

        right_layout.addWidget(tab_widget)

        # Advanced widgets section
        right_layout.addWidget(QLabel("Advanced Widgets:"))

        # Spin box
        spin_layout = QHBoxLayout()
        spin_layout.addWidget(QLabel("Spin Box:"))
        spin_box = QSpinBox()
        spin_box.setRange(0, 100)
        spin_box.setValue(42)
        spin_layout.addWidget(spin_box)
        spin_layout.addStretch()
        right_layout.addLayout(spin_layout)

        # List widget
        right_layout.addWidget(QLabel("List Widget:"))
        list_widget = QListWidget()
        list_widget.addItems(
            ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
        )
        list_widget.setMaximumHeight(80)
        right_layout.addWidget(list_widget)

        # Tree widget
        right_layout.addWidget(QLabel("Tree Widget:"))
        tree_widget = QTreeWidget()
        tree_widget.setHeaderLabels(["Theme Components", "Status"])
        tree_widget.setMaximumHeight(100)

        # Add tree items
        root_item = QTreeWidgetItem(
            tree_widget, ["Custom Themes", "✅ Generated"]
        )
        QTreeWidgetItem(root_item, ["QSS Stylesheets", "✅ Compiled"])
        QTreeWidgetItem(root_item, ["PNG Icons", "✅ Generated"])
        QTreeWidgetItem(root_item, ["Resource Files", "✅ Created"])

        tree_widget.expandAll()
        right_layout.addWidget(tree_widget)

        # Tool buttons
        right_layout.addWidget(QLabel("Tool Buttons:"))
        tool_layout = QHBoxLayout()
        tool_button1 = QToolButton()
        tool_button1.setText("Tool 1")
        tool_button2 = QToolButton()
        tool_button2.setText("Tool 2")
        tool_layout.addWidget(tool_button1)
        tool_layout.addWidget(tool_button2)
        tool_layout.addStretch()
        right_layout.addLayout(tool_layout)

        right_layout.addStretch()
        demo_layout.addWidget(right_panel)

        layout.addWidget(demo_frame)

    def on_theme_changed(self, text):
        """Handle theme selection change."""
        if text == "Default Theme":
            QApplication.instance().setStyleSheet("")
            self.current_theme = None
            self.update_status("Applied default theme")
            return

        if text in self.available_themes:
            self.apply_theme(text)

    def apply_theme(self, theme_name):
        """Apply selected theme."""
        qss_file = self.available_themes[theme_name]

        try:
            # Get theme directory for resource imports
            theme_dir = os.path.dirname(qss_file)
            base_dir = os.path.dirname(theme_dir)

            # Add to Python path for resource imports
            if base_dir not in sys.path:
                sys.path.insert(0, base_dir)

            # Import resource module for icons
            variant = "dark" if "dark" in qss_file else "light"
            resource_module = f"{variant}.{variant}style_rc"
            if resource_module in sys.modules:
                del sys.modules[resource_module]

            try:
                __import__(resource_module)
                print(f"✅ Loaded resource module: {resource_module}")
            except ImportError as e:
                print(f"⚠️ Could not load resource module: {e}")

            # Load and apply stylesheet
            with open(qss_file, "r") as f:
                stylesheet = f.read()

            QApplication.instance().setStyleSheet(stylesheet)
            self.current_theme = theme_name
            self.update_status(f"Applied {theme_name} theme")

            print(
                f"🎨 Applied {theme_name} theme - QSS length: {len(stylesheet)} chars"
            )

        except Exception as e:
            QMessageBox.warning(
                self,
                "Theme Error",
                f"Failed to apply {theme_name} theme:\n{e}",
            )
            print(f"❌ Theme application failed: {e}")

    def update_status(self, message):
        """Update status bar."""
        self.status_bar.showMessage(message)

    def show_theme_info(self):
        """Show detailed color information for the current theme."""
        if not self.current_theme:
            QMessageBox.information(
                self,
                "Theme Info",
                "No theme currently applied. Please select a theme first.",
            )
            return

        # Get the palette class for the current theme
        theme_palettes = {
            "Ocean Dark": OceanDarkPalette,
            "Ocean Light": OceanLightPalette,
            "Forest Dark": ForestDarkPalette,
            "Forest Light": ForestLightPalette,
            "Sunset Dark": SunsetDarkPalette,
            "Sunset Light": SunsetLightPalette,
        }

        if self.current_theme not in theme_palettes:
            QMessageBox.warning(
                self, "Theme Error", f"Unknown theme: {self.current_theme}"
            )
            return

        palette_class = theme_palettes[self.current_theme]

        # Create detailed color table
        info_text = f"""🎨 {self.current_theme} Theme - Color Palette

Background Colors:
• COLOR_BACKGROUND_1: {palette_class.COLOR_BACKGROUND_1} (Primary background)
• COLOR_BACKGROUND_2: {palette_class.COLOR_BACKGROUND_2} (Secondary background)
• COLOR_BACKGROUND_3: {palette_class.COLOR_BACKGROUND_3} (Tertiary background)
• COLOR_BACKGROUND_4: {palette_class.COLOR_BACKGROUND_4} (Raised elements)
• COLOR_BACKGROUND_5: {palette_class.COLOR_BACKGROUND_5} (Pressed elements)
• COLOR_BACKGROUND_6: {palette_class.COLOR_BACKGROUND_6} (Hover elements)

Text Colors:
• COLOR_TEXT_1: {palette_class.COLOR_TEXT_1} (Primary text)
• COLOR_TEXT_2: {palette_class.COLOR_TEXT_2} (Secondary text)
• COLOR_TEXT_3: {palette_class.COLOR_TEXT_3} (Tertiary text)
• COLOR_TEXT_4: {palette_class.COLOR_TEXT_4} (Quaternary text)

Accent Colors:
• COLOR_ACCENT_1: {palette_class.COLOR_ACCENT_1} (Primary accent)
• COLOR_ACCENT_2: {palette_class.COLOR_ACCENT_2} (Secondary accent)
• COLOR_ACCENT_3: {palette_class.COLOR_ACCENT_3} (Tertiary accent)
• COLOR_ACCENT_4: {palette_class.COLOR_ACCENT_4} (Quaternary accent)
• COLOR_ACCENT_5: {palette_class.COLOR_ACCENT_5} (Quinary accent)

Other Colors:
• COLOR_DISABLED: {palette_class.COLOR_DISABLED} (Disabled elements)
• OPACITY_TOOLTIP: {palette_class.OPACITY_TOOLTIP} (Tooltip opacity)

Theme ID: {palette_class.ID}
Description: {palette_class.__doc__}"""

        QMessageBox.information(
            self, f"{self.current_theme} Theme Colors", info_text
        )


def main():
    """
    Main demo function.
    
    This function orchestrates the complete custom themes demo:
    1. Creates a temporary directory for theme generation
    2. Generates all theme variants (6 total: 3 themes × 2 variants)
    3. Launches a Qt demo application with theme switching
    4. Cleans up temporary files on exit
    
    Theme Generation Process:
    - Ocean Theme: Blue tones with cyan accents (Dark & Light)
    - Forest Theme: Green with Gray system integration (Dark & Light)
    - Sunset Theme: Warm colors with red/orange palette (Dark & Light)
    
    Each theme demonstrates different color system approaches:
    - Pure custom hex colors (Ocean)
    - Mixed custom and built-in colors (Forest)
    - Custom warm color system (Sunset)
    
    The demo application allows real-time theme switching to
    compare different approaches and see the results.
    
    Returns:
        int: Exit code (0 for success, 1 for failure)
    """
    print("🎨 QDarkStyleSheet Custom Themes Demo")
    print("=" * 50)

    # Create temporary directory
    temp_dir = tempfile.mkdtemp(prefix="custom_themes_demo_")
    print(f"Using temporary directory: {temp_dir}")

    try:
        # Generate themes
        available_themes = {}

        # Generate Ocean themes
        ocean_dark_qss = generate_theme(
            temp_dir, OceanDarkPalette, "Ocean", "dark"
        )
        if ocean_dark_qss:
            available_themes["Ocean Dark"] = ocean_dark_qss

        ocean_light_qss = generate_theme(
            temp_dir, OceanLightPalette, "Ocean", "light"
        )
        if ocean_light_qss:
            available_themes["Ocean Light"] = ocean_light_qss

        # Generate Forest themes
        forest_dark_qss = generate_theme(
            temp_dir, ForestDarkPalette, "Forest", "dark"
        )
        if forest_dark_qss:
            available_themes["Forest Dark"] = forest_dark_qss

        forest_light_qss = generate_theme(
            temp_dir, ForestLightPalette, "Forest", "light"
        )
        if forest_light_qss:
            available_themes["Forest Light"] = forest_light_qss

        # Generate Sunset themes
        sunset_dark_qss = generate_theme(
            temp_dir, SunsetDarkPalette, "Sunset", "dark"
        )
        if sunset_dark_qss:
            available_themes["Sunset Dark"] = sunset_dark_qss

        sunset_light_qss = generate_theme(
            temp_dir, SunsetLightPalette, "Sunset", "light"
        )
        if sunset_light_qss:
            available_themes["Sunset Light"] = sunset_light_qss

        if not available_themes:
            print("❌ No themes could be generated. Exiting.")
            return 1

        print(f"\n✅ Successfully generated {len(available_themes)} themes:")
        for theme_name in available_themes:
            print(f"   • {theme_name}")

        # Create Qt application
        app = QApplication(sys.argv)
        app.setOrganizationName("QDarkStyleDemo")
        app.setApplicationName("Custom Themes Demo")

        # Create and show demo window
        demo_window = CustomThemeDemo(available_themes)
        demo_window.show()

        print("\n🚀 Demo application started!")

        # Run the application
        return app.exec_()

    except Exception as e:
        print(f"❌ Demo failed: {e}")
        import traceback

        traceback.print_exc()
        return 1

    finally:
        # Cleanup
        print(f"\n🧹 Cleaning up: {temp_dir}")
        shutil.rmtree(temp_dir, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
