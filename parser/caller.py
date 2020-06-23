import subprocess as sp

def call(command):
    print(command)
    return sp.run(command, capture_output=True, text=True, shell=True)