import os

import appdirs
from lekt.__about__ import __app__

PLUGINS_ROOT_ENV_VAR_NAME = "LEKT_PLUGINS_ROOT"

# Folder path which contains *.yml and *.py file plugins.
# On linux this is typically ``~/.local/share/lekt-plugins``. On the nightly branch
# this will be ``~/.local/share/lekt-plugins-nightly``.
# The path can be overridden by defining the ``LEKT_PLUGINS_ROOT`` environment
# variable.


PLUGINS_ROOT = os.path.expanduser(
    os.environ.get(PLUGINS_ROOT_ENV_VAR_NAME, "")
) or '/app/lekt-plugins'  # TODO: get from context

#appdirs.user_data_dir(appname=__app__ + "-plugins")
