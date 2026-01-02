# Buildcpp: A Python Build System for C++ Projects  

![MIT-LICENSE](https://img.shields.io/github/license/Anglebase/buildcpp)  
![PyPI](https://img.shields.io/pypi/v/buildcpp)

Buildcpp is a build tool that uses Python as the scripting language for C++ projects. Its minimalist design makes building C++ projects straightforward and efficient.

## Installation  

Buildcpp requires **Python 3.7 or higher**. You can download Python from [python.org](https://www.python.org/downloads/).  
Once Python is installed, install Buildcpp via pip:

```shell
pip install buildcpp
```

Buildcpp also depends on **CMake 3.15 or later**, which you can download from [cmake.org](https://cmake.org/download/).  
Under the hood, Buildcpp uses Python for front-end scripting and CMake as the back-end build engine.

## Usage  

Buildcpp is a Python package that provides a set of APIs for defining and building C++ projects.  
To use it, simply create a Python script in your project directory and define your build using Buildcpp’s API. Running this script will execute the build.

While Buildcpp uses a script-based approach, the script itself resembles a configuration file. This design choice stems from the fact that C++ builds often involve numerous configuration options, which can become cumbersome in static configuration files.

Here’s a minimal example:

```python title="myproject.py"
from buildcpp import Target, Builder, Scope
from pathlib import Path

# Get current directory
ROOT = Path(__file__).parent

# Define a build target
target = Target('main')\
    .add_sources(Scope.PRIVATE, ROOT / 'main.cpp')

if __name__ == '__main__':
    # Create a builder and compile the target
    builder = Builder()
    builder.attach(target)
    builder.build()
```

Even without prior Python experience, you can likely understand what’s happening if you’re familiar with C++.  
The `Target` object is central to Buildcpp—it holds all the metadata needed for the build, much like a configuration file.

If you want to learn more, check out the [documentation](https://anglebase.github.io/buildcpp/site/quick/).

## LICENSE

This project is licensed under the MIT license.
