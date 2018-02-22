# Contributing

This file describes a path to contribute to this project. Check out our
[CODE OF CONDUCT](./CODE_OF_CONDUCT.md).

## Bug Reports and Feature Requests

If you have encountered a problem with QDarkStyle or have an idea for a new
feature, please submit it to the
[issue tracker](https://github.com/ColinDuquesnoy/QDarkStyleSheet/issues).

## Contributing to QDarkStyle

The recommended way for new contributors to submit code to QDarkStyle is to
fork the repository on GitHub and then submit a pull request after
committing the changes.  The pull request will then need to be approved by one
of the manteiners before it is merged into the main repository.

- Check for open issues or open a fresh issue to start a discussion around a
    feature idea or a bug.
- Fork [the repository](https://github.com/ColinDuquesnoy/QDarkStyleSheet)
    on GitHub to start making your changes to the master branch.
- Write a test which shows that the bug was fixed or that the feature works
    as expected if its a function, or create a screenshot if you are changing
    the stylesheet evidencing the changes.
- Send a pull request and bug the maintainer until it gets merged and
    published. Make sure to add yourself to
    [AUTHORS](./AUTHORS.md)
    and the change(s) to
    [CHANGES](./CHANGES.md).

## Getting Started

These are the basic steps needed to start developing on QDarkStyle.

- Create an account on GitHub.

- Fork the main
    [QDarkStyle repository](https://github.com/ColinDuquesnoy/QDarkStyleSheet)
    using the GitHub interface.

- Clone the forked repository to your machine.

    ```bash
       git clone https://github.com/USERNAME/qdarkstyle
       cd qdarkstyle
    ```

- Checkout the appropriate branch.

    ```bash
       git checkout master
    ```

- Setup a virtual environment (not essential, but highly recommended).

    ```bash
       virtualenv ~/.venv
       . ~/.venv/bin/activate
       pip install -e .
    ```

- Create a new working branch. Choose any name you like.

    ```bash
       git checkout -b feature-xyz
    ```

- Hands on.

    For tips on working with the code, see the Code Guide.

- Test, test, test.

    Testing is best done through ``tox``, which provides a number of targets and
    allows testing against multiple different Python environments:

- Please add a list point to [CHANGES](./CHANGES.md) if the fix or
    feature is not trivial (small doc updates, typo fixes).

- Please add you as an author to [AUTHORS](./AUTHORS.md).

- Add files to commit.

    Add files that are part of your changes, remember that each commit
    must represent a small but functional change. Remember to add CHANGES.md
    and AUTHORS.md too. To add all files changed do:
    ```bash
       git add .
    ```

- Commiting changes.

    GitHub recognizes certain phrases that can be used to automatically
    update the issue tracker, so you can commit like this:

    ```bash
       git commit -m "Add useful new feature that does this, close #42"
    ```
    ```bash
       git commit -m "Fix returning problem for get_style(), fix #78"
    ```

- Push changes in the branch to your forked repository on GitHub.

    ```bash
       git push origin feature-xyz
    ```

- Submit a pull request (PR).

    Do it from your branch to the respective branch using the
    [GitHub PR](https://github.com/ColinDuquesnoy/QDarkStyleSheet/pulls)
    interface.

- Wait for mainteiner to review your changes.

## Logging

Inside modules we provided a logging that should be used to inform the user.
Please, follow the levels bellow.

- debug: for debug information, high detailed one, directed to programers;
- info: something important for common user to know;
- warning: something that should not be a big problem or a desicision changed;
- error: some error, but not capable of stop program;
- critical: something that stops the running program.

## Guide to QDarkStyle

Now you can use our example to work on the stylesheet. It has all possible
widget provided by Qt - common ones. Feel free to add more to them.

To simplify the structure, there are separated files in
[example.ui](./example/ui/) folder.

- `dw_buttons.ui`: all types of buttons;
- `dw_containers_no_tabs.ui`: all types of containers except for tabs;
- `dw_containers_tabs.ui`: all containers tabs;
- `dw_displays.ui`: all types of displays;
- `dw_inputs_fields.ui`: all types of inputs with fields;
- `dw_inputs_no_fields.ui`: all types of inputs without fields;
- `dw_views.ui`: all types of views;
- `dw_widgets.ui`: all types of widgets;
- `mw_menus.ui`: main window with all menus and toolbars.

*Obs.: `dw` stands for dock widget and `mw` for main window.*

The entire example is built at runtime, in
[example.py](./example/example.py). To see more information about it,
see its documentation.

### Modifying UI Files

Feel free to modify [ui](./example/ui) files with Qt Designer and recompile UI using
[process_ui.py](./script/process_ui.py) script, inside script folder, using:

```bash
python process_ui.py
```

It will generate all `_ui.py` files for PyQt4, PyQt5, PySide, QtPy, PyQtGraph.

### Modifying QSS File

If you are changing the [stylesheet](./qdarkstyle/style.qss), you will need
to recompile the QRC files using [process_qrc.py](./script/process_qrc.py)
script, inside script folder.

```bash
python process_qrc.py
```

This generates all `_rc.py` files for PyQt4, PyQt5, PySide, QtPy, PyQtGraph.

### Making It Easy

To simplify this process for the developer, if you are changing many things,
use the script [run_ui_css_edition.py](./script/run_ui_css_edition.py):

```bash
python run_ui_css_edition.py
```

This creates a loop that restarts the application, process ui and css
files.

For more information about those scripts, see their documentation.

### Qt, Stylesheets and Palettes

- [Box model](http://doc.qt.io/qt-5/images/stylesheet-boxmodel.png)
- [Box model with height and width](https://www.tutorialrepublic.com/lib/images/css-box-model.jpg)
- [Customizing Widgets](http://doc.qt.io/qt-5/stylesheet-customizing.html)
- [Window structure](http://doc.qt.io/qt-5/images/mainwindowlayout.png)
- [QMainWindow](http://doc.qt.io/qt-5/qmainwindow.html)
- [References](http://doc.qt.io/qt-5/stylesheet.html)

Create good palettes with these tools. For example, on paletton, choose
  three colors from greyish light (foreground), greyish dark (background)
  and three more colorfull colors (selection). Greyish colors have a litle
  bit of the main color, so it is nice to change it if you change the main
  color.

- [Paletton.com](http://paletton.com/)
- [Coolors.co](https://coolors.co/)

## Unit Testing and Fix Preview

It is a good practice, if you are writing functions to QDarkStyle or fixing
something related to those functions (not style), that you provide a test
for it.

If you are fixing something about style, please, at least, provide an
screenshot before and after the fix to comparison. This could be inserted
in the issue tracker, as a message. Better than that, use modules provided
in test folder to create a GUI test, creating a new file for it.

Check [test](./test) files to more details. Tests will keep our application stable.

## If You Are a Mantainer, Go Ahead

We create a guide to create and upload this package to PyPI, follow the
instructions in [PRODUCTION](./PRODUCTION.md).