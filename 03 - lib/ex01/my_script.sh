#!/bin/sh

/usr/bin/python3 -m venv local_lib

source local_lib/bin/activate

python -m pip --version

python -m pip install --log pip_install.log --force-reinstall git+https://github.com/jaraco/path.git

python my_program.py