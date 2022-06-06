import sys
import importlib


def load_extension(path, name):
    sys.path.append(path)
    try:
        return importlib.import_module(name, package=path)
    except ImportError:
        return None
