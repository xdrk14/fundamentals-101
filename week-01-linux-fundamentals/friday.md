History of Linux
Commands Learnt Today:
echo <text> <if you want to write it into a file, file name> - outputs text from terminal
Note: using “>” operator, output of a command can be stored in a text file
Usage:<Command with a output> > <Name Of New Text File> 
cat <file name> - reads one or many txt files 

Cat > or >> can be used to overwrite or append into a text file from terminal input directly
Args:
-n: Number all output lines, starting from 1.
-b: Number only non-empty output lines.
-s: Squeeze multiple blank lines into one blank line.
-A: Show nonprinting characters, tabs, and line endings.

USE less for longer files
Less Usage
less -N file.txt - open the file numbered
less +G file.txt - open at the end of the file
less +F file.txt - Follow up with new content in the file

date <format> - Date Generator

expr <expression spaced> - Math Operations
Note: is a filename wildcard so to do multiplication \*

figlet <-f followed by font name spaced> <text> - Asci Art Generator

clear - Clears terminal

Ls - lists the folder and files in the current working directory

whoam -i lists the current user

id <root> -un
Note:
Main output UID Group ID Groups this account is a member of
root returns super user
-un returns only username
Pwd - lists current working directory




Cd - change directory

cd . current
cd .. one above
cd ~ root
cd - working

ls <-a to show hidden files,-l moredetails> <-h humanize  output> <-r reverse order> <-t for time> Combinational 

touch - used to create one or many files without overwriting its content if it already exists
Args: 
-a  changes the access time of the file
-m: changes the modified time of the file
-r: is used to give nother file the same access and modification time
-d:-changes access and modification time to a set date      
Usage : “2026-7-3 12:30:34” newfile
<-c> - only updates when the file already exists

file - used to check the real file type (multiple)
Args:
-i: Show MIME-style information.
-b: Use brief mode and omit the filename from the output.
-L: Follow symbolic links and classify their targets.
-z: Try to examine the contents of compressed files.

History
Args:
-w - write to history
-c - Clears History
-d <offset> - deletes at a given offset

Cp - copies files to another file or path
Usage: Cp <file> <file or path>
Args:
-r or -R to copy full directories
-a for backup style copies
Always use -n to avoid a file being overwritten or -i to overwrite with confirmation
-p for preserving
-u to copy only if the directy doesnt exist or is newer
-f to force
-v to show each file after copy

Mv syntax is similar to cp
Mv can be used to rename files or directories
And move files to directions

Mkdir <name of folder>
Args
Using -p missing directories while creating a sub directory can be created to avoid errors
-m set permission(Modes)

rm 
Args
-f to silent run, if missing
-r to remove directories
Combinational
-v for report

Find 
Find <path> <expression>
Args
-name - direct name search
Use iname - for caseless searches
For types only do 
-type -f for files
-d for directories
-size
+ for greater than
- for less than
-print 
-exec to use a commadn for the matches

Help command Usage
help <command>
<command> help

Man <command> - Manual for command

Whatis - one line description of command

Exit 1 and 0 - quit or exit terminal
Logout - logout from a login shell

Can use regex
[] Characters within the brackets
*any characters
? single character
Sudo apt install required for some dependencies(Ex: command: cal) - install command

