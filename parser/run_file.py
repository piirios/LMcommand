from lmparser import load_file, separate_headers, header_check, command_traitement
from db import get_command, check_command_exists, init_db, update_command_hash
import click

@click.command()
@click.argument('script', help='the script to execute')
def run(script, *args, **kwargs):
    _, session = init_db()
    command_obj = get_command(session,script)
    lines = load_file(command_obj.filepath)
    header, content = separate_headers(lines)
    if header_check(session, header,script, content):
        command_traitement(content,*args, **kwargs)

if __name__ == '__main__':
    run()