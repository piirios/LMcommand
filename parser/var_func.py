from lmdecorator import var_func
import getpass
from blake3 import blake3
from LMprint import strc, printc
import caller
import os
from db import get_command, init_db

vf = var_func()

@vf.vartype('i')
def input_value(value, vars):
    res = input(strc(value, ltype='S') + ' : ')
    return res

@vf.vartype('ip')
def input_password(value, vars):
    pswd = blake3(bytes(getpass.getpass(strc('password : ', ltype='S')), 'utf-8')).hexdigest()

@vf.vartype('path')
def path_var(value, vars):
    if value == 'current':
        return os.path.abspath(os.path.curdir)
    elif value.startswith('cd'):
        folder = value.strip('cd ')
        if os.path.exists(folder):
            if os.path.isdir(folder):
                return os.path.join(os.path.abspath(os.path.curdir), folder)
            else:
                raise ValueError("specified path isn't a directory")
        else:
            raise ValueError("Directory doesn't exist!")

@vf.vartype('py')
def python_code(value, vars):
    value = f'{os.getcwd()}{ os.path.normpath(value)}'
    value = "python {}".format(value).split(' ')
    return value

@vf.vartype('co')
def command(value, vars):
    from lmparser import load_file,header_check, separate_headers, command_traitement
    _, session = init_db()
    command_obj = get_command(session,value)
    lines = load_file(command_obj.filepath)
    header, content = separate_headers(lines)
    if header_check(session, header,value, content):
        command_traitement(content)
    return 