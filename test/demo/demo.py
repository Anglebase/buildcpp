# Find buildcpp
import sys
from pathlib import Path
sys.path.insert(0, Path(__file__).parent.parent.parent.joinpath('src').as_posix())

# core
from buildcpp import *

hello = import_project(PROJECT_ROOT.parent / 'hello'/ 'hello.py')['hello']

lib = Target('add', Type.STATIC_LIBRARY)\
    .add_sources(Scope.PUBLIC, find_files(SRC_ROOT, 'add.cpp'))

target = Target('demo')\
    .add_sources(Scope.PUBLIC, find_files(SRC_ROOT, 'main.cpp'))\
    .add_includes(Scope.PUBLIC, find_directories(PROJECT_ROOT, 'include'))\
    .depend_on(hello, lib)
    

if __name__ == '__main__':
    builder = Builder()
    builder.attach(target)
    builder.build(generator=Generator.MinGW)