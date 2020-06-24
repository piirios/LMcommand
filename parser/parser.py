import os
from caller import call

"""
parser of the file:
TODO:
[] finish variable parser
  [X] need to implement var into var => actual: only one level of var work need n level of var work
  [] implement python function var
  [] finish implement path var

[] future
  [] implement db var
  [] make a compiler for simplified writting command
    [] autorisation token
    [] hash secure
    [] db for persistent store of the token
  [] make a secure credentials storage
"""


def load_file(filename): #the function for loading the file and init the line by line read
    with open('{}.lmcommand'.format(filename), 'r') as f:
        lines = f.readlines()

    return lines

def separate_headers(l): #separate the header of the content in compiled file
    print(l)
    i = l.index('----\n')
    header = l[:i]
    content = l[i+1:]
    return header, content

def header_check(header): # TODO: implement file hash verification and token verify
    token = header[0].split(':')[1].strip()
    filehash = header[1].split(':')[1].strip()
    return token, filehash

def command_traitement(content): #this is the core func where we call the var checker, call the func into subprocess and check the result
    vars = {}
    print(content)
    for command in content:
        command = command.rstrip()
        command = check_command_variables(command, vars)
        res = call(command)
        if res.returncode !=0:
            print(f"erreur: {res.stderr}")

def check_command_variables(command, vars): #this function check if a variable is in the line and call the var execute function for render command
    print(f"command is {command}")
    if not '{%' in command:
        print('any command in this line')
        return command.split(' ')
    else:
        command = command.split(' ')
        id = [command.index(element) for element in command if '{%' in element][0]
        print(id)
        #rint(command[id].split('{%')[1].split('%}')[0])
        #print(command[id].split('{%')[1])
        variable = command[id].lstrip('{%').rstrip('%}')
        print(variable)
        typev, value = variable.split(':', 1)
        print(f"value before sub: {value}")
        if value.startswith('{%'):
            value = check_command_variables(value, vars)
        value = value.strip() if isinstance(value, (int, str)) else value[0]
        value_var, vars = variable_execute(typev.strip(),value, vars)
        command[id] = value_var
        print(f"variables type: {typev} value: {value} -> value:{value_var}") 
        return command


def variable_execute(typev, value, vars): #this function execute variable snippet and replace it for make valid commandline command
    typev = typev.split('_')
    
    if len([typev.index(element) for element in typev if 'v' in element]) != 0:
        id = [typev.index(element) for element in typev if 'v' in element][0]
        varname = typev[id].split('=')[1]
        value = vars[varname]

    elif 'i' in typev:
        print(value)
        value = ' '.join(value.split('_')) if '_' in value else value
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
