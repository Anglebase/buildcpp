# Find buildcpp
from buildcpp import *
import sys
from pathlib import Path
sys.path.insert(
    0, Path(__file__).parent.parent.parent.joinpath('src').as_posix())

# core

hello = Target('hello', Type.STATIC_LIBRARY)\
    .add_includes(Scope.PUBLIC, find_directories(Path(__file__).parent, 'include'))\
    .add_sources(Scope.PUBLIC, find_files(Path(__file__).parent / 'src', '*cpp'))\

export = hello

if __name__ == '__main__':
    pass