git --version or -v
git --help or -h

check git identity
git config --global --list

git config --global user.name "Xdrk14"
git config --global -.name "xdrk14@gmail.com"

git init :Start a new repository to enable versioning
git add	:Group related changes in the staging area, ready to commit
git commit	:Save the staged changes to history, with a commit message (a short description)
git status	:Show the state of the working directory and staging area
git checkout	:Change the working directory to a different version from history
git log	Detailed history
git log --oneline	One commit per line, less detail
git log --graph	Visual diagram, useful for diverging paths
git checkout <id>	Moves to another point in history (changes files in your working directory)

use 
git config --global color.diff.old red
git config --global color.diff.new green


git diff	Working directory ↔ staging area
git diff --staged	Staging area ↔ previous commit
git diff HEAD~1	Current commit ↔ the one before it

git branch my-new-feature	Start a branch from the current branch
git checkout my-new-feature	Switch the working directory to that branch
git merge	Apply one branch's commits onto another (default: fast-forward)

Clone	Copy a repository to your local machine
Branch & develop	Build features on branches
Push	Publish your changes to a remote repository others can access
Pull	Others who like your changes merge them into their copy
Pull request	You proactively ask another developer to integrate your changes


Unordered (bulleted)	- Item / * Item / + Item	One item per line
Ordered (numbered)	1. Step	Any number works; Markdown counts automatically, so 1. on every line renders 1, 2, 3
Task (checkbox)	- [ ] To do / - [x] Done	The empty brackets need a space inside


Code block
Three backticks ``` above and below the code (not three apostrophes ''').
Syntax highlighting
Put the language name after the opening backticks: ```bash, ```js, and many more.

![alt text](url). The URL can be relative (a file in the repository) or absolute (anywhere online). The alt text displays if the image fails to load and is read aloud by screen readers. Markdown cannot set image size.
HTML image
<img> gives more control: alt (alternative text), src (source URL), width/height (pixels), align (left or right).

merge conflicts- when two of the same parts of the same file are changed in two different branches

Conversation	Activity log, plus open space for ideas, suggestions and feedback
Commits	Only the commits unique to the proposed branch
Checks	Results of GitHub Actions automations on the PR
Files changed	Before/after diff view, with in-context comments and reviews
Tip

Assignee
The person (or people) most familiar with the proposed changes: a simple way to know whom to contact with questions. Distinct from a reviewer, who gives feedback.


Comment	General feedback, neither approving nor rejecting
Approve	Permits merging where rulesets, code owners or other policies require approval
Request changes	The work does not yet meet expectations; re-request a review after fixing


Suggested change
For small fixes (typos, rewording) that are easier to make than describe. The Add a suggestion button in the comment editor inserts a special ```suggestion block; GitHub then shows the author a Commit suggestion button to accept it in one click, with no code editor needed.