from pathlib import Path
from typing import Iterable

import click

from python_c_bench.prepare import prepare_helloworld


@click.command()
@click.argument('program')
@click.option('--which', multiple=True)
@click.option('--build-dir')
def prepare(program: str, which: Iterable[str], build_dir: str = None) -> None:
    if build_dir:
        build_path = Path(build_dir)
    else:
        build_path = Path(__file__).parent.parent / 'build'

    if program == 'helloworld':
        prepared = 0
        for implementation in which:
            prepare_helloworld(implementation, build_path=build_path)
            prepared += 1
        if not prepared:
            raise click.ClickException("Use --which option to specify at least one implementation")
    else:
        raise Exception(f"Unknown program {program!r}")
