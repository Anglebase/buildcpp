import os
from abc import ABC, abstractmethod
from enum import Enum
from pathlib import Path
from ..const import BUILD_ROOT, PROJECT_NAME


class AbstractTarget(ABC):
    """
    This abstract class is used for handling dependencies between projects.
    """
    name_set = set()

    def __init__(self, name: str) -> None:
        super().__init__()

        self.name = name
        assert name not in AbstractTarget.name_set, f"Duplicate target name: {name}"

    @abstractmethod
    def to_cmake(self) -> str:
        pass


class Type(Enum):
    EXECUTABLE = 1
    STATIC_LIBRARY = 2
    SHARED_LIBRARY = 3
    MODULE_LIBRARY = 4
    OBJECT_LIBRARY = 5
    INTERFACE_LIBRARY = 6

    def __str__(self) -> str:
        if self == Type.EXECUTABLE:
            return "EXECUTABLE"
        elif self == Type.STATIC_LIBRARY:
            return "STATIC"
        elif self == Type.SHARED_LIBRARY:
            return "SHARED"
        elif self == Type.MODULE_LIBRARY:
            return "MODULE"
        elif self == Type.OBJECT_LIBRARY:
            return "OBJECT"
        elif self == Type.INTERFACE_LIBRARY:
            return "INTERFACE"
        assert False, 'Invalid type'


class Scope(Enum):
    PUBLIC = 1
    PRIVATE = 2
    INTERFACE = 3

    def __str__(self) -> str:
        if self == Scope.PUBLIC:
            return "PUBLIC"
        elif self == Scope.PRIVATE:
            return "PRIVATE"
        elif self == Scope.INTERFACE:
            return "INTERFACE"
        assert False, 'Invalid scope'


class Target(AbstractTarget):
    def __init__(self, name: str, type: Type = Type.EXECUTABLE) -> None:
        super().__init__(name)

        self.type = type

        self._sources: dict[Scope, list[Path]] = {}

    def __expand(self, ls) -> list:
        result = []
        for item in ls:
            if isinstance(item, list):
                result.extend(self.__expand(item))
            else:
                result.append(item)
        return result

    def add_source(self, scope: Scope, *sources):
        if scope not in self._sources:
            self._sources[scope] = []
        items = self.__expand(sources)
        assert len(items) > 0 and \
            all(isinstance(item, Path)for item in items), \
            "Invalid source files"
        self._sources[scope].extend(items)
        return self

    def to_cmake(self) -> str:
        result = f"add_executable({self.name})\n"
        for scope in self._sources:
            files = [f'"{item.as_posix()}"' for item in self._sources[scope]]
            result += f"target_sources({self.name} {str(scope)} {' '.join(files)})\n"

        return result


class Builder:
    def __init__(self) -> None:
        self.targets = []

    def attach(self, target: AbstractTarget):
        self.targets.append(target)

    def _gen_cmakelists(self, output_dir: Path):
        output_dir.mkdir(exist_ok=True)
        cmakelists = f"cmake_minimum_required(VERSION 3.15)\n"
        cmakelists += f"project({PROJECT_NAME})\n"

        for target in self.targets:
            cmakelists += target.to_cmake()

        with open(output_dir / "CMakeLists.txt", 'w+') as f:
            f.write(cmakelists)

    def build(self, *, output_dir: Path = BUILD_ROOT):
        self._gen_cmakelists(output_dir)
        os.system(
            f"cmake -S {output_dir.as_posix()} -B {output_dir.as_posix()}")
        os.system(f"cmake --build {output_dir.as_posix()}")
