from pathlib import Path


def abs_path_from_project(relative_path: str):
    return str(Path(__file__).parent.joinpath(relative_path))