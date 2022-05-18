#!/usr/bin/env python3

# import required libraries
import os, subprocess, sys


class EnvSpecNotExist(Exception):
    """
    Exception raised for errors where environment.yml or spec-file.txt is missingself.

    Attributes:
        file -- missing file name
    """

    def __init__(self, file: str):
        if file not in ["environment.yml", "spec-file.txt"]:
            super().__init__(
                f"Conda env file must be environment.yml or spec-file.txt, please check sys.argv file name!"
            )
        else:
            super().__init__(
                f"Conda env {file} is missing, please check provide file existence!"
            )


def check_environment_file(file: str = "environment.yml"):
    files = ["environment.yml", "spec-file.txt"]

    if file not in files:
        raise EnvSpecNotExist(file=file)

    return True


# read system argument files
if len(sys.argv) == 1:
    file = "environment.yml"
else:
    file = sys.argv[1]

assert check_environment_file(file)

# create a conda environment with environment.yml file
if file == "environment.yml":
    subprocess.run(["conda", "env", "create", "-f", file])
# create a environment with spec-file.txt
else:
    subprocess.run(["conda", "install", "--name", "bop", "--file", file])

sys.exit(0)
