from lmparser import load_file
from hash import hash_content, hash_token, gen_token
from db import init_db, get_command, check_command_exists, add_command, get_all, del_all
from os import path
import base64

def compile(filepath=None, name=None, workdir='dev/', update=False):
    if filepath is None:
        raise ValueError('filepath must be specified')
    if name is None:
        raise ValueError('name must be specified')
    _, ses = init_db()
    if not check_command_exists(ses, name):
        header= {}
        fp = path.join(workdir, name)
        lines = load_file(filepath)
        header['file_hash'] = hash_content(lines)
        token = gen_token()
        hasht = hash_token(str(token))
        header['token'] = "{}.{}".format(token, hasht)
        with open("{}.lmcommand".format(fp),'w') as f:
            write_header(f, header)
            for line in lines:
                f.write(line)
        add_command(ses, name, str(token), header['file_hash'], path.abspath(fp))




def write_header(f, headers):
    """
    header is dic for write type 'key: value'
    """
    for key, value in headers.items():
        f.write("{}: {}\n".format(key, value))
    f.write("----\n")
    

if __name__ =='__main__':
    _, ses = init_db(echo=False)
    del_all(ses)
    compile(filepath='test', name='test')
    for command in get_all(ses):
        print(command)