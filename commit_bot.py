from random import choice
import sys
import os

directory = sys.argv[1]

text_file = open(sys.argv[2], "r")
lines = text_file.read().split('\n')
text_file.close()

line = ''

while line == '':
        line = choice(lines)

commit_command = 'git commit -m \"' + line + '\"'

os.chdir(directory)
os.system('git add .')
os.system(commit_command)