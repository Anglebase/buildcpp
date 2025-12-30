from pathlib import Path
from .target import AbstractTarget
from ..const import PROJECT_NAME, BUILD_ROOT
import os
import subprocess


class Builder:
    def __init__(self, *, cmake=None) -> None:
        self.targets = []

        self._cmake = cmake or "cmake"
        self._check_cmake()

    def _check_cmake(self):
        result = subprocess.run(
            [self._cmake, "--version"],
            capture_output=True,
            shell=True,
            text=True,
        )
        assert result.returncode == 0, "CMake not found"
        stdout = result.stdout.strip()
        assert "cmake version" in stdout, "Invalid CMake"

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
            f"{self._cmake} -S {output_dir.as_posix()} -B {output_dir.as_posix()}")
        os.system(f"{self._cmake} --build {output_dir.as_posix()}")
