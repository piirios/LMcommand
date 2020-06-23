import os
from caller import call

def load_file(filename):
    with open('{}.lmcommand'.format(filename), 'r') as f:
        lines = f.readlines()

    return lines

def separate_headers(l):
    print(l)
    i = l.index('----\n')
    header = l[:i]
    content = l[i+1:]
    return header, content

def header_check(header):
    token = header[0].split(':')[1].strip()
    filehash = header[1].split(':')[1].strip()
    return token, filehash

def command_traitement(content):
    for command in content:
        command = command.rstrip()
        command = check_command_variables(command)
        res = call(command)
        if res.returncode !=0:
            print(f"erreur: {res.stderr}")

def check_command_variables(command):
    if not '{%' in command:
        print('any command in this line')
        return command.split(' ')
    else:
        command = command.split(' ')
        id = [command.index(element) for element in command if '{%' in element][0]
        print(command[id].split('{%')[1].split('%}')[0])
        variable = command[id].split('{%')[1].split('%}')[0]
        typev, value = variable.split(':')
        value_var = variable_execute(typev.strip(), value.strip())
        command[id] = value_var
        print(f"variables type: {typev} value: {value} -> value:{value_var}") 
        return command


def variable_execute(typev, value):
    if typev == 'i':
        value = ' '.join(value.split('_'))
        value = input(f" {value}: ")

    elif typev == 'path':
        if value =='current':
            value = os.path.abspath(os.path.curdir)
    return value
l = load_file('test')
header, content = separate_headers(l)
creditential = header_check(header)
command_traitement(content)

print(creditential)
