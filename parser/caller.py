from subprocess import run

"""
TODO:
[] finish the caller process
  [] change run by popen
  [] cwd control
"""

def call(command):
    return run(command, capture_output=True, text=True, shell=True)