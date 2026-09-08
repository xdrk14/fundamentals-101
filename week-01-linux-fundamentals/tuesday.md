Regex

Use * for repeating characters – usage ab* accepts: ab,abb,abbb….
^ - Forces to search at the beginning of a line ^[A-Z]
$ - Forces to search at the end of a line - [A-Z]$ 
. - Allows one single character, along with anther differen character follwing it
[ ]- Sets, used to check if either are present, if ^used after [, the set is negated(anything included cannot be present in the line)
Note: Use Grep -E to support the characters///
+: One or more repetitions. 
?: Zero or one repetition. 
|: Either the expression on the left or the right. 
(...): Group expressions.

VIM
Search/Find
Open im using vim <filename>
:q! To quit with unsaved changes
/ starts a forward search
? starts a backward search
Use n to repeat the search in the same direction or N to repeat in the opposite direction
Use *(forward) #(backward) to search for the word under the cursor
:set ignorecase makes searches ignore case. 
:set smartcase makes an uppercase character restore case sensitivity when ignorecase is also set. 
\c inside a pattern forces that search to ignore case. 
\C forces that search to respect case.

Navigation
h: Move one character left. 
j: Move one screen line down. 
k: Move one screen line up. 
l: Move one character right.
w: Move to the beginning of the next word. 
b: Move to the beginning of the current or previous word. 
e: Move to the end of the current or next word.
0: Move to column zero. 
^: Move to the first nonblank character. 
$: Move to the end of the line.
gg: Move to the first line. 
G: Move to the final line. 
42G: Move to line 42. 
Ctrl+F: Move forward approximately one screen.
Ctrl+B: Move backward approximately one screen.
Modifying
i: Enter Insert mode before the cursor. 
a: Enter Insert mode after the cursor.
I: Enter Insert mode before the first nonblank character. 
A: Enter Insert mode at the end of the line.
o: Open a new line below the current line and enter Insert mode. O: Open a new line above the current line and enter Insert mode.
d: Delete text. 
c: Change text, then enter Insert mode. 
y: Yank, or copy, text. 
x: Delete the character under the cursor. 
dd: Delete the current line linewise. 
3dd: Delete three lines starting with the current line. 
cc: Change the current line and enter Insert mode. 
r{char}: Replace the character under the cursor with 
{char}. R: Enter Replace mode until Esc is pressed.
ce: Change through the end of the word. 
c$: Change through the end of the line. 
cc: Change the complete current line. 
ciw: Change the inner word under the cursor. 
caw: Change a word text object, including surrounding spacing as Vim defines it.
yw: Yank through a word motion. 
yy: Yank the current line. 
p: Put after the cursor for characterwise text or below the current line for linewise text. 
P: Put before the cursor or above the current line.
u: Undo the most recent change. 
Ctrl+R: Redo an undone change. 

Save/Exit
Use :w to write the current buffer to its associated file without closing the window:
:saveas copy.txt
:q to quit without committing changes to the current buffer
:wq -writing and quiting 
:x or ZZ Write if modified and quit

EMACS

Terminal did not recognize , use sudo dnf install emacs

Emacs (for GUI)
Emacs -nw for no GUI

Emacs <filename or path>

A buffer holds text or other editor state. A visited file's content lives in a buffer. 
A window is an area within an Emacs frame that displays a buffer. 
A frame is a top-level Emacs display, such as a graphical frame or terminal frame.

C-x C-f Find File


Saving

C-x C-s Save file
C-x C-w to write under a new name(Save As)
C-x s Save some buffers

Navigation
C-x b to switch buffers
C-x [2,3] to multiple window(2-3)
C-x o to select next window

C-x 0 to delete selected window
C-x 1 to delete the other windows in the current frame

C-x k to kill a buffer

C-f: Move forward one character. 
C-b: Move backward one character. 
C-n: Move to the next line. 
C-p: Move to the previous line. 
C-a: Move to the beginning of the line. 
C-e: Move to the end of the line.
M-f: Move forward one word. 
M-b: Move backward one word. 
M-<: Move to the beginning of the buffer. 
M->: Move to the end of the buffer.


C-w: Kill the active region, removing it and adding it to the kill ring. M-w: Copy the active region to the kill ring without removing it. 
C-k: Kill from point to the end of the line; repeated use can include the newline.

C-x C-x Save-buffers-kill-terminal 
C-g cancel pending command
C/ Undo Mac changes

Users and Groups
Users have a Unique ID UUID
Groups have a Unique ID GID

Root has UUID 0

Su starts the terminal with a diff identity(default root)
Su - [Name]

Sudo (same default is root)
Args -u, used to use another identity(user)
          -l used for checking permission and policies for current account

/etc/passwd
Cat /etc/passwd reads only local file of passwords

getent passwd - get password
getent passwd root - get password of root user
Output Format

Login name: The human-readable account name, such as root.
Password field: Usually x on a shadow-password system, indicating protected password data is stored separately. 
UID: The numeric user identity. UID 0 has traditional superuser treatment. 
Primary GID: The numeric ID of the account's primary group.
GECOS/comment: Descriptive account information, often internally comma-separated. 
Home directory: The path used as the account's home setting; it may be absent on disk. 
Login shell/program: The program requested for applicable login sessions, such as /bin/bash or a non-login program.

/etc/shadow

Output Forma
Login name.
Password hash or special password marker. 
Last password change, in days since 1970-01-01; 0 requests a change at the next password-authenticated login in typical tooling.
Minimum password age, in days. 
Maximum password age, in days. 
Warning period before password expiration, in days. 
Inactivity period after password expiration, in days. 
Account expiration date, in days since 1970-01-01. Reserved field.

Sudo passwd -S - shows account status
Sudo chage -l -Displays password aging fields

/etc/group
getent group 
getent group developers 

Output Format 
Group name: developers. 
Password field: Commonly x, *, or another placeholder; protected group-password data can be stored in /etc/gshadow. 
GID: The numeric group identity, 1500 here. 
Member list: Comma-separated explicit member names, alice and bob here.

Use these to inspect a user’s group
id alice
groups alice

User Management
$ sudo useradd -m -s /bin/bash -c "Bob Example" bob
Args
-m requests creation of a home directory for the account

-s (shell setting) /bin/bash, set as bash

-c used as a descriptive comment followed by comment

Username of account

Getent passwd bob - Retrieves password information via NSS

Passwd -S bob
Checks authentication/password status
L is Locked
P is password active
NP is no Password

Usermod
Args
-s used to change shell /bin/zsh 
-d specifies the new home directory for the user and moves only the home 
Use -m(moves the rest of the files , settings etc) with -d to move home directory inline 
-aG adds the user to groups

Sudo passwd [-l/-u]
Locking accounts is passwd -l 
Unlocking accounts password -u 

Userdel 
args -r to remove with home directory

Group Management
groupadd makes a new grp
groupdel deletes 
groupmod -n <old name> <new name>

Getent <groupname> - List all grp
Group <username> - Groups belonging to a user

gpasswd -d bob developers - Remove user form a group using g pass

