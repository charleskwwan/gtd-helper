# cli/utils.py
#   Utility functions for the CLI

import pkgutil


def modules_in_pkg(pkg):
    """ Generator for modules in a python package (a directory with an
    __init__.py file in it)
    """
    for _, module_name, _ in pkgutil.walk_packages(pkg.__path__):
        yield module_name


def load_method(module_name, method_name):
    """ Return a function from a module given the module's name and the
    function's name
    """
    module = __import__(module_name, fromlist=[method_name])
    method = getattr(module, method_name)
    return method
