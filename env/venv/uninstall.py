#!/usr/bin/env python3
import sys, subprocess

# remove the virtual environment directory
print("Remove /usr/share/py-bof directory content")
subprocess.run(["rm", "-rf", "./venv-bop"])

sys.exit()
