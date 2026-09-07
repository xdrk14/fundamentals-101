Commands:-
Standard code:
0: standard input (stdin) 
1: standard output (stdout) 
2: standard error (stderr)


Can combine all 3 File Input Redirection and File Output Redirection

Stdout
Echo writes its argos to stdout
>is a output redirector
Warn: truncates the file and is recretead if the file already existed
Use for case >> for append

>,>> are standard bash commands
Stdin
< use this for opening the contents of a file and redirect to command output, throws a error if it doesnt exist 

Stderr
Do not use > for redirecting errors, altho it prepares destination file for stdout, the error is still passed onto stderr to shell

Use 2> to redirect diagnostic to destination file

Use &1 to point to same destination along with standard operands

DIrecting stdout and stderr to the same destination
Stdout(>) and Stderr(2>&1) - Use &> as shorter syntax


Redirecting stderr and stdout to duplicates of the same locations
Stderr(2>&1) and Stdout(>)

Redirecting streams to /dev/null (use only for expected or unnecessary outputs)

Pipe- operator | , used to connect command (stdouts or stderrs to to stdins)  

Tee- Used with pipe, used to Write output of connected streams to a text file
Args:
-a if append only

Env
Exists as ${}

Cut - used for splicing
Args:
 -c {[inital position],[final position]}
 -f (default delimiter tab, can be explicitly passed as a argument), can pass argument to  selectign positions position(a number)
 -d used with -f to set a custom delimiter 
 -s use when there is not delimiter to suppress the lines

Paste - used to merge files side by side 
Args: 
 -d: use to choose a delimiter
 -s: joins into one line(serialized)
 Use - at the end of line to read stdin

Head prints by default the firtst 10 line sor all lines if the files is shorter
args
 -n used to specify number lines
 -c used to specify byte count
Can be used with no operand to stdin

Tail used to print by default the last 10 lines or all lines if the files is shorter
Args:
 -n used to specify number lines
 -c used to specify byte count
 If a number is supplied with +{N} with -n it will start at Line N till the end of the file
Use -f to show data as it has been appended to the file

Expand and UNexpand (used to convert between tabs to delimiter)
Args:
 -t used to specify the tab stops
 -a to consider with words

Join used to join two files using a key
Args:
 -1 2 chooses field 2 from file one, and -2 1 chooses field 1 from file   two.

Split used to split the files 
Args
-l for NUmber of max lines per split
Add prefix at the end with -
-b like L, but by Bytes(SIze)

Sort Sorts file content. By default orders lines depending on content in the file
Args:
-r reverse
-n used to sort by number
-k used to sort by field, use -t specify record delimiter(so it doesn’t sort the records too)
-u used to remove duplicates
-o used for safe arrangement with 
Tr used to translate, delete, squeeze characters
Usage
[stdout] | [INPUT SET] [TRANSLATION SET] 
Args:
-d :used to delete needs only one set
-s  :used to squeeze and keep only one instance of character
Preset Classes
[:lower:]: Lowercase letters. 
[:upper:]: Uppercase letters. 
[:digit:]: Digits. 
[:alpha:]: Letters. 
[:alnum:]: Letters and digits. 
[:space:]: Whitespace characters. 
[:punct:]: Punctuation characters. 
Uniq returns one line from consecutive lines
args: 
-c used to add the count 
-d outputs cases of multiple lines
-q outputs cases of only one line
Note: checks happen only with neighbouring values, so use sort if its mixed
Wc is used to count properties of a file
Args:
-l: Count newline characters. 
-w: Count words.
 -c: Count bytes. 
-m: Count characters
Nl returns lines numbered ignoring space lines
Args:
-na use to number of lines
Grep - Find matching lines in a file
Args
-F to check for string expressions
-E for Extened regular expresionms with +.|,- etc
-i: Ignore case distinctions. 
-n: Prefix selected lines with line numbers.
 -v: Select lines that do not match. 
-c: Print the count of selected lines for each input file. 
-o: Print only each nonempty matching part rather than the full selected line.
-r search readable files only


