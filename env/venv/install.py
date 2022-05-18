#!/usr/bin/env python3
import subprocess, sys

# this install script will install a virtual environment under ~ path

print("Build a python virtual envrionment")
subprocess.run(["python3", "-m", "venv", "./venv-bop"])

sys.exit()
