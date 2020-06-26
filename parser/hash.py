from blake3 import blake3
from lmparser import load_file, separate_headers

def hash_content(filename):
    files = load_file(filename)
    _, content = separate_headers(files)
    hashed = ''.join([blake3(bytes(line.strip(), 'utf-8')).hexdigest() for line in content])
    hashed = blake3(bytes(hashed, 'utf-8')).hexdigest()
    return hashed

def hash_token(token):
    return  blake3(bytes(token, 'utf-8')).hexdigest()


hashed = hash_content('test')
print(hashed)