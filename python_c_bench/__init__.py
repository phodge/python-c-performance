from pathlib import Path


def get_helloworld_executable(implementation: str, build_path: Path) -> Path:
    if implementation == 'c':
        return build_path / 'helloworld' / 'helloworld_c'
    elif implementation == 'nuitka':
        return build_path / 'helloworld' / 'helloworld_nuitka'
    else:
        raise Exception(f"Unknown implementation {implementation!r}")
