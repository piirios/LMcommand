import os
from caller import call
from var_func import vf

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
        #res = call(command)
        #if res.returncode !=0:
        #    print(f"erreur: {res.stderr}")

def check_command_variables(command, vars): #this function check if a variable is in the line and call the var execute function for render command
    print(f"command is {command}")
    if not '{%' in command:
        print('any command in this line')
        return command.split(' ')
    else:
        for c in command.split(' '):
            if not '{%' in c:
                continue
            else: 
                start = c.find('{%')
                end = c.rfind('%}')
                content = c[start+2:end]
                vtype, value = separate_variables(content)
                if '{%' in value:
                    _, value, vars = check_command_variables(content, vars)
                value, vars = variable_execute(vtype, value, vars)
                print(f'value is {value}')
                print(f"start:{start} end:{end} content:{content}")
                return vtype, value, vars
        """
        command = command.split(' ')
        print(command)
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
        """

def separate_variables(content):
    print(content.split(':', 1))
    typev, value = content.split(':', 1)[:2]
    typev = separate_type_variable(typev)
    print(f"variables type: {typev} value: {value}")
    return typev, value

def separate_type_variable(content):
    return content.split('_')

def variable_execute(typev, value, vars): #this function execute variable snippet and replace it for make valid commandline command
    for vartype in typev:
        print(f"variables type: {vartype} value: {value}")
        try:
            value = vf.run_func(vartype, params=[value, vars])
        except NotImplementedError:
            print(f"not implemented for {vartype}")

            if vartype == 's':
                if value in vars:
                    value =  vars[value]
                else:
                    raise ValueError
            
            elif vartype.split('=')[0] == 'v':
                varname = vartype.split('=')[1]
                if varname not in vars:
                    vars[varname] = value

            else:
                raise ValueError("unknown variable type %s" % vartype)

            """
            if len([typev.index(element) for element in vartype if 'v' in element]) != 0:
                id = [typev.index(element) for element in vartype if 'v' in element][0]
                varname = typev[id].split('=')[1]
                value = vars[varname]


            if len([typev.index(element) for element in vartype if 's' in element]) != 0:
                id = [typev.index(element) for element in vartype if 's' in element][0]
                varname = typev[id].split('=')[1]
                vars[varname] = value
                print(vars)

            """

    return value, vars


l = load_file('test')
header, content = separate_headers(l)
creditential = header_check(header)
command_traitement(content)

print(creditential)
