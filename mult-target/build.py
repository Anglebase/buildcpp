from buildcpp import Target, Scope, Builder
from pathlib import Path

ROOT = Path(__file__).parent

main = Target('main')\
    .add_sources(Scope.PRIVATE, ROOT/'main.cpp')

start = Target('start')\
    .add_sources(Scope.PRIVATE, ROOT/'start.cpp')

if __name__ == '__main__':
    bdr = Builder()
    bdr.attach(main, start)
    bdr.build()
