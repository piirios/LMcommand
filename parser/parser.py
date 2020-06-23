def load_file(filename):
    with open('{}.lmcommand'.format(filename), 'r') as f:
        lines = f.readlines()

    return lines

def separate_headers(l):
    print(l)
    i = l.index('----\n')
    header = l[:i]
    content = l[i+1:]
    return header, content

def header_check(header):
    token = header[0].split(':')[1].strip()
    filehash = header[1].split(':')[1].strip()
    return token, filehash

def command_traitement(content):
    for command in content:
        command = command.rstrip()
        check_command_variables(command)
        command_list = command.split(' ')
        print(command_list)

def check_command_variables(command):
    if not '{%' in command:
        print('any command in this line')
        return False
    else:
        variable = command.split('{%')[1].split('%}')[0]
        typev, value = variable.split(':')
        print(typev, value)

l = load_file('test')
header, content = separate_headers(l)
creditential = header_check(header)
command_traitement(content)

print(creditential)
