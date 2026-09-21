Variables, are dynamically typed(assigned at runtime)

types:
{
    float :42,4
    int:32
    string:"Examlle"
    bool
    NoneType:True/False
    complex:2+3i
}

type checking
type(<variable>) returns as <class "[variabletype]">
isinstance(<vairable>,<variabletype>) returns true or false\

str()
int()
float(int(<value>)) CAN STACK
bool("")
bool("")
bool("0")

snake_case or variable/functions
PascalCase for classes

a, b = 1, 2
a ,b = b, a (swaping without temp variable)

x = y = z = 0 chained assignment

count += *= 

Divisor //
Modulo %
** Exponent
** unary minus

Literals

print(<variable>,"string","string"+<variable>)
print(f"{<variable>} "string")
input("Input string") - can be cased in any type converter for type checking
 
conditions
if/elif/else

== Equal | != not equal
< > <= >= : Ordering comparisons
and	: True if both operands are true
or	: True if at least one operand is true
not	: Boolean negation

conditions can be chained

ternary(inline)

status = "pass" if score >= 60 else "fail"

(more nesting reduces reliability)

status = "A" if score >= 90 else "B" if score > 75 else "C"

&	AND	
|	OR	
^	XOR	
~	NOT	
<<	Left shift
>>	Right shift	

Loops

for i in range():

fruits = ["apple", "banana", "cherry"]
name = ["hasthi","drug"]
age = [1,2]
for fruit in fruits:
    print(fruit)

for i,fruit in enumerate(fruits):
    print(f"index: {i} fruit: {fruit})

for name,age in zip(name,age):
    print(f"name: {name} age:{2}")

range in for(<starting index>,<ending index>,<interation step>)

for in range(0,31,2) - 31 because it does not include the ending index

while loops

while <condition>:

count = 0
while count <=10 :
    print(count)
    count +=1 


using break,continue

continue - skips the rest of the iteration
exit - exit the loop immmediately


loops nestable

functions,parameters and returning values

def <function name>():
    return - use this to return a value 

to default
parameter -  variable name
argument - value passed into the variable name 

to default a value, create the function with default defined

def multiple(in=0,out=0):
    return in*out

*args - use this to take extra arguments and store as a tuple

**kwards - use this to take extra arguments and store as a dictionary

use / and * to restrict how arguments are passed to a function

recursive is when the function is called by itself

using lambda

is a self contained one time use function, when no logic or extra lines are required 
add = lambda a,b:a+b



lists
one-dim-list = []
two-dim-list = [[],[]]
three-dim-list = [[],[],[]]
lists are mutable

tuple = ()
tuples are immmutable

dictionary ={<key>:<value>}

user = {name:"hasthi", age: 15}
user["role"] = "tech engineer" - add or update a pair 
user.pop ("age") removes whole pair
user.get("age",0) gets value

sets
mutable
a = {1, 2, 3}
b = {2, 3, 4}
a | b     # union: {1, 2, 3, 4}
a & b      # intersection: {2, 3}
a - b       # difference: {1}
a ^ b        # symmetric difference: {1, 4}


string operations
s = "Python Essentials"
s[0] # 'P'
s[-1] # 's' — negative indices count from the end
s[0:6] # 'Python'
s[7:] # 'Essentials'
s[::-1] # 'slaitnessE nohtyP' — reversed
len(s) # 18
"Py" in s # True — membership test

.lower() | .upper()	Case conversion

.title() | .capitalize()	
"the tea" → "The Tea" | "The tea"

.strip() | .lstrip() | .rstrip() Remove whitespace (or given chars) from ends

.split(sep)	String → list of substrings

.join(iterable)	List of strings → single string

.replace(old, new)	Substring substitution

.find(sub) | .index(sub)	Position of substring — find returns -1 if missing

.startswith() | .endswith()	Prefix & suffix test

.isdigit() digit | .isalpha() alphabetic | .isalnum() alphanumeric	Character-class checks
.count(sub)	Occurrences of a substring

\n	Newline
\t	Tab
\\	Literal backslash
\" / \'	Literal quote character


File operations
opening a file modes
r - read
w - creates or overwrites existing file
a - append
x - create only, if already existing, error
r+ - file must  exist

instead of 
file = open()
file = close()

use with file = open()w

consider f as a file
with open("file.txt",w) as f:
    f.write(lines) - writes as is no newlines
with open("file.txt",w) as f:
    f.writelines(lines) - expects and adds newlines 

with open("file.txt",r) as f:
    all whole file  f.read() - reads whole file
with open("file.txt",r) as f:
    line f.readline() - read a single line
with open("file.txt",r) as f:
    all lines f.readlines() - reads all lines()


import os

os.getcwd()                        # current working directory
os.path.exists("file.txt")           # True/False — check before opening
os.path.join("data.txt", "file.txt")        # "data/notes.txt" — builds paths portably across OSes


from pathlib import Path              # modern alternative to os.path
p = Path("data") / "notes.txt"
p.exists()
p.read_text()                              # reads whole file as a string, no "with" needed
p.write_text("Hello\n")                       # writes, creating the file if missing

Exceptions

try,except,else,finally

try:
    result = 0 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except (TypeError, ValueError) as e:     # catch multiple types, capture the exception object
    print(f"Error: {e}")
else:
    print("No exception occurred")            # runs only if try succeeded
finally:
    print("Always runs")                          # runs no matter what — success, failure, or return

common built in exceptions
ZeroDivisionError - Division or modulo by zero
ValueError - Correct type, invalid value — int("abc")
TypeError - Operation applied to an incompatible type
IndexError - Sequence index out of range
KeyError - Dictionary key not found
AttributeError - Attribute/method doesn't exist on the object
FileNotFoundError - File doesn't exist on open()
NameError - Using a name that hasn't been defined

Avoid bare Exception,(catches keyboard intterupt if left undefined)

custom exceptions

raise can be used to raise an error 
def typecheck():
    if isinstance(10,int):
        raise TypeError

try:
    typecheck()
except TypeError:
    print("Type invalid")

use assert to check internal errors(in code)
