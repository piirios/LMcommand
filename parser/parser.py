import os
from caller import call

def load_file(filename):
    with open('{}.lmcommand'.format(filename), 'r') as f:
        lines = f.readlines()
        print(dir(lines[0]))

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
    vars = {}
    for command in content:
        command = command.rstrip()
        command = check_command_variables(command, vars)
        res = call(command)
        if res.returncode !=0:
            print(f"erreur: {res.stderr}")

def check_command_variables(command, vars, i=1):
    print(f"command is {command}")
    if not '{%' in command:
        print('any command in this line')
        return command.split(' ')
    else:
        command = command.split(' ')
        id = [command.index(element) for element in command if '{%' in element][0]
        print(id)
        #rint(command[id].split('{%')[1].split('%}')[0])
        print(command[id].split('{%')[1])
        variable = command[id].split('{%')[1].split('%}')[0]
        print(variable)
        typev, value = variable.split(':')
        print(f"value before sub: {value}")
        if 1+i < len(command[id].split('{%')):
            value = check_command_variables(command[id].split('{%')[1+i].split('%}')[0], vars, i=i+1)
        print(value)
        value_var, vars = variable_execute(typev.strip(), ' '.join(value).strip(), vars)
        command[id] = value_var
        print(f"variables type: {typev} value: {value} -> value:{value_var}") 
        return command


def variable_execute(typev, value, vars):
    typev = typev.split('_')
    
    if len([typev.index(element) for element in typev if 'v' in element]) != 0:
        id = [typev.index(element) for element in typev if 'v' in element][0]
        varname = typev[id].split('=')[1]
        value = vars[varname]

    elif 'i' in typev:
        value = ' '.join(value.split('_'))
        value = input(f" {value}: ")

    elif 'path' in typev:
        if value =='current':
            value = os.path.abspath(os.path.curdir)

    if len([typev.index(element) for element in typev if 's' in element]) != 0:
        id = [typev.index(element) for element in typev if 's' in element][0]
        varname = typev[id].split('=')[1]
        vars[varname] = value
        print(vars)

    return value, vars


l = load_file('test')
header, content = separate_headers(l)
creditential = header_check(header)
command_traitement(content)

print(creditential)
