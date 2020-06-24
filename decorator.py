# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 17:44:29 2020
@author: Louis

TODO:
[] better import for the func

"""

all_func = {}
import dis


class Lmfunc:
    def __init__(self, name, ltype='Private'): #init class with name of project and it's private's level
        self.ltype = ltype
        self.name = name
        self.func_list = {}
        
    def func_params(self, func): #get all attribute of the func
        func_desc = {}
        func_desc['func'] = func
        func_desc['arg_nrb'] = func.__code__.co_argcount
        func_desc['filename'] = func.__code__.co_filename
        func_desc['varnames'] = func.__code__.co_varnames
        func_desc['doc'] = func.__doc__
        self.func_list[func.__name__] = func_desc
        
    def __call__(self, func): #this this the decorator
        self.func_params(func) #we call func_params for get all of attribute of the func
        def callabe(*args, **kwargs): #this is the callabe for call the func out of the class
            result = func(*args, **kwargs)
            return result
        return callabe
            
    def run_func(self, func_name, params=[]): #function for intern func call
        return self.func_list[func_name]['func'](*params)



def all_atribute(func):
    print(func['func'].__doc__)
    for attr in dir(func['func'].__code__):
        if attr != 'co_code':
            print('{} = {}'.format(attr, func['func'].__code__.__getattribute__(attr)))
        else:
            dis.dis(func['func'].__code__.__getattribute__(attr))
                
