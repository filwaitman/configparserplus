configparserplus (a.k.a. ".ini is boring.")
============================================

If you have to use .ini files on your projects you probably realized that the lack of a decent hierarchy between settings files just sucks.

**configparserplus allows you to use Jinja2 templating language on your .ini files** so you don't need to ctrl-C, ctrl-V your settings in your N config files. Seriously, never do it again. Just. Never.


Installation:
-------------
.. code:: bash

    pip install configparserplus


Usage:
-------------

Just replace your boring:

.. code:: python

    from ConfigParser import ConfigParser  # Python 2
    from configparser import ConfigParser  # Python 3

    config = ConfigParser()
    # ...


With a super cool:

.. code:: python

    from configparserplus import ConfigParserPlus  # Python 2 and Python 3 _o/

    config = ConfigParserPlus()
    # ...


* Please note that configparserplus **works nicely on both Python 2 and Python 3**. Also, it **works normally on non-jinja** (boring, regular) .ini files - so you can just replace it and refactor bit by bit.
* Ah! If you just want to **generate** (not **read/parse**) .ini files using Jinja2 engine I would recommend using `jinja2-standalone-compiler <https://github.com/filwaitman/jinja2-standalone-compiler>`_


Contribute
----------
Did you think in some interesting feature, or have you found a bug? Please let me know!

Of course you can also download the project and send me some `pull requests <https://github.com/filwaitman/configparserplus/pulls>`_.


You can send your suggestions by `opening issues <https://github.com/filwaitman/configparserplus/issues>`_.

You can contact me directly as well. Take a look at my contact information at `http://filwaitman.github.io/ <http://filwaitman.github.io/>`_ (email is preferred rather than mobile phone).
