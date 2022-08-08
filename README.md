Python Hello-world Benchmarks
=============================

A performance comparision of "Idiomatic Python" versus "C".

Installation
------------

Create a python virtual environment, then pip install this project:

    python3 -m venv .venv
    . .venv/bin/activate
    pip install -e .


Preparing Executables
---------------------

Building benchmark executables with `./prepare` script

    python bin/prepare.py helloworld --which=c --which=nuitka ...
