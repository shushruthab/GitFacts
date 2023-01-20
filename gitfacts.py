import os
import subprocess
import shlex
from datetime import datetime, timedelta
from dateutil import parser, tz


def git_facts(git_dir):
    # Change the working directory to <git_dir>
    os.chdir(git_dir)
    items = []
    # Active branch
    # git rev-parse --abbrev-ref HEAD command returns the name of the branch that the current HEAD is pointing to. git rev-parse is used to extract information from git objects and HEAD is the reference to the current commit on the current branch.
    # .decode('utf-8') is used to convert the output of command from bytes to string
    
    try:
        branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).decode('utf-8').strip()
        item = f"Active branch: {branch}"
        items.append(item)
        print("Active branch: ", branch)

        #whether repository files have been modified
        status = subprocess.check_output(shlex.split(f'git log -1 --pretty=format:"%ad"')).decode('utf-8').strip()
        if status:
            items.append("Local changes: True")
            print("Local changes: True")
        else:
            items.append("Local changes: False")
            print("Local changes: False")

        #whether the current head commit was authored in the last week
        author_date = subprocess.check_output(['git', 'log', '-1', '--pretty=format:"%ad"']).decode('utf-8').strip()
        
        author_date = author_date.strip('"')
        author_date = parser.parse(author_date)  
        now = datetime.now().replace(microsecond=0, tzinfo=tz.tzlocal())
        
        if (now - author_date) <= timedelta(days=7):
            items.append("recent commit: True")
            print("recent commit: True")
        else:
            items.append("recent commit: False")
            print("recent commit: False")

        #whether the current head commit was authored by Rufus
        author_name = subprocess.check_output(['git', 'log', '-1', '--pretty=format:"%an"']).decode('utf-8').strip()
        if author_name == 'Rufus':
            items.append("blame Rufus: True")
            print("blame Rufus: True")
        else:
            items.append("blame Rufus: False")
            print("blame Rufus: False")

    except:
        print("Not a git repository")

    return items

# git_dir = input("Enter git repository directory: ")
# git_facts(git_dir)
