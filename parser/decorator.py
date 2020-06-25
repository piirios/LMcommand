import os

class var_func:
    def __init__(self): #init class
        self.func_list = {}
        self.key = []

    def var_func_add(self,var_type, func): #setter for func_list
        self.func_list[var_type] = func
        self.key.append(var_type)
        
    def vartype(self, var_type):
        def decorator(func): #this this the decorator
            self.var_func_add(var_type, func) #we call func_params for get all of attribute of the func
            return func
        return decorator
    def run_func(self, var_type, params=[]): #function for intern func call
        if var_type in self.key:
            return self.func_list[var_type](*params)
        else:
            raise NotImplementedError




if __name__ == "__main__":
    vt = var_func()


    @vt.vartype('p')
    def path_traitement(value, vars):
        if value == "current":
            return os.path.abspath(os.path.curdir)
        else:
            return 'nop'



    r= vt.run_func('p', params=['currnt', {}])

    print(r)