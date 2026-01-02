from buildcpp import Target, Scope, Builder, Type
from pathlib import Path

ROOT = Path(__file__).parent

add = Target("add", type=Type.STATIC_LIBRARY)\
    .add_includes(Scope.PUBLIC, ROOT/"add")\
    .add_sources(Scope.PRIVATE, ROOT/"add/add.cpp")

main = Target("main")\
    .add_sources(Scope.PRIVATE, ROOT/"src/main.cpp")\
    .depend_on(add)

if __name__ == "__main__":
    builder = Builder()
    builder.attach(main)
    builder.build()
