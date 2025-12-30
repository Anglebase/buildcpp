# buildcpp

![MIT-LICENSE](https://img.shields.io/github/license/Anglebase/buildcpp)
![PyPI](https://img.shields.io/pypi/v/buildcpp)

Buildcpp is an innovative build system that combines Python's expressive power with the reliability of CMake. No longer need to worry about complex CMake syntax - manage your C++ projects with clear and maintainable Python code.

## Why buildcpp?

Building a C++ project is usually a very tedious operation. From Makefile to CMake and then to Xmake, everyone hopes to reduce the difficulty of building C++ projects. However, the inherent complexity of building C++ projects is unavoidable. The goal of Buildcpp is to use Python's approachable syntax as a build script for C++ projects and provide some facilities for building C++ projects.

## How It Works?

In fact, Buildcpp plays the same role as CMake in building systems. We can generate the corresponding Makefile by writing a CMake script and running cmake. Similarly, the design principle of Buildcpp is to allow us to write Python scripts to run and generate a CMake script for building. In this way, it not only avoids duplicate wheel building, but also makes Buildcpp inherently cross platform, as Python and CMake are both cross platform.

## Getting Started

Buildcpp is essentially a Python package, first you need to ensure that your device has a [Python 3.7+](https://www.python.org/) environment.

Run the following code in the terminal:

```shell
pip install buildcpp
```

After installation, your device will have the conditions to use Buildcpp.

For example, you can create a new directory for your C++ project and create a new Python file in it. Now, we have such a directory. There are no special requirements for the names of folders and Python files, you can choose any name you like. Additionally, it should be noted that the name of the Python file will be considered as the project name.

```text
myproject
└── myproject.py
```

Now, you can add C++ code files according to your habits. Buildcpp has no requirements for these things. For example, I like to create a `src` folder to store `.cpp` files. I write a Hello World code in the C++ file. Now, its directory structure is as follows:

```text
myproject
├── myproject.py
└── src
    └── main.cpp
```

We started using Buildcpp to write build scripts:

```python
from buildcpp import *

target = Target('demo')\
    .add_source(Scope.PUBLIC, find_files(SRC_ROOT, '*.cpp'))

if __name__ == '__main__':
    builder = Builder()
    builder.attach(target)
    builder.build()
```

Here, we first create a `Target` object with the name `demo`. We then add the source files to the target using the `add_source` method. The `Scope.PUBLIC` parameter specifies that these files are public, which means that they can be accessed by other targets. The `find_files` function is used to find all the C++ files in the `src` folder.

Next, we create a `Builder` object and attach the target to it. Finally, we call the `build` method to generate the Makefile and build the project.

## LICENSE

MIT-License
