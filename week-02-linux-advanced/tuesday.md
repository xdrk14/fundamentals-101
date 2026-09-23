Navigation
pwd - print where you are
ls - list what's in this folder 
cd <folder> - move into a folder → cd 
cd .. - move up one folder

Finding programs & processes
which <cmd>- show which program runs for a name
echo $PATH - list folders the shell searches for programs
<cmd> & - run a command in the background
ps - list running processes 
kill <pid> - ask a process to stop, by PID
Text tools
cat <file> - dump the whole file to screen
head / tail - first / last lines of a file 
grep "<word>" <file> - show only matching lines 
sort / uniq - order lines / drop repeats 
find . -name "<pattern>" - search this folder + subfolders 
sed -i 's/<a>/<b>/g' <file> – find-and-replace across a file
awk '{print $<n>}' <file> - print one column of text 

Piping(redirects)
| — send one command's output into the next
> file — save output to a file (overwrite)
>> file — append output to a file
2> file — send only error messages to a file
Environment & exit codes
export <NAME>=<value> — set an environment variable
echo $<NAME> — read a variable back
cmd1 && cmd2 — run cmd2 only if cmd1 succeeded
cmd1 || cmd2 — run cmd2 only if cmd1 failed
Signals
Ctrl+C — "stop now" (can clean up first)
Ctrl+Z — pause the current program
fg — bring a paused program back
kill -9 <pid> — force-quit, no cleanup (last resort)
Scripting
#!/bin/bash — first line: run this file with bash
chmod +x <file> — make a script runnable 
bash <file> — run a script
name="value" — set a variable (no spaces around =)
$1 – 1st argument
$# —count
$@ – all arguments 
if [ <test> ]; then OR fi — run code only if a condition holds
fi has else 
for x in <list>; do end with done — repeat once per item
while <test>; do end with done — repeat while a condition holds 
SSH
ssh <user>@<host> — log in to a remote computer
ssh-keygen -t ed25519 — create a key pair, once
ssh-copy-id <user>@<host> — send your public key to a server 
scp <file> <user>@<host>:<path> — copy a file to/from a server 
tmux
tmux — start a new session 
Ctrl+b d — detach, leave it running 
tmux attach — reattach to a running session 
Ctrl+b c — new window (tab) 
Ctrl+b % — split pane side by side 

