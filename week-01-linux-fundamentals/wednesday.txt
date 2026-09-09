Ls - l  
Output: drwxr-xr-x

First letter symbolism
- for a regular file 
d for a directory 
l for a symbolic link

In triplets
r grants read permission. 
w grants write permission. 
x grants execute permission. 
- means that permission is absent.
T for sticky bit(useful for shared directories, later sections)

Owner: permissions used when the process's effective user ID matches the file owner. 
Group: permissions used when an applicable process group ID matches the file's group. 
Other: permissions used when neither of the preceding classes matches.

Use chmod to modify permission
usage/args:
u selects the owner class. 
g selects the group class. 
o selects the other class. 
a selects all three classes. 

+ adds permissions,
- removes them, 
and = sets the selected class exactly.

For example, add execute permission for the owner:

$ chmod u+x myfile 

Remove write permission from the group: 

$ chmod g-w myfile 

Add write permission for both the owner and group: 

$ chmod ug+w myfile 

Multiple clauses can be separated with commas. This command sets the owner to read and write, the group to read only, and other to no permissions: 

$ chmod u=rw,g=r,o= myfile

 If the class is omitted, as in chmod +x myfile, the process umask affects which classes are changed. Naming the class explicitly makes the intended result easier to review.

Using octal mod
4 for read 
2 for write 
1 for execute 
0 for no permissions 
(used by adding them)

Owner→Group→Other

Chmod 775 TestDir (7 means r,w,x for Owner,7 means r,w,x for Group,5 means r,x for Other) 

Use sudo chown to change owner of file/folder for user
Use [chgrp <group> / chown :<group> for better control] to change group owner of file/folder for user 

Chown can change both together
Sudo chown <user>:<group> <file/folder>

Maskign and unmasking
in Octal Form
If current process permission bits are 0666
Unmask 0222
Causes the process permission bits to changes to 0644

SetUID is used to run executables with permissions of users(root or other)
Basically set using chmod, rw(s)x or the left most special bit in octal, 
Essentially, when the executable is executed, it will run as that specific user(root or other)

setGID
Used for mainly directories and executables, in directories, any file created or edited inherits the permissions set by the group

Bit notation
If left most special bit is 4 it is SetUID(permission by the created or modifying user) 
else if 2 SetGIB (Permission by the created or modified UserGroup)
Else if 1 it is sticky 

User ID Is the caller for the process
Effective User ID holds the access permission the process currently contains
Saved Set User ID stores EUID for later use, until its needed, example for dong normal tasks it stores later, but when higher privileges are needed , it used the EUID

Sticky bit, used to set permissions to shared directories, normal share directories can be modified even without the user owning it. 
The lowercase “t” in ls-l output is the sticky bit 

Processes
Ps 
PID: process ID 
TTY: controlling terminal, or ? when none is associated 
TIME: accumulated CPU time, not elapsed wall-clock duration 
CMD: command name or command line, depending on the selected format
Ps aux 
Ps -e -f

Use top with ps to watch live view instead of single snapshot

Use tty to check pseudo-terminal associations

Pgrep to get more details on a proces

Kernel manages process details

fork() creates a child procss with new PID

execve calls a process and replaces the process image while retaining the same PID

Ps -o PID,PPID,CMD
PID returns process ID
PPID returns parent process ID
Cmd returns running terminal

wait() used to retrieve child terminations information
Zombie process appear as Z in ps, these a process that no longer executes but stays as a minimal process entry, caused whena child process is no reaped after terminated

Reparenting is when a new parent process or sub reaper is assigned to a child process that already has its parent process terminated

A signal is a messenger that carries events or actions to the process or thread

Process can do default action, use custom action or ignore signals

SIGINT can be blocked and kept until delivery is possible
SIGKILL and SIGSTOP

Kill <PID>(sends SIGTERM by default can be blocked)
-0  error checks without delivering a signal
-KILL for force termination

Nicenessis when a process is favored between -20 to 19
Lower niceness means more weight given
Higher niceness means less weight given

Can view using ni in ps, ps -o ni….

Nice -n <number> <command> can be used to launch with adjusted niceness
Renice -n <number> -p <PID> can be used to adjust existing process Niceness

Process states (ps -o stat)
D - uninterrupted sleep
S - Interruptable sleep
R- already Running or ready to run
T - Means Stopped
Z - Zombie Process

/proc is aa virtual filesystem that tracks process info
Usage ls or findmt /proc/<PID>

Check status /proc/<PID>/status

Packages
Exist in deb(debian based linux) or rpm(fedora etc), content dependencies, name and version, scripts

Package repositories

Sudo apt update, updates local list and any list in that directory on package details and information

Apt looks for signed by for trust

gzip and gunzipis a zipping tool
-k to keep input file

tar -cvf <project name> file1 file2 directory1 
Args
-c creates a new archive. 
-v lists members while processing and(optional).
 -f project.tar names the archive file
-z to compress using gzip

For debian low-level packages are dpkg
For RPM low-level packages are rpm

Search and get info of packages
Debian - Apt [search/show]
RPM - Dnf[search/info]

Installing packages
Debian - Sudo apt install
RPM - Sudo dnf install


Removing packages
Debian - Sudo apt remove
RPM - Sudo dnf remove

Updating on debian 
Sudo apt update
Apt list –upgradable
Sudo apt upgrade

Updating on rpm
Dnf check-update
Dnf upgrade

Yum is compatibility backed by dnf

