# Extension

Buildcpp is not a closed build system, it provides an extensible interface called `AbstractTarget`. The `Target` provided by buildcpp is one of its subclasses. By inheriting `AbstractTarget` and implementing its abstract methods, you can achieve your own defined target logic.

```py title="target.py"
...

class AbstractTarget(ABC):
    def __init__(self, name: str) -> None:
        ...

    @abstractmethod
    def to_cmake(self) -> str:
        pass

    def depend_on(self, *targets, allow_invaild=False):
        ...

    def rename(self, new_name: str):
        ...

...
```

The above is the definition of the abstract class `AbstractTarget`, which has an abstract method `to_cmake` used to customize the target logic. Buildcpp is similar to CMake in that it translates Python code into CMake, just like how CMake translates CMake scripts into Makefiles.
