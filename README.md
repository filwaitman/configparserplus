[![Travis](https://travis-ci.com/filwaitman/configparserplus.svg?branch=master)](https://travis-ci.com/filwaitman/configparserplus)
[![Codecov](https://codecov.io/gh/filwaitman/configparserplus/branch/master/graph/badge.svg)](https://codecov.io/gh/filwaitman/configparserplus)
[![PyPI](https://img.shields.io/pypi/v/configparserplus.svg)](https://pypi.python.org/pypi/configparserplus/)
[![License](https://img.shields.io/pypi/l/configparserplus.svg)](https://pypi.python.org/pypi/configparserplus/)
[![Python versions](https://img.shields.io/pypi/pyversions/configparserplus.svg)](https://pypi.python.org/pypi/configparserplus/)
[![PyPI downloads per month](https://img.shields.io/pypi/dm/configparserplus.svg)](https://pypi.python.org/pypi/configparserplus/)


# configparserplus

If you have to multiple `.ini` files (for instance, when dealing with Pyramid's settings) you probably realized that the lack of a decent hierarchy between settings files just sucks.

**configparserplus allows you to use Jinja2 templating language on your .ini files** so you don't need to ctrl-C, ctrl-V your settings in your N config files. Seriously, never do it again. Just. Never.


## Usage:

Just replace:
```python
from configparser import ConfigParser  # `from ConfigParser import ConfigParser` in Python2
config = ConfigParser()
```

... to:
```python
from configparserplus import ConfigParserPlus
config = ConfigParserPlus()
```

... and refactor your `.ini` files to use Jinja stuff (such as [templates inheritance](https://jinja.palletsprojects.com/en/2.11.x/templates/#template-inheritance))

For more details, please check [these examples](https://github.com/filwaitman/configparserplus/tree/master/tests/fixtures).
Ah! Configparserplus **works normally on non-jinja** (boring, regular) `.ini` files - so you can just replace it and refactor bit by bit.


## Development:

### Run linter:
```bash
pip install -r requirements_dev.txt
isort -rc .
tox -e lint
```

### Run tests via `tox`:
```bash
pip install -r requirements_dev.txt
tox
```

### Release a new major/minor/patch version:
```bash
pip install -r requirements_dev.txt
bump2version <PART>  # <PART> can be either 'patch' or 'minor' or 'major'
```

### Upload to PyPI:
```bash
pip install -r requirements_dev.txt
python setup.py sdist bdist_wheel
python -m twine upload dist/*
```

## Contributing:

Please [open issues](https://github.com/filwaitman/configparserplus/issues) if you see one, or [create a pull request](https://github.com/filwaitman/configparserplus/pulls) when possible.
In case of a pull request, please consider the following:
- Respect the line length (132 characters)
- Write automated tests
- Run `tox` locally so you can see if everything is green (including linter and other python versions)
