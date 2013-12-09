Commit Bot v0.1
===============

A Git Commit Script for automatically adding and committing a git repo
----------------------------------------------------------------------

### Dependencies are:
1. Git (duh)
2. Python

### Usage:
```bash
python commit_bot.py <Git Directory> <Commit Message File>
```

Commit Message file needs to have one commit message per line.

If no path to a Commit Message File is specified it will attempt to look
for a 'commit_messages.txt' file located in the same directory where it
is committing.
