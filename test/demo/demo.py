# Find buildcpp
import sys
from pathlib import Path
sys.path.insert(0, Path(__file__).parent.parent.parent.joinpath('src').as_posix())

# core
from buildcpp import *

target = Target('demo')\
    .add_sources(Scope.PUBLIC, find_files(SRC_ROOT, '*.cpp'))\
    .add_includes(Scope.PUBLIC, find_directories(PROJECT_ROOT, 'include'))\
    .cxx_standard(20)
    

if __name__ == '__main__':
    builder = Builder()
    builder.attach(target)
    builder.build(generator=Generator.MinGW)