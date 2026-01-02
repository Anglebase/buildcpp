from buildcpp import Target, Scope, Builder
from pathlib import Path

ROOT = Path(__file__).parent

main = Target('main')\
    .add_sources(Scope.PRIVATE, ROOT/'main.cpp')

if __name__ == '__main__':
    bdr = Builder()
    bdr.attach(main)
    bdr.build()
