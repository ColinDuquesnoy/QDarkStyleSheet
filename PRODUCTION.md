# Production

Of course, until you start these steps, make sure the package have passed all
tests and checkers before continue.

- Create a `.pypirc` file in your home folder with this
    ```bash
        [distutils]
        index-servers =
        pypi
        testpypi

        [pypi]
        repository:https://pypi.python.org/pypi
        username=your username

        [testpypi]
        repository: https://test.pypi.org/legacy/
        username=your username
    ```

    If you want to put also your password in that file, remember to set
    appropriated permission to it.

    *Note that you need to create an account for both sites.*

- Install TWine
    ```bash
        sudo apt install twine
    ```

- Register if necessary
    ```bash
        python setup.py register
    ```

- Create a distribution (code package and wheel)
    ```bash
        python setup.py sdist bdist_wheel
    ```

- Test uploading using Twine
    ```bash
        twine upload -r testpypi dist/*
    ```

- Check if things are OK on [PyPI test page](https://test.pypi.org/project/QDarkStyle).

- Test installing using pip from test PyPI
    ```bash
        pip install --index-url https://test.pypi.org/project/ qdarkstyle
    ```

- **If you make sure all things are OK**, upload officialy
    ```bash
        twine upload -r pypi dist/*
    ```

- Check if things are OK on [PyPI official page](https://pypi.python.org/pypi/QDarkStyle).

- Test installing using pip
    ```bash
        pip install qdarkstyle
    ```