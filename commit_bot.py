from random import choice
import sys
import os

directory = sys.argv[1]

default_commits = []
default_commits.append("Misc Bugfixes")
default_commits.append("Code Additions/Edits")
default_commits.append("More Code")
default_commits.append("Here Have Code")
default_commits.append("AAAAAAAAAA")
default_commits.append("ADKJSLKDFJSDKLFJ")
default_commits.append("My Hands are Typing Words")
default_commits.append("HAAAAAAAAAAAAAAAANDS")

lines = []

if len(sys.argv) > 2:
    text_file = open(sys.argv[2], "r")
    lines = text_file.read().split('\n')
    text_file.close()
else:
    lines = default_commits

line = ''

while line == '':
        line = choice(lines)

commit_command = 'git commit -m \"' + line + '\"'

os.chdir(directory)
os.system('git add .')
os.system(commit_command)
