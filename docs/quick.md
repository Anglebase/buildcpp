# Getting Started

Buildcpp streamlines C++ builds by modeling them as a series of `Target` constructions. Build order is determined by dependency relationships between targets. Each `Target` is defined as a set of metadata containing everything needed to produce a single output—such as an executable (`.exe`), a static library (`.lib`, `.a`), or a dynamic library (`.dll`, `.so`).

## Building a Single `Target`

Buildcpp scripts are purely declarative. Even with only C++ knowledge and no Python experience, the syntax remains intuitive. Here’s the simplest build script:

```py title="myproject.py"
from buildcpp import Target, Builder, Scope
from pathlib import Path

# Get the current directory
ROOT = Path(__file__).parent
# Define a target
target = Target('main')\
    .add_sources(Scope.PRIVATE, ROOT / 'main.cpp')

if __name__ == '__main__':
    # Create a builder and compile the target
    builder = Builder()
    builder.attach(target)
    builder.build()
```

The corresponding project structure is:

```text
myproject/
├── main.cpp
└── myproject.py
```

Buildcpp does not enforce any specific directory layout—you’re free to organize projects as you prefer.

That’s all you need to get started. The `Target` object also provides additional APIs for configuring metadata like include paths, macro definitions, and more.

## Building Multiple `Targets`

A Python build script corresponds to a project in buildcpp, and a project can define multiple targets. When a target is built, all of its dependencies are automatically pulled into the build process.

To build several executables in one project, simply define multiple targets. For example, with two source files:

```text
myproject/
├── main.cpp
├── start.cpp
└── myproject.py
```

In `myproject.py`, define both targets and attach them to the builder:

```py title="myproject.py"
from buildcpp import Target, Builder, Scope
from pathlib import Path

# Get the current directory
ROOT = Path(__file__).parent
# Define targets
main = Target('main')\
    .add_sources(Scope.PRIVATE, ROOT / 'main.cpp')

start = Target('start')\
    .add_sources(Scope.PRIVATE, ROOT / 'start.cpp')

if __name__ == '__main__':
    # Create a builder and compile the targets
    builder = Builder()
    builder.attach(main, start)
    builder.build()
```

This approach is especially useful for compiling multiple test programs or examples in one go.

## Building with Dependencies (`Combined Target`)

Sometimes one target depends on code from another. Consider this project:

```text
myproject/
├── include/
│   └── add.h
├── src/
│   ├── add.cpp
│   └── main.cpp
└── myproject.py
```

If `main.cpp` uses a function from `add.cpp`, we could bundle both into one target—but a cleaner approach is to model them as separate targets with a dependency link.

```py title="myproject.py"
from buildcpp import Target, Builder, Scope
from pathlib import Path

# Get the current directory
ROOT = Path(__file__).parent
# Define targets
add = Target('add', type=Type.STATIC_LIBRARY)\
    .add_sources(Scope.PRIVATE, ROOT / 'src/add.cpp')\
    .add_includes(Scope.PUBLIC, ROOT / 'include')

main = Target('main')\
    .depend_on(add)

if __name__ == '__main__':
    # Create a builder and compile the targets
    builder = Builder()
    builder.attach(main)
    builder.build()
```

Note the `type` parameter in the `Target` constructor. By default, it produces an executable, but here we specify `STATIC_LIBRARY` to build a static library.

The `Scope` parameter defines the visibility of metadata:

+ **`Scope.PUBLIC`**: Visible to the current target and all targets that depend on it.
+ **`Scope.PRIVATE`**: Visible only to the current target.
+ **`Scope.INTERFACE`**: Visible only to dependent targets, not to the current target.

In the example above, we pass the include path with `Scope.PUBLIC`, so dependent targets like `main` automatically receive it. Because `main` depends on `add`, the builder will compile `add` first, then `main`.

## Building Across Multiple Projects

To reuse external projects without reinventing the wheel, buildcpp supports multi-project builds. Imagine two projects:

```text
myproject/
├── main.cpp
└── myproject.py

thirdparty/
├── include/
│   └── thirdparty.h
├── src/
│   ├── thirdparty.cpp
└── thirdparty.py
```

The third-party project exposes its target via an `export` variable:

```py title="thirdparty.py"
from buildcpp import Target, Builder, Scope
from pathlib import Path

# Get the current directory
ROOT = Path(__file__).parent
# Define target
thirdparty = Target('thirdparty', type=Type.STATIC_LIBRARY)\
    .add_sources(Scope.PRIVATE, ROOT / 'src/thirdparty.cpp')\
    .add_includes(Scope.PUBLIC, ROOT / 'include')

export = [thirdparty]
# Alternatively:
# export = thirdparty

if __name__ == '__main__':
    builder = Builder()
    builder.attach(thirdparty)
    builder.build()
```

The `export` variable is a convention in buildcpp for exposing targets to other projects.

Your own project can then import and use that target:

```py title="myproject.py"
from buildcpp import Target, Builder, Scope
from pathlib import Path

thirdparty = import_project('path/to/thirdparty')['thirdparty']

# Get the current directory
ROOT = Path(__file__).parent
# Define target
main = Target('main')\
    .add_sources(Scope.PRIVATE, ROOT / 'main.cpp')\
    .depend_on(thirdparty)

if __name__ == '__main__':
    builder = Builder()
    builder.attach(main)
    builder.build()
```

The `import_project` function returns a dictionary (similar to a C++ `hashmap`) where keys are target names and values are `Target` instances. These can be used just like locally defined targets.
