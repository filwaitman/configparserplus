# -*- coding: utf-8 -*-
import os
import sys

from jinja2 import Environment, FileSystemLoader, StrictUndefined

from .compat import ConfigParser, StringIO


def render_template(jinja_template):
    jinja_template = os.path.abspath(jinja_template)
    paths = [x[0] for x in os.walk(os.path.dirname(jinja_template))]

    environment = Environment(loader=FileSystemLoader(paths))
    environment.undefined = StrictUndefined
    template = environment.get_template(os.path.basename(jinja_template))
    return template.render()


class JinjaSupportMixin(object):
    def _read(self, fp, fpname):
        content = render_template(fpname)

        output = StringIO()
        output.write(content)
        output.seek(0)
        return ConfigParser._read(self, output, fpname)  # On python2 ConfigParser is an old-style class.


class StrictFalseMixin(object):
    def __init__(self, *args, **kwargs):
        if sys.version_info[0] == 3:
            kwargs.setdefault('strict', False)

        ConfigParser.__init__(self, *args, **kwargs)  # On python2 ConfigParser is an old-style class.


class ConfigParserPlus(JinjaSupportMixin, StrictFalseMixin, ConfigParser):
    pass
