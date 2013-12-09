Commit Bot v0.1
---------------

###A Git Commit Script for automatically adding and committing a git repo


### Dependencies are:
1. Git (duh)
2. Python

### Usage:
```bash
python commit_bot.py <Git Directory> <Commit Message File>
```

Commit Message file needs to have one commit message per line.

If no path to a Commit Message File is specified it will use one of
several predefined commit messages. Inspired by
[xkcd](http://xkcd.com/1296/).

#### NOTE:

This is really horrible practice, and is only really meant as a joke, or
for some silly situation that forces you to attach non-specific commit
messages to your commits. Really no one should ever do this.
