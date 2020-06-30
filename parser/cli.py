import click
from lmparser import load_file, separate_headers, header_check, command_traitement
from hash import hash_content, hash_token, gen_token
from db import init_db, get_command, check_command_exists, add_command, get_all, del_all
from os import path
import base64
from tabulate import tabulate


def write_header(f, headers):
    """
    header is dic for write type 'key: value'
    """
    for key, value in headers.items():
        f.write("{}: {}\n".format(key, value))
    f.write("----\n")


@click.group()
def main():
    pass

@main.command()
@click.argument('filepath', type=str)
@click.argument('name', type=str)
@click.option('--workdir', '-wd', default='dev/')
def compile(filepath, name, workdir):
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


@main.command()
@click.argument('script')
def run(script, *args, **kwargs):
    _, session = init_db()
    command_obj = get_command(session,script)
    lines = load_file(command_obj.filepath)
    header, content = separate_headers(lines)
    if header_check(session, header,script, content):
        command_traitement(content,*args, **kwargs)


@main.command()
def list_command():
    dic_command = {}
    _, session = init_db()
    all_name = get_all(session)
    dic_command['name'] = []
    dic_command['filepath'] = []
    for command in all_name:
        dic_command['name'].append(command.command_name)
        dic_command['filepath'].append(command.filepath)

    print(dic_command['name'])
    print(tabulate(dic_command, headers='keys', tablefmt="pretty"))


if __name__ == '__main__':
    main()



