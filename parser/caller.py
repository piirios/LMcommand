from subprocess import run, PIPE
import os

"""
TODO:
[] finish the caller process
    [] change run by popen
    [] cwd control
"""

def call(command):
    res = run(command, text=True, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, cwd=os.getcwd())
    return res