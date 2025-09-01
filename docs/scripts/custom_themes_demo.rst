Custom Themes Demo
==================

The Custom Themes Demo is a comprehensive demonstration of QDarkStyleSheet's custom theme capabilities. It showcases the complete workflow from palette definition to theme generation and application.

Overview
--------

The demo includes three complete theme examples, each demonstrating different approaches to custom theme creation:

- **Ocean Theme**: Blue-toned themes with cyan accents
- **Forest Theme**: Green themes mixing custom and built-in Gray system colors  
- **Sunset Theme**: Warm-colored themes with red/orange/yellow palette

Each theme demonstrates different color system design approaches:

- **Pure custom hex colors** (Ocean)
- **Mixed custom and built-in colors** (Forest)
- **Custom color system with warm tones** (Sunset)

Usage
-----

Run the demo from the project root:

.. code:: bash

   python scripts/custom_themes_demo.py

This will:

1. Generate all theme variants (6 total: 3 themes × 2 variants)
2. Launch a Qt demo application with theme switching
3. Clean up temporary files on exit

Demo Features
--------------

**Theme Generation**
- Automatic palette file creation
- Asset generation using qdarkstyle.utils CLI
- PNG icon generation with custom colors
- QSS stylesheet compilation
- Resource file creation

**Demo Application**
- Real-time theme switching
- Comprehensive UI widget showcase
- Theme color information display
- Status updates and error handling

**UI Widgets Demonstrated**
- Basic controls (buttons, checkboxes, radio buttons)
- Text input and editing
- Sliders and progress bars
- Tab widgets and group boxes
- List and tree widgets
- Tool buttons and spin boxes

Theme Examples
--------------

Ocean Theme
~~~~~~~~~~~

 | **Dark Variant**: Deep ocean blues with cyan accents  
 | **Light Variant**: Very light blues with dark ocean text

.. code:: python

   class OceanDarkPalette(Palette):
       ID = "dark"
       COLOR_BACKGROUND_1 = "#0a1a2e"  # Deep ocean blue
       COLOR_ACCENT_1 = "#00d4ff"      # Bright cyan
       # ... other colors

Forest Theme
~~~~~~~~~~~~

 | **Dark Variant**: Custom greens mixed with built-in Gray system  
 | **Light Variant**: Light greens with dark green text

.. code:: python

   class ForestDarkPalette(Palette):
       ID = "dark"
       COLOR_BACKGROUND_1 = "#1a2f1a"  # Custom dark green
       COLOR_TEXT_1 = Gray.B150        # Built-in gray
       # ... other colors

Sunset Theme
~~~~~~~~~~~~

 | **Dark Variant**: Warm grays transitioning to reds/oranges
 | **Light Variant**: Very light warm tones with dark text

.. code:: python

   class SunsetDarkPalette(Palette):
       ID = "dark"
       COLOR_BACKGROUND_1 = "#2F2F2F"  # Very dark warm gray
       COLOR_ACCENT_1 = "#FF6347"      # Tomato red
       # ... other colors

Development Workflow
--------------------

The demo demonstrates the complete custom theme development workflow:

1. **Palette Definition**: Create palette classes inheriting from `qdarkstyle.palette.Palette`
2. **Asset Generation**: Use `qdarkstyle.utils` CLI to generate theme assets
3. **Theme Application**: Load and apply custom themes to Qt applications
4. **Testing**: Verify themes work correctly across different UI elements

Key Functions
-------------

**create_palette_file()**
   Serializes palette classes to Python files for theme generation

**generate_theme()**
   Orchestrates the complete theme generation process using qdarkstyle.utils

**CustomThemeDemo**
   PyQt5 demo window with theme selection and comprehensive UI widgets

**show_theme_info()**
   Displays detailed color palette information for the selected theme

Integration with Documentation
------------------------------

This demo complements the `custom_palettes.rst` documentation by providing:

- **Working examples** of all documented concepts
- **Real-world implementation** of custom theme creation
- **Interactive testing** environment for theme development
- **Complete workflow** demonstration from start to finish

The demo serves as both a learning tool and a testing environment for custom theme development.

See Also
--------

- :doc:`../custom_palettes` - Comprehensive custom palette documentation
- :doc:`qdarkstyle_utils` - CLI tool for theme generation
- :doc:`../color_reference` - Built-in color system reference 
