# PCEP training notes

## While loop
The while loop runs as long as a given condition is true. Using while True creates an infinite loop that runs endlessly until stopped by a break statement or an external interruption. Its main uses include:

    Continuously prompt user input until valid data is entered
    Keep a program running to listen for events or connections
    Retry operations until success
    Always include a break to exit the loop and prevent infinite execution.
    Avoid busy waiting; add delays like time.sleep() to reduce CPU load.
    Prefer clear conditions with regular while loops when possible.
    Use try-except blocks to handle errors gracefully inside the loop.

# IS
Python has an is operator that can
be used in logical expressions
• Implies “is the same as”
• Similar to, but stronger than ==
• is not also is a logical operator

## Try, except, else, finally
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.

## Numbers in Python 3.6
You can now add underscore to numbers for readability
eg. 111_111_111

## Integers: octal and hexadecimal numbers
### Octal
If an integer number is preceded by an 0O or 0o prefix (zero-o), it will be treated as an octal value. This means that the number must contain digits taken from the [0..7] range only.

0o123 is an octal number with a (decimal) value equal to 83.

The print() function does the conversion automatically. Try this:
print(0o123)

### Hexadecimal
The second convention allows us to use hexadecimal numbers. Such numbers should be preceded by the prefix 0x or 0X (zero-x).

0x123 is a hexadecimal number with a (decimal) value equal to 291. The print() function can manage these values too. Try this:
print(0x123)

## Floats
For the exam, don't forget that: you can omit zero when it is the only digit in front of or after the decimal point.
4. or .4 is okay
4. is recognized as 4.0 and .4 as 0.4

4.0 is not the same as 4, in Python. One is a float and the other an integer.

## Scientific notation
3E8 is 3 x 10^8 or 3,00,000,000

The output of 2E2 for instance is a float.
20.0

The exponent (the value after the E) has to be an integer;
the base (the value in front of the E) may be an integer.
Plank's contanst, 10 to the ive 34 written as seen below
6.62607E-34

## Coding floats
Python will choose the most economical form of a number.
eg. print(0.0000000001) is 1e-10

### Uppercase and lowercase doesn't seem to matter
1e10 gives the same value as 1E10

## Strings
Use escape character \ backslash or choose a apostrophe instead of quote
print("to be or not \"to be\"")
to be or not "to be"

## Escape characters
Use of the backslash \
print("I'm Monty Python")
print('I\'m Monty Python')

## String methods
dir will list methods (some, not all) available for a string
stuff = 'hello'
dir(stuff)
[... 'capitalize', 'casefold', 'center', 'count', 'encode',
'endswith', 'expandtabs', 'find', 'format', 'format_map',
'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit',
'isidentifier', 'islower', 'isnumeric', 'isprintable',
'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower',
'lstrip', 'maketrans', 'partition', 'replace', 'rfind',
'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip',
'split', 'splitlines', 'startswith', 'strip', 'swapcase',
'title', 'translate', 'upper', 'zfill']

## Find
word = 'spaceforce'
index = word.find('a')
print(index)
2
Notice the index is displayed and not the character
You get a -1 if the character is not found

It can take as a second argument the index where it should start:
index = word.find('c', 2)
## Stripping whitespace
string = ' marvelous '
x = string.strip()
There is rstrip and lstrip - these will strip from right of left

## Startswith - returns boolen values - is case sensitive too
Use with .lower if you want to remove case sensitivity
string = 'bifurcate'
print(string.startswith("bi))

## Parsing strings
If we just want the domain:
x = ben.jones@nasa.jpl.gov
x.find('@')