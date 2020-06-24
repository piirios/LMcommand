# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 17:44:29 2020
@author: Louis
"""

all_func = {}
import dis


class workflow:
    def __init__(self, name, ltype='Private'):
        self.ltype = ltype
        self.name = name
        self.func_list = {}
        
    def func_params(self, func):
        func_desc = {}
        func_desc['func'] = func
        func_desc['arg_nrb'] = func.__code__.co_argcount
        func_desc['filename'] = func.__code__.co_filename
        func_desc['varnames'] = func.__code__.co_varnames
        func_desc['doc'] = func.__doc__
        self.func_list[func.__name__] = func_desc
        
    def __call__(self, func):
        self.func_params(func)
        def callabe(*args, **kwargs):
            result = func(*args, **kwargs)
            return result
        return callabe
            
    def run_func(self, func_name, params=[]):
        return self.func_list[func_name]['func'](*params)


if __name__ == '__main__':
    wf = workflow('test')

    @wf
    def add(a,b):
        return a + b

    @wf
    def diff(a,b):
        return a - b

    @wf
    def mul(a,b, lol='lol', y='xd'):
        """
        ####this fonction multiply a and b
        """
        bg = 'bg'
        alert = True
        return a*b


    r = wf.run_func('add', params=[3,6])
    print(r)



    def all_atribute(func):
        print(func['func'].__doc__)
        for attr in dir(func['func'].__code__):
            if attr != 'co_code':
                print('{} = {}'.format(attr, func['func'].__code__.__getattribute__(attr)))
            else:
                dis.dis(func['func'].__code__.__getattribute__(attr))
                
