from decorator import var_func
import getpass
from blake3 import blake3
from LMprint import strc, printc
import os

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