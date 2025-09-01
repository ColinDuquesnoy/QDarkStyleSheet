Custom Palettes Guide
=====================

This guide explains how to create and use custom palettes with QDarkStyleSheet. Custom palettes allow you to define completely custom color schemes while following the established dark/light theme pattern.


Understanding Custom Palettes
-----------------------------

QDarkStyleSheet supports custom palettes that follow the same pattern as built-in themes:

- **Standard IDs**: Custom palettes use 'dark' and/or 'light' IDs (same as built-in themes)
- **Custom colors**: Complete freedom to define all colors within your palette
- **Custom color system**: Can use built-in colors or define your own
- **Generated resources**: The qdarkstyle.utils module generates all necessary files (QSS, QRC, PNG icons)
- **Theme variants**: Custom themes typically provide both dark and light variants

.. note::
   **Important**: Custom palettes with standard 'dark' and 'light' IDs **CAN** be used with ``qdarkstyle.load_stylesheet()``, 
   just like the built-in ``DarkPalette`` and ``LightPalette`` classes.
   
   Custom palettes with other IDs (like 'my_theme') cannot be used with ``load_stylesheet()`` and must be loaded directly from QSS files.
   This design maintains consistency with the dark/light theme architecture.


Creating a Custom Palette
-------------------------

Basic Structure
~~~~~~~~~~~~~~~

All custom palettes must inherit from the ``Palette`` class and use standard IDs:

.. code-block:: python

    from qdarkstyle.palette import Palette

    class DarkOceanPalette(Palette):
        """Ocean-inspired dark theme."""
        
        # Standard dark theme ID
        ID = 'dark'
        
        # Background colors (customize as needed)
        COLOR_BACKGROUND_1 = '#0a1a2e'  # Deep ocean blue
        COLOR_BACKGROUND_2 = '#16213e'  # Dark blue
        COLOR_BACKGROUND_3 = '#1e2d4f'  # Medium blue
        COLOR_BACKGROUND_4 = '#253a5e'  # Lighter blue
        COLOR_BACKGROUND_5 = '#2d476d'  # Light blue
        COLOR_BACKGROUND_6 = '#35547c'  # Lightest blue
        
        # Text colors
        COLOR_TEXT_1 = '#e6f3ff'       # Almost white with blue tint
        COLOR_TEXT_2 = '#cce7ff'       # Light blue-white
        COLOR_TEXT_3 = '#99d6ff'       # Medium blue-white
        COLOR_TEXT_4 = '#66c5ff'       # Darker blue-white
        
        # Accent colors (for interactive elements)
        COLOR_ACCENT_1 = '#00d4ff'     # Bright cyan
        COLOR_ACCENT_2 = '#00b8e6'     # Medium cyan
        COLOR_ACCENT_3 = '#009ccc'     # Darker cyan
        COLOR_ACCENT_4 = '#0080b3'     # Dark cyan
        COLOR_ACCENT_5 = '#006699'     # Very dark cyan
        
        COLOR_DISABLED = '#4a6b8a'
        OPACITY_TOOLTIP = 230

    class LightOceanPalette(Palette):
        """Ocean-inspired light theme."""
        
        # Standard light theme ID
        ID = 'light'
        
        # Light background colors
        COLOR_BACKGROUND_1 = '#f0f8ff'  # Very light blue
        COLOR_BACKGROUND_2 = '#e6f3ff'  # Light blue-white
        COLOR_BACKGROUND_3 = '#dce8ff'  # Medium light blue
        COLOR_BACKGROUND_4 = '#d2ddff'  # Light blue
        COLOR_BACKGROUND_5 = '#c8d2ff'  # Medium blue
        COLOR_BACKGROUND_6 = '#bec7ff'  # Darker blue
        
        # Dark text colors for light background
        COLOR_TEXT_1 = '#0a1a2e'       # Deep ocean blue
        COLOR_TEXT_2 = '#16213e'       # Dark blue
        COLOR_TEXT_3 = '#1e2d4f'       # Medium blue
        COLOR_TEXT_4 = '#253a5e'       # Lighter blue
        
        # Accent colors (same as dark theme for consistency)
        COLOR_ACCENT_1 = '#00d4ff'     # Bright cyan
        COLOR_ACCENT_2 = '#00b8e6'     # Medium cyan
        COLOR_ACCENT_3 = '#009ccc'     # Darker cyan
        COLOR_ACCENT_4 = '#0080b3'     # Dark cyan
        COLOR_ACCENT_5 = '#006699'     # Very dark cyan
        
        COLOR_DISABLED = '#4a6b8a'
        OPACITY_TOOLTIP = 230

Required Properties
~~~~~~~~~~~~~~~~~~~

Every custom palette must define these properties:

- **ID**: **MUST** be either 'dark' or 'light' (standard theme IDs)
  - Use 'dark' for dark-themed palettes
  - Use 'light' for light-themed palettes
  - Custom IDs (like 'my_theme') are not supported by load_stylesheet()
- **Background Colors**: Six levels (COLOR_BACKGROUND_1 to COLOR_BACKGROUND_6)
- **Text Colors**: Four levels (COLOR_TEXT_1 to COLOR_TEXT_4)
- **Accent Colors**: Five levels (COLOR_ACCENT_1 to COLOR_ACCENT_5)
- **Disabled Color**: COLOR_DISABLED for disabled elements
- **Tooltip Opacity**: OPACITY_TOOLTIP (0-255)

.. note::
   Custom themes typically provide both dark and light variants for consistency.
   You can create just one variant if needed, but providing both gives users
   the flexibility to switch between themes.

Using Custom Color Systems
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Option 1: Using Built-in Color Systems**

You can mix custom hex colors with the built-in color systems:

.. code-block:: python

    from qdarkstyle.palette import Palette
    from qdarkstyle.colorsystem import Gray, Blue

    class DarkForestPalette(Palette):
        """Forest-inspired dark theme with custom and built-in colors."""
        
        ID = 'dark'
        
        # Mix custom colors with color system
        COLOR_BACKGROUND_1 = '#1a2f1a'      # Custom dark green
        COLOR_BACKGROUND_2 = '#2d4a2d'      # Custom medium green
        COLOR_BACKGROUND_3 = Gray.B30        # Built-in gray
        COLOR_BACKGROUND_4 = Gray.B40        # Built-in gray
        COLOR_BACKGROUND_5 = Gray.B50        # Built-in gray
        COLOR_BACKGROUND_6 = Gray.B60        # Built-in gray
        
        # Use built-in colors for consistency
        COLOR_TEXT_1 = Gray.B150
        COLOR_TEXT_2 = Gray.B140
        COLOR_TEXT_3 = Gray.B130
        COLOR_TEXT_4 = Gray.B120
        
        # Custom accent colors
        COLOR_ACCENT_1 = '#4ade80'
        COLOR_ACCENT_2 = '#22c55e'
        COLOR_ACCENT_3 = '#16a34a'
        COLOR_ACCENT_4 = '#15803d'
        COLOR_ACCENT_5 = '#166534'
        
        COLOR_DISABLED = Gray.B70
        OPACITY_TOOLTIP = 230

    class LightForestPalette(Palette):
        """Forest-inspired light theme."""
        
        ID = 'light'
        
        # Light backgrounds with green tint
        COLOR_BACKGROUND_1 = '#f0f8f0'      # Very light green
        COLOR_BACKGROUND_2 = '#e6f3e6'      # Light green
        COLOR_BACKGROUND_3 = '#dce8dc'      # Medium light green
        COLOR_BACKGROUND_4 = '#d2ddd2'      # Light green
        COLOR_BACKGROUND_5 = '#c8d2c8'      # Medium green
        COLOR_BACKGROUND_6 = '#bec7be'      # Darker green
        
        # Dark text for light background
        COLOR_TEXT_1 = '#1a2f1a'            # Dark green
        COLOR_TEXT_2 = '#2d4a2d'            # Medium green
        COLOR_TEXT_3 = '#3f5f3f'            # Lighter green
        COLOR_TEXT_4 = '#517451'            # Light green
        
        # Same accent colors for consistency
        COLOR_ACCENT_1 = '#4ade80'
        COLOR_ACCENT_2 = '#22c55e'
        COLOR_ACCENT_3 = '#16a34a'
        COLOR_ACCENT_4 = '#15803d'
        COLOR_ACCENT_5 = '#166534'
        
        COLOR_DISABLED = Gray.B70
        OPACITY_TOOLTIP = 230

**Option 2: Creating Fully Custom Color Systems**

For complete control over all colors, you can create your own color system classes:

.. code-block:: python

    # custom_colors.py - Define your own color system
    class WarmColors:
        """Warm color palette system."""
        # Reds and oranges
        RED_DARK = '#8B0000'      # Dark red
        RED_MEDIUM = '#DC143C'    # Crimson
        RED_LIGHT = '#FF6347'     # Tomato
        
        ORANGE_DARK = '#FF4500'   # Orange red
        ORANGE_MEDIUM = '#FF8C00' # Dark orange
        ORANGE_LIGHT = '#FFA500'  # Orange
        
        # Yellows and warm neutrals
        YELLOW_DARK = '#DAA520'   # Goldenrod
        YELLOW_MEDIUM = '#FFD700' # Gold
        YELLOW_LIGHT = '#FFFF99' # Light yellow
        
        WARM_GRAY_1 = '#2F2F2F'   # Very dark gray
        WARM_GRAY_2 = '#4A4A4A'   # Dark gray
        WARM_GRAY_3 = '#6B6B6B'   # Medium gray
        WARM_GRAY_4 = '#8C8C8C'   # Light gray
        WARM_GRAY_5 = '#ADADAD'   # Very light gray
        
    class CoolColors:
        """Cool color palette system."""
        # Blues and greens
        BLUE_DARK = '#191970'     # Midnight blue
        BLUE_MEDIUM = '#4169E1'   # Royal blue
        BLUE_LIGHT = '#87CEEB'    # Sky blue
        
        GREEN_DARK = '#006400'    # Dark green
        GREEN_MEDIUM = '#228B22'  # Forest green
        GREEN_LIGHT = '#90EE90'   # Light green
        
        # Purples and cool neutrals
        PURPLE_DARK = '#4B0082'   # Indigo
        PURPLE_MEDIUM = '#8A2BE2' # Blue violet
        PURPLE_LIGHT = '#DDA0DD'  # Plum
        
        COOL_GRAY_1 = '#2E3440'   # Dark cool gray
        COOL_GRAY_2 = '#3B4252'   # Medium dark gray
        COOL_GRAY_3 = '#434C5E'   # Medium gray
        COOL_GRAY_4 = '#4C566A'   # Light gray
        COOL_GRAY_5 = '#5E81AC'   # Very light gray

Now use your custom color systems in your palettes:

.. code-block:: python

    from qdarkstyle.palette import Palette
    from custom_colors import WarmColors, CoolColors

    class DarkSunsetPalette(Palette):
        """Warm sunset-inspired dark theme using custom color system."""
        
        ID = 'dark'
        
        # Use your custom warm colors
        COLOR_BACKGROUND_1 = WarmColors.WARM_GRAY_1    # Very dark background
        COLOR_BACKGROUND_2 = WarmColors.WARM_GRAY_2    # Dark background
        COLOR_BACKGROUND_3 = WarmColors.WARM_GRAY_3    # Medium background
        COLOR_BACKGROUND_4 = WarmColors.RED_DARK       # Dark red for raised elements
        COLOR_BACKGROUND_5 = WarmColors.ORANGE_DARK    # Orange for pressed elements
        COLOR_BACKGROUND_6 = WarmColors.ORANGE_MEDIUM  # Bright orange for hover
        
        # Warm text colors
        COLOR_TEXT_1 = WarmColors.YELLOW_LIGHT         # Primary text
        COLOR_TEXT_2 = WarmColors.YELLOW_MEDIUM        # Secondary text
        COLOR_TEXT_3 = WarmColors.ORANGE_LIGHT         # Tertiary text
        COLOR_TEXT_4 = WarmColors.WARM_GRAY_5          # Quaternary text
        
        # Warm accent colors
        COLOR_ACCENT_1 = WarmColors.RED_LIGHT          # Bright accent
        COLOR_ACCENT_2 = WarmColors.RED_MEDIUM         # Medium accent
        COLOR_ACCENT_3 = WarmColors.RED_DARK           # Dark accent
        COLOR_ACCENT_4 = WarmColors.ORANGE_DARK        # Darker accent
        COLOR_ACCENT_5 = WarmColors.WARM_GRAY_4        # Subtle accent
        
        COLOR_DISABLED = WarmColors.WARM_GRAY_3
        OPACITY_TOOLTIP = 230

    class LightSunsetPalette(Palette):
        """Warm sunset-inspired light theme using custom color system."""
        
        ID = 'light'
        
        # Light warm backgrounds
        COLOR_BACKGROUND_1 = '#fff8f0'                 # Very light warm
        COLOR_BACKGROUND_2 = '#fff0e6'                 # Light warm
        COLOR_BACKGROUND_3 = '#ffe8dc'                 # Medium light warm
        COLOR_BACKGROUND_4 = '#ffe0d2'                 # Light warm
        COLOR_BACKGROUND_5 = '#ffd8c8'                 # Medium warm
        COLOR_BACKGROUND_6 = '#ffd0be'                 # Darker warm
        
        # Dark text for light background
        COLOR_TEXT_1 = WarmColors.WARM_GRAY_1          # Very dark text
        COLOR_TEXT_2 = WarmColors.WARM_GRAY_2          # Dark text
        COLOR_TEXT_3 = WarmColors.WARM_GRAY_3          # Medium text
        COLOR_TEXT_4 = WarmColors.WARM_GRAY_4          # Light text
        
        # Same accent colors for consistency
        COLOR_ACCENT_1 = WarmColors.RED_LIGHT
        COLOR_ACCENT_2 = WarmColors.RED_MEDIUM
        COLOR_ACCENT_3 = WarmColors.RED_DARK
        COLOR_ACCENT_4 = WarmColors.ORANGE_DARK
        COLOR_ACCENT_5 = WarmColors.WARM_GRAY_4
        
        COLOR_DISABLED = WarmColors.WARM_GRAY_3
        OPACITY_TOOLTIP = 230

**Why Use Custom Color Systems?**

- **Consistency**: Ensures all colors work harmoniously together
- **Maintainability**: Easy to update color schemes across multiple themes
- **Design System**: Creates a cohesive color language for your application
- **Flexibility**: Mix and match color systems for different themes

Complete Workflow
-----------------

1. Create Your Palette File
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a Python file with your custom palettes:

.. code-block:: python

    # my_theme.py
    from qdarkstyle.palette import Palette

    class DarkNeonPalette(Palette):
        """Cyberpunk neon dark theme."""
        
        ID = 'dark'
        
        # Dark backgrounds with neon accents
        COLOR_BACKGROUND_1 = '#0d0d0d'  # Almost black
        COLOR_BACKGROUND_2 = '#1a1a1a'  # Very dark gray
        COLOR_BACKGROUND_3 = '#262626'  # Dark gray
        COLOR_BACKGROUND_4 = '#333333'  # Medium gray
        COLOR_BACKGROUND_5 = '#404040'  # Light gray
        COLOR_BACKGROUND_6 = '#4d4d4d'  # Lighter gray
        
        # Bright text colors
        COLOR_TEXT_1 = '#ffffff'        # Pure white
        COLOR_TEXT_2 = '#e6e6e6'        # Light gray
        COLOR_TEXT_3 = '#cccccc'        # Medium gray
        COLOR_TEXT_4 = '#b3b3b3'        # Darker gray
        
        # Neon accent colors
        COLOR_ACCENT_1 = '#ff0080'      # Hot pink
        COLOR_ACCENT_2 = '#e6006b'      # Dark pink
        COLOR_ACCENT_3 = '#cc0066'      # Darker pink
        COLOR_ACCENT_4 = '#b30055'      # Very dark pink
        COLOR_ACCENT_5 = '#990044'      # Almost black pink
        
        COLOR_DISABLED = '#666666'
        OPACITY_TOOLTIP = 230

    class LightNeonPalette(Palette):
        """Cyberpunk neon light theme."""
        
        ID = 'light'
        
        # Light backgrounds with neon accents
        COLOR_BACKGROUND_1 = '#ffffff'  # Pure white
        COLOR_BACKGROUND_2 = '#f8f8f8'  # Very light gray
        COLOR_BACKGROUND_3 = '#f0f0f0'  # Light gray
        COLOR_BACKGROUND_4 = '#e8e8e8'  # Medium light gray
        COLOR_BACKGROUND_5 = '#e0e0e0'  # Medium gray
        COLOR_BACKGROUND_6 = '#d8d8d8'  # Darker gray
        
        # Dark text colors for light background
        COLOR_TEXT_1 = '#0d0d0d'        # Almost black
        COLOR_TEXT_2 = '#1a1a1a'        # Very dark gray
        COLOR_TEXT_3 = '#262626'        # Dark gray
        COLOR_TEXT_4 = '#333333'        # Medium gray
        
        # Same neon accent colors for consistency
        COLOR_ACCENT_1 = '#ff0080'      # Hot pink
        COLOR_ACCENT_2 = '#e6006b'      # Dark pink
        COLOR_ACCENT_3 = '#cc0066'      # Darker pink
        COLOR_ACCENT_4 = '#b30055'      # Very dark pink
        COLOR_ACCENT_5 = '#990044'      # Almost black pink
        
        COLOR_DISABLED = '#666666'
        OPACITY_TOOLTIP = 230

2. Generate Theme Resources
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::
   **CRITICAL REQUIREMENT**: You MUST generate theme resources before using any custom palette. This process creates the necessary QSS stylesheets, PNG icons, and resource files with your custom colors. Custom palettes cannot be used without this step.

.. warning::
   **Asset Generation Required for Custom Color Systems**: When using custom color systems (like the WarmColors/CoolColors example above), the asset generation process will create PNG icons using your custom colors. This ensures that UI elements like checkboxes, arrows, and other icons match your color scheme.

Use the qdarkstyle.utils module to generate all necessary files:

.. code-block:: bash

    # Generate dark theme resources
    python -m qdarkstyle.utils \
        --custom-palette-file my_theme.py \
        --custom-palette-class-name DarkNeonPalette \
        --base-path ./my_neon_theme

    # Generate light theme resources
    python -m qdarkstyle.utils \
        --custom-palette-file my_theme.py \
        --custom-palette-class-name LightNeonPalette \
        --base-path ./my_neon_theme

.. note::
   The command-line interface is provided by the ``qdarkstyle.utils`` module. This is the same tool used internally by QDarkStyleSheet for generating built-in themes.

**Available CLI Options:**

- ``--custom-palette-file``: Path to your Python file containing the palette class
- ``--custom-palette-class-name``: Name of your palette class (must match exactly)
- ``--base-path``: Directory where theme assets will be generated (default: package directory)
- ``--create``: Qt binding to compile for (default: qtpy, options: pyqt5, pyqt6, pyside2, pyside6, all)
- ``--palette-images``: Generate preview palette images (default: False)
- ``--palette-images-path``: Path for preview images (default: docs/images)
- ``--resource-prefix``: Resource prefix for icons (default: qss_icons)
- ``--style-prefix``: Style prefix for QSS files (default: qdarkstyle)

This creates the complete theme structure:

.. code-block:: text

    my_neon_theme/
    ├── dark/                      # Dark theme resources
    │   ├── darkstyle.qss         # Generated dark stylesheet
    │   ├── darkstyle.qrc         # Qt resource file
    │   ├── darkstyle_rc.py       # Python resource module
    │   ├── palette.py            # Your dark palette class
    │   ├── main.scss             # SCSS source
    │   ├── _variables.scss       # SCSS variables
    │   └── rc/                   # Generated PNG icons (150+ files)
    │       ├── arrow_down.png
    │       ├── checkbox_checked.png
    │       └── ... (all icons in your colors)
    └── light/                     # Light theme resources
        ├── lightstyle.qss        # Generated light stylesheet
        ├── lightstyle.qrc        # Qt resource file
        ├── lightstyle_rc.py      # Python resource module
        ├── palette.py            # Your light palette class
        ├── main.scss             # SCSS source
        ├── _variables.scss       # SCSS variables
        └── rc/                   # Generated PNG icons (150+ files)
            ├── arrow_down.png
            ├── checkbox_checked.png
            └── ... (all icons in your colors)

**What Happens During Asset Generation?**

The asset generation process does several critical things:

1. **Creates Colored Icons**: Takes the base SVG icons and generates PNG versions using your palette's colors
   
   - ``COLOR_ACCENT_2`` is used for pressed states
   - ``COLOR_ACCENT_5`` is used for focus states  
   - ``COLOR_BACKGROUND_4`` is used for disabled states
   - ``COLOR_TEXT_1`` is used for normal states

2. **Generates QSS Stylesheet**: Compiles SCSS variables with your colors into a complete QSS stylesheet

3. **Creates Resource Files**: Generates Qt resource files (.qrc) and Python resource modules (_rc.py) that bundle all assets

4. **Ensures Color Consistency**: All UI elements (backgrounds, text, icons, borders) use colors from your palette

**Without asset generation, your custom theme will not work** because:

- Icons will not match your color scheme
- Many UI elements depend on the generated PNG resources
- The QSS file contains references to generated resources

3. Use Your Custom Theme
~~~~~~~~~~~~~~~~~~~~~~~~

Custom themes with standard 'dark'/'light' IDs **CAN** be used with ``qdarkstyle.load_stylesheet()``. For other IDs, use one of these methods:

**Method 1: Use load_stylesheet() (Recommended for 'dark'/'light' IDs)**

.. code-block:: python

    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow
    import qdarkstyle

    app = QApplication(sys.argv)
    
    # Import your custom palettes
    from my_theme import DarkNeonPalette, LightNeonPalette
    
    # Use with load_stylesheet() - works because IDs are 'dark'/'light'
    app.setStyleSheet(qdarkstyle.load_stylesheet(palette=DarkNeonPalette))
    # or
    # app.setStyleSheet(qdarkstyle.load_stylesheet(palette=LightNeonPalette))
    
    window = QMainWindow()
    window.setWindowTitle("Neon Dark Theme")
    window.show()
    
    app.exec_()

**Method 2: Load QSS file directly (for custom IDs or direct file access)**

.. code-block:: python

    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow

    app = QApplication(sys.argv)
    
    # Load your custom dark stylesheet directly
    with open('./my_neon_theme/dark/darkstyle.qss', 'r') as f:
        stylesheet = f.read()
    
    app.setStyleSheet(stylesheet)
    
    window = QMainWindow()
    window.setWindowTitle("Neon Dark Theme")
    window.show()
    
    app.exec_()

    # Or load light theme
    # with open('./my_neon_theme/light/lightstyle.qss', 'r') as f:
    #     stylesheet = f.read()

**Method 3: Import generated resources**

There are two recommended approaches for importing custom theme resources:

**Option A: Local theme module (for single applications)**

Place your generated themes in a theme package within your application:

.. code-block:: text

    your_app/
    ├── main.py
    └── my_neon_theme/              # Theme package
        ├── __init__.py
        ├── dark/                   # Dark theme
        │   ├── darkstyle.qss
        │   ├── darkstyle_rc.py
        │   └── ...
        └── light/                  # Light theme
            ├── lightstyle.qss
            ├── lightstyle_rc.py
            └── ...

.. code-block:: python

    from PyQt5.QtWidgets import QApplication, QMainWindow
    from PyQt5.QtCore import QFile, QTextStream

    # Import the generated dark theme resources
    import my_neon_theme.dark.darkstyle_rc  # This loads the resources
    
    app = QApplication(sys.argv)
    
    # Load dark stylesheet from resources
    qss_file = QFile(":/qss_icons/dark/darkstyle.qss")
    qss_file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(qss_file)
    stylesheet = stream.readAll()
    
    app.setStyleSheet(stylesheet)
    
    window = QMainWindow()
    window.setWindowTitle("Neon Dark Theme with Resources")
    window.show()
    
    app.exec_()

    # Or load light theme
    # import my_neon_theme.light.lightstyle_rc
    # qss_file = QFile(":/qss_icons/light/lightstyle.qss")

**Option B: Proper Python package (for reusable themes)**

Create a proper Python package structure for your themes:

.. code-block:: text

    my_neon_theme/
    ├── setup.py
    ├── my_neon_theme/
    │   ├── __init__.py
    │   ├── dark/
    │   │   ├── darkstyle.qss
    │   │   ├── darkstyle_rc.py
    │   │   └── ...
    │   └── light/
    │       ├── lightstyle.qss
    │       ├── lightstyle_rc.py
    │       └── ...
    └── ...

.. code-block:: python

    from PyQt5.QtWidgets import QApplication, QMainWindow
    from PyQt5.QtCore import QFile, QTextStream

    # Import the generated dark theme resources from installed package
    import my_neon_theme.dark.darkstyle_rc  # This loads the resources
    
    app = QApplication(sys.argv)
    
    # Load dark stylesheet from resources
    qss_file = QFile(":/qss_icons/dark/darkstyle.qss")
    qss_file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(qss_file)
    stylesheet = stream.readAll()
    
    app.setStyleSheet(stylesheet)
    
    window = QMainWindow()
    window.setWindowTitle("Neon Dark Theme with Resources")
    window.show()
    
    app.exec_()

    # Or load light theme
    # import my_neon_theme.light.lightstyle_rc
    # qss_file = QFile(":/qss_icons/light/lightstyle.qss")

.. note::
   **Theme Consistency**: By using standard 'dark' and 'light' IDs, your custom themes follow the same pattern as built-in themes, making them more intuitive and fully compatible with the current QDarkStyleSheet API.


Color Selection Guidelines
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Background Hierarchy**: Use COLOR_BACKGROUND_1 for main areas, higher numbers for elevated surfaces
2. **Text Contrast**: Ensure sufficient contrast between text and background colors
3. **Accent Consistency**: Use COLOR_ACCENT_3 as primary selection color
4. **Accessibility**: Test with color vision deficiency simulators
5. **System Colors**: Consider using built-in color constants for consistency

Theme Development Workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Design Phase**: Plan your color scheme with design tools
2. **Prototype**: Create palette class and generate initial theme
3. **Test**: Use the test application to verify all widgets
4. **Iterate**: Refine colors based on visual testing
5. **Validate**: Check accessibility and usability

File Management
~~~~~~~~~~~~~~~

1. **Organization**: Keep themes in separate directories
2. **Version Control**: Track palette files and generated resources
3. **Documentation**: Document color choices and theme purpose
4. **Backup**: Maintain copies of working themes

Important Notes
----------------

Limitations and Considerations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**load_stylesheet() support**: Custom palettes with standard 'dark' and 'light' IDs **CAN** be used with ``qdarkstyle.load_stylesheet()``, just like the built-in DarkPalette and LightPalette classes. Custom palettes with other IDs (like 'my_theme') cannot be used with ``load_stylesheet()`` and must be loaded directly from QSS files.

**Resource Management**: Generated themes include resource files that must be properly imported if using Method 2.

**Path Management**: Ensure proper path handling when loading QSS files in different environments.

**Qt Binding Compatibility**: Generated resource files work with all Qt bindings (PyQt5, PyQt6, PySide2, PySide6).

**Theme Architecture**: Custom themes follow the same dark/light pattern as built-in themes, providing consistency and potential future compatibility.

Technical Details
~~~~~~~~~~~~~~~~~

**How load_stylesheet() works with custom palettes**: The function validates palette IDs and accepts 'dark' or 'light'. For these IDs, it imports the correct resource modules (darkstyle_rc or lightstyle_rc) that contain the compiled QSS and icon resources. Custom palettes with 'dark'/'light' IDs work because they generate their own resource files with the same structure. Custom palettes with other IDs don't work because the function doesn't know how to locate their resources.

**Future Compatibility**: By using standard 'dark' and 'light' IDs, custom themes follow the same architecture as built-in themes. This design choice makes it easier to potentially integrate custom themes with the main API in future versions while maintaining backward compatibility.

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Theme not loading**: Verify the QSS file path is correct and accessible.

**Icons not showing**: Ensure resource files are properly imported (Method 2) or use Method 1.

**Colors not applied**: Check that all required palette properties are defined.

**CLI generation fails**: Verify qtsass and watchdog are installed, and palette class is properly defined.

**Performance issues**: Large themes may take time to load; consider caching stylesheets.

Resources
---------

- **CLI Reference**: See :doc:`scripts/qdarkstyle_utils` for complete command-line options
- **Color System**: See :doc:`color_reference` for built-in colors
- **API Reference**: See :doc:`reference/modules` for palette class details
- **Custom Themes Demo**: See :doc:`scripts/custom_themes_demo` for working examples and testing environment

**External Tools**:

- `Adobe Color <https://color.adobe.com/>`_ - Professional color palette generator
- `Coolors <https://coolors.co/>`_ - Fast color scheme generator
- `Material Design Colors <https://material.io/design/color/>`_ - Google's color system
- `WebAIM Contrast Checker <https://webaim.org/resources/contrastchecker/>`_ - Accessibility verification 
