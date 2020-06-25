from decorator import var_func
import getpass
from blake3 import blake3
from LMprint import strc, printc

vf = var_func()

@vf.vartype('i')
def input_value(value, vars):
    res = input(strc(value, ltype='S'))
    return res

@vf.vartype('ip')
def input_password(vale, vars):
    pswd = blake3(bytes(getpass.getpass(strc('password:', ltype='S')), 'utf-8')).hexdigest()
