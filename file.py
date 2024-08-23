def abs_path_from_project(relative_path: str):
    from pathlib import Path

    return (
        Path(__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )