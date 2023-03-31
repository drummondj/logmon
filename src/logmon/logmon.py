import click
import os
import re

def find_log_files(dir):
    file_list = []
    for root, dirs, files in os.walk(dir):
        for fn in files:
            if re.match('.*\.log.*', fn):
                file_list.append(os.path.join(root,fn))
    return file_list

@click.command()
@click.argument('dir')
@click.option('--email', help='The email address to send errors to')
def logmon(dir):
    """Monitor the log files contained in the specified dir and email if an error is found"""
    file_list = find_log_files(dir)

if __name__ == '__main__':
    logmon()
