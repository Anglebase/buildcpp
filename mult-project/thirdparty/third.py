from buildcpp import Target, Scope, Type, Builder
from pathlib import Path

ROOT = Path(__file__).parent

add = Target('add', Type.STATIC_LIBRARY)\
    .add_includes(Scope.PUBLIC, ROOT/'include')\
    .add_sources(Scope.PRIVATE, ROOT/'src/add.cpp')

export = [add]

if __name__ == '__main__':
    builder = Builder()
    builder.attach(add)
    builder.build()
