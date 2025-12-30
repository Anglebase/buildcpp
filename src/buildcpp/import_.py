from pathlib import Path
from .cmake.target import AbstractTarget


def import_project(buildcpp: Path) -> dict:
    project_dir = buildcpp.parent
    project_name = project_dir.name.split('.')[0]

    import sys
    sys.path.insert(0, project_dir.as_posix())
    try:
        module = __import__(project_name)
    except ImportError:
        raise ImportError(f"Cannot import project '{buildcpp}'")
    finally:
        sys.path.remove(project_dir.as_posix())

    if not hasattr(module, 'export'):
        raise ImportError(
            f"Project '{buildcpp}' is not an importable project.")

    if isinstance(module.export, AbstractTarget):
        return {module.export.name: module.export}
    elif isinstance(module.export, list) and all(isinstance(t, AbstractTarget) for t in module.export):
        return {t.name: t for t in module.export}
    else:
        raise TypeError(f"Project '{buildcpp}' export is not a valid target.")
