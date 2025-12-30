# Find buildcpp
import sys
from pathlib import Path
sys.path.append(Path(__file__).parent.parent.parent.joinpath('src').as_posix())

# core
from buildcpp import *

target = Target('demo')\
    .add_sources(Scope.PUBLIC, find_files(SRC_ROOT, '*.cpp'))\
    .add_includes(Scope.PUBLIC, find_directories(PROJECT_ROOT, 'include'))
    

if __name__ == '__main__':
    builder = Builder()
    builder.attach(target)
    builder.build(generator=Generator.MinGW)