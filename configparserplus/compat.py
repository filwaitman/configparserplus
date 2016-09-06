import sys

is_py2 = (sys.version_info[0] == 2)
is_py3 = (sys.version_info[0] == 3)

if is_py2:
    from ConfigParser import ConfigParser  # noqa
    from StringIO import StringIO  # noqa

if is_py3:
    from configparser import ConfigParser  # noqa
    from io import StringIO  # noqa
