import click
from lmparser import load_file, separate_headers, header_check, command_traitement
from dotenv import load_dotenv
from hash import hash_content, hash_token, gen_token
from db import init_db, get_command, check_command_exists, add_command, get_all, del_all, remove_command
import os
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
@click.option('--workdir', '-wd', default='/script/')
def compile(filepath, name, workdir):
    workdir_path  = f"{os.getenv('WORKDIR')}{workdir}"
    if not os.path.exists(workdir_path) or not os.path.isdir(workdir_path):
        os.makedirs(workdir_path)
    if filepath is None:
        raise ValueError('filepath must be specified')
    if name is None:
        raise ValueError('name must be specified')
    _, ses = init_db()
    if not check_command_exists(ses, name):
        header= {}
        fp = os.path.join(workdir_path, name)
        lines = load_file(filepath)
        header['file_hash'] = hash_content(lines)
        token = gen_token()
        hasht = hash_token(str(token))
        header['token'] = "{}.{}".format(token, hasht)
        with open("{}.lmcommand".format(fp),'w') as f:
            write_header(f, header)
            for line in lines:
                f.write(line)
        add_command(ses, name, str(token), header['file_hash'], os.path.abspath(fp))


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

    print(tabulate(dic_command, headers='keys', tablefmt="pretty"))


@main.command()
@click.argument('script')
def remove(script):
    _, session = init_db()
    filepath = get_command(session,script).filepath
    os.remove(os.path.normpath(f"{filepath}.lmcommand"))
    remove_command(session, script)


if __name__ == '__main__':
    load_dotenv()
    main()



