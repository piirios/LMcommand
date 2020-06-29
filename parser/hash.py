from blake3 import blake3
#from lmparser import separate_headers
from os import urandom
import base64
from LMprint import printc

def hash_content(files):
    hashed = ''.join([blake3(bytes(line.strip(), 'utf-8')).hexdigest() for line in files])
    hashed = blake3(bytes(hashed, 'utf-8')).hexdigest()
    return hashed

def hash_token(token):
    if not isinstance(token,bytes):
        token = bytes(token, 'utf-8')
    return blake3(token).hexdigest()

def gen_token(len=16):
    return urandom(len)


def verify_sign(token, token_hash):
    ntk_hash = hash_token(token)
    if ntk_hash == token_hash:
        return True
    else:
        printc('la signature du token de la commande est invalide!', ltype=None, alert='C')
        return False


if __name__ =='__main__':
    hashed = hash_content('test')
    print(hashed)