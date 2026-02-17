import subprocess
import os

BIN_DIR = os.path.join(os.path.dirname(__file__), '..', 'bin')


def run(script, *args, input=None):
    path = os.path.join(BIN_DIR, script)
    result = subprocess.run(
        [path, *args],
        input=input,
        capture_output=True,
        text=True,
    )
    return result
