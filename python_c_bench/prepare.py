from pathlib import Path
from subprocess import run

import click

from python_c_bench import get_helloworld_executable


def _heading(msg: str) -> None:
    click.secho(msg, fg='yellow', bold=True)


def _info(msg: str) -> None:
    click.secho(msg, fg='cyan')


def prepare_helloworld(implementation: str, *, build_path: Path) -> None:
    if implementation == 'c':
        _heading("Preparing C implemementation of 'helloworld'")
        outfile = get_helloworld_executable(implementation, build_path)
        outfile.parent.mkdir(parents=True, exist_ok=True)
        run(['gcc', 'programs/helloworld/helloworld.c', '-o', str(outfile)])
        _info("Testing C implemementation of 'helloworld'")
        run([str(outfile)])
    elif implementation == 'nuitka':
        _heading("Preparing Nuitka implemementation of 'helloworld'")
        output_path = build_path / 'helloworld' / 'helloworld.nuitka.build'
        outfile = get_helloworld_executable(implementation, build_path)
        run([
            'python',
            '-m', 'nuitka',
            '-o', str(outfile),
            f'--output-dir={output_path}',
            'helloworld.py',
        ], cwd='programs/helloworld')
        _info("Testing Nuitka implemementation of 'helloworld'")
        run([str(outfile)])
    else:
        raise Exception(f"Unknown implementation {implementation!r}")
