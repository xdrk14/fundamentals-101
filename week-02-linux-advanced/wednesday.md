
Debugging

Code does what you tell it, not what you expect.
Start with print statements near the problem. Once fixed, turn useful prints into proper logs.
Logging = printing with levels (DEBUG, INFO, WARN, ERROR) that you can filter.
Many tools print more detail with -v or --verbose.
A debugger lets you pause the program and look inside it:
Python: pdb (or breakpoint() in your code)
C, C++, Rust: gdb
Key actions: set breakpoint, step, continue, print a variable, show the call stack
strace shows every system call a program makes (files opened, network, etc.). Linux only.
Memory bugs in C: compile with -fsanitize=address to catch them, or run valgrind.
AI is good at explaining confusing error messages, but always verify its fixes.

Profiling

Measure before optimising.
htop shows CPU and memory per process.
ss -tlnp | grep :8080 finds which process is using a port.
A profiler shows which functions take the most time:
Python: cProfile or py-spy
Linux, any language: perf record, then perf report
hyperfine compares how fast two commands are.


Version Control and Git

Git stores snapshots of your project.
File = blob. 
|-->Folder = tree. 
Snapshot  + message + author plus parent ⇒ commit.
Commits form a graph. Branches split it, merges join it.
Everything is stored by a long ID(Hash). Commits never change; "editing" makes new ones.
Branch names like main are just labels pointing to a commit.
HEAD = where you are right now.
Staging area = the list of changes going into your next commit.

Commands You Actually Need

git init - start a repo
git status - what is going on
git add file - stage changes
git commit -m "message" - save a snapshot
git log --oneline --graph --all - see history
git diff - see unstaged changes
git branch name - create a branch
git switch name - move to a branch
git merge name - merge a branch into the current one
git clone url - download a repo
git pull - get and merge remote changes
git push - upload your commits

Fixing Things

git restore file - throw away changes to a file
git reset file - unstage a file
git commit --amend - fix the last commit
git stash / git stash pop - put work aside and bring it back
git revert commit - undo a commit safely with a new commit

Useful Later

git blame - who changed each line
git bisect - find which commit broke something
git rebase -i - clean up commits before sharing
.gitignore - files Git should skip
Git is the tool; GitHub is a website that hosts Git repos.

Dependencies and Environments

Your code depends on libraries. Those libraries depend on others.
Two projects needing different versions of the same library = conflict.
Fix: one virtual environment per project.
python -m venv venv
source venv/bin/activate
uv is a much faster replacement for pip: uv pip install requests.
Never install packages into your system's own Python.

Packaging

pyproject.toml describes your project: name, version, dependencies.
uv build turns your code into a wheel (.whl) that anyone can install.

Versions

Semantic versioning, MAJOR.MINOR.PATCH:
PATCH = bug fix
MINOR = new feature, nothing breaks
MAJOR = something breaks
Lock file (uv lock) = exact versions of every dependency, so every machine gets the same setup.
Libraries: allow version ranges. Apps: lock exact versions.

Containers

A container packages your app with everything it needs, to ensure consistency.
Lighter than a virtual machine because it shares the host's kernel.
Docker image is a template. Container is a running copy of it.
A Dockerfile lists the steps to build the image.
Docker Compose runs several containers together (e.g. your app plus a database) from one YAML file.
Kubernetes manages huge numbers of containers

Configuration and Secrets

Settings go in environment variables or config files, not in code.
Never commit passwords or API keys to Git.

Publishing

Python packages go on PyPI (practise on TestPyPI first).
GitHub Releases can hold ready-to-download builds.
GitHub Pages hosts simple websites for free.

