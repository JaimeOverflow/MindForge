import os
import subprocess


def clean_screen():
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run(command, shell=True)
