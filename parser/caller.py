from subprocess import run

def call(command):
    print(command)
    return run(command, capture_output=True, text=True, shell=True)