import sys
import importlib
from pathlib import Path


def load_module(directory, name):
    sys.path.insert(0, directory)
    importlib.import_module(name)
    sys.path.pop(0)


def load_directory(directory):
    pathlist = Path(directory).rglob('*.py')
    for path in pathlist:
        load_module(directory.as_posix(), path.stem)


def load_bundled():
    directory = Path(__file__).parent + '/extensions'
    load_directory(directory)
