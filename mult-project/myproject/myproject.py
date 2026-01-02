from buildcpp import Target, Scope, Builder, import_project
from pathlib import Path

ROOT = Path(__file__).parent

add = import_project(ROOT.parent/'thirdparty/third.py')['add']

main = Target('main')\
    .add_sources(Scope.PRIVATE, ROOT/'main.cpp')\
    .depend_on(add)

if __name__ == '__main__':
    builder = Builder()
    builder.attach(main)
    builder.build()
