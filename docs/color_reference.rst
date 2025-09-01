Colors
======

Color System
------------

The color system is the source of the colors that themes draw from. Each
has a range of values from ``0`` (black ``#000000``) to ``150`` (white
``#ffffff``). Not all colors are or should be used in every theme, but
the scales provide a chance to see the colors in a larger context and
makes it easy to switch out colors as desired.

The number assigned to each estimates how light or dark that color is.
For parts of an interface that are interactive, have text, or have any
other important information, please use colors combinations that have at
least a difference of 20 where colors overlap. Depending on the colors,
you may need more contrast to create a theme that meets accessibility
standards about contrast or color blindness.

Gray
~~~~

=========== =========== =========
System Name Value       Sample
=========== =========== =========
B0          ``#000000`` |image1|
B10         ``#19232D`` |image2|
B20         ``#262E38`` |image3|
B30         ``#37414F`` |image4|
B40         ``#455364`` |image5|
B50         ``#54687A`` |image6|
B60         ``#60798B`` |image7|
B70         ``#788D9C`` |image8|
B80         ``#9DA9B5`` |image9|
B90         ``#CBCACA`` |image10|
B100        ``#D9D8D8`` |image11|
B110        ``#E1E1E1`` |image12|
B120        ``#EEEEEE`` |image13|
B130        ``#F5F5F5`` |image14|
B140        ``#FAFAFA`` |image15|
B150        ``#FFFFFF`` |image16|
=========== =========== =========

Blue
~~~~

=========== =========== =========
System Name Value       Sample
=========== =========== =========
B0          ``#000000`` |image17|
B10         ``#062647`` |image18|
B20         ``#26486B`` |image19|
B30         ``#375A7F`` |image20|
B40         ``#346792`` |image21|
B50         ``#1A72BB`` |image22|
B60         ``#057DCE`` |image23|
B70         ``#259AE9`` |image24|
B80         ``#37AEFE`` |image25|
B90         ``#73C7FF`` |image26|
B100        ``#9FD9FF`` |image27|
B110        ``#C2E3FA`` |image28|
B120        ``#CEEBFF`` |image29|
B130        ``#DAF0FF`` |image30|
B140        ``#F5FBFF`` |image31|
B150        ``#FFFFFF`` |image32|
=========== =========== =========

Palette System
--------------

QDarkStyle uses a palette system that defines semantic color constants for different UI elements and states. This system ensures consistency across themes and makes it easy to customize colors.

Background Colors
~~~~~~~~~~~~~~~~~

Background colors are used for different layers and depths in the interface:

=================== ======================= ======================= =========
Constant            Dark Theme              Light Theme             Usage
=================== ======================= ======================= =========
COLOR_BACKGROUND_1  ``Gray.B10`` (#19232D)  ``Gray.B140`` (#FAFAFA) Base background
COLOR_BACKGROUND_2  ``Gray.B20`` (#293544)  ``Gray.B130`` (#DFE1E2) Secondary background
COLOR_BACKGROUND_3  ``Gray.B30`` (#37414F)  ``Gray.B120`` (#D2D5D8) Tertiary background
COLOR_BACKGROUND_4  ``Gray.B40`` (#455364)  ``Gray.B110`` (#C0C4C8) Raised elements
COLOR_BACKGROUND_5  ``Gray.B50`` (#54687A)  ``Gray.B100`` (#B4B8BC) Pressed elements
COLOR_BACKGROUND_6  ``Gray.B60`` (#60798B)  ``Gray.B90`` (#ACB1B6)  Hover elements
=================== ======================= ======================= =========

Text Colors
~~~~~~~~~~~

Text colors for different content types and importance levels:

=================== ======================= ======================= =========
Constant            Dark Theme              Light Theme             Usage
=================== ======================= ======================= =========
COLOR_TEXT_1        ``Gray.B130`` (#DFE1E2) ``Gray.B10`` (#19232D)  Primary text
COLOR_TEXT_2        ``Gray.B110`` (#C0C4C8) ``Gray.B20`` (#293544)  Secondary text
COLOR_TEXT_3        ``Gray.B90`` (#ACB1B6)  ``Gray.B50`` (#54687A)  Tertiary text
COLOR_TEXT_4        ``Gray.B80`` (#9DA9B5)  ``Gray.B70`` (#788D9C)  Quaternary text
=================== ======================= ======================= =========

Accent Colors
~~~~~~~~~~~~~

Accent colors for interactive elements, selections, and highlights:

=================== ======================= ======================= =========
Constant            Dark Theme              Light Theme             Usage
=================== ======================= ======================= =========
COLOR_ACCENT_1      ``Blue.B20`` (#26486B)  ``Blue.B130`` (#DAEDFF) Selection background
COLOR_ACCENT_2      ``Blue.B40`` (#346792)  ``Blue.B100`` (#9FCBFF) Primary selection
COLOR_ACCENT_3      ``Blue.B50`` (#1A72BB)  ``Blue.B90`` (#73C7FF)  Hover selection
COLOR_ACCENT_4      ``Blue.B70`` (#259AE9)  ``Blue.B80`` (#37AEFE)  Active elements
COLOR_ACCENT_5      ``Blue.B80`` (#37AEFE)  ``Blue.B70`` (#259AE9)  Focus indicators
=================== ======================= ======================= =========

Special Colors
~~~~~~~~~~~~~~

Special-purpose colors for specific UI states:

=================== ======================= ======================= =========
Constant            Dark Theme              Light Theme             Usage
=================== ======================= ======================= =========
COLOR_DISABLED      ``Gray.B70`` (#788D9C)  ``Gray.B80`` (#9DA9B5)  Disabled elements
=================== ======================= ======================= =========

Other Palette Properties
~~~~~~~~~~~~~~~~~~~~~~~~

Additional properties that define the visual appearance:

=================== ======================= =========
Constant            Value                   Usage
=================== ======================= =========
OPACITY_TOOLTIP     230                     Tooltip opacity
SIZE_BORDER_RADIUS  4px                     Border radius
=================== ======================= =========

Usage Examples
~~~~~~~~~~~~~~

**In custom palettes:**

.. code-block:: python

    from qdarkstyle.palette import Palette
    from qdarkstyle.colorsystem import Gray, Blue
    
    class DarkOceanPalette(Palette):
        ID = 'dark'  # Must use 'dark' for dark themes
        
        # Background colors
        COLOR_BACKGROUND_1 = Gray.B15
        COLOR_BACKGROUND_2 = Gray.B25
        
        # Text colors
        COLOR_TEXT_1 = Gray.B130
        COLOR_TEXT_2 = Gray.B110
        
        # Accent colors
        COLOR_ACCENT_1 = Blue.B30
        COLOR_ACCENT_2 = Blue.B50
        
        # Special colors
        COLOR_DISABLED = Gray.B75

**In SCSS/CSS:**

.. code-block:: text

    QWidget {
        background-color: $COLOR_BACKGROUND_1;
        color: $COLOR_TEXT_1;
    }
    
    QPushButton {
        background-color: $COLOR_BACKGROUND_4;
        color: $COLOR_TEXT_1;
    }
    
    QPushButton:hover {
        background-color: $COLOR_BACKGROUND_6;
    }
    
    QPushButton:disabled {
        color: $COLOR_DISABLED;
    }

.. |image1| image:: images/color_samples/GrayB0.png
.. |image2| image:: images/color_samples/GrayB10.png
.. |image3| image:: images/color_samples/GrayB20.png
.. |image4| image:: images/color_samples/GrayB30.png
.. |image5| image:: images/color_samples/GrayB40.png
.. |image6| image:: images/color_samples/GrayB50.png
.. |image7| image:: images/color_samples/GrayB60.png
.. |image8| image:: images/color_samples/GrayB70.png
.. |image9| image:: images/color_samples/GrayB80.png
.. |image10| image:: images/color_samples/GrayB90.png
.. |image11| image:: images/color_samples/GrayB100.png
.. |image12| image:: images/color_samples/GrayB110.png
.. |image13| image:: images/color_samples/GrayB120.png
.. |image14| image:: images/color_samples/GrayB130.png
.. |image15| image:: images/color_samples/GrayB140.png
.. |image16| image:: images/color_samples/GrayB150.png
.. |image17| image:: images/color_samples/BlueB0.png
.. |image18| image:: images/color_samples/BlueB10.png
.. |image19| image:: images/color_samples/BlueB20.png
.. |image20| image:: images/color_samples/BlueB30.png
.. |image21| image:: images/color_samples/BlueB40.png
.. |image22| image:: images/color_samples/BlueB50.png
.. |image23| image:: images/color_samples/BlueB60.png
.. |image24| image:: images/color_samples/BlueB70.png
.. |image25| image:: images/color_samples/BlueB80.png
.. |image26| image:: images/color_samples/BlueB90.png
.. |image27| image:: images/color_samples/BlueB100.png
.. |image28| image:: images/color_samples/BlueB110.png
.. |image29| image:: images/color_samples/BlueB120.png
.. |image30| image:: images/color_samples/BlueB130.png
.. |image31| image:: images/color_samples/BlueB140.png
.. |image32| image:: images/color_samples/BlueB150.png
