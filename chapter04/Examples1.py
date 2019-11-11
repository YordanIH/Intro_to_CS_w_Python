Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> len('Albert Einstaein')
16
>>> len('123!')
4
>>> len(' ')
1
>>> len('')
0
>>> 'Albert' + ' Einstein'
'Albert Einstein'
>>> 'Four score and ' + '7' + "years ago'
SyntaxError: EOL while scanning string literal
>>> 'Four score and ' + '7' + "years ago"
'Four score and 7years ago'
>>> 'Four score and ' + str(7) + 'years ago'
'Four score and 7years ago'
>>> int('0')
0
>>> int(2.3)
2
>>> int(2.7)
2
>>> (int('4') +int('7'))/2
5.5
>>> int('a')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    int('a')
ValueError: invalid literal for int() with base 10: 'a'
>>> AT*6
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    AT*6
NameError: name 'AT' is not defined
>>> 'AT' * 6
'ATATATATATAT'
>>> 4
4
>>> 4
4
>>> 4 * '_'
'____'
>>> 'GC' * -3
''
>>> sequence = 'ATTGTCCCCC'
>>> SEQUENCE
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    SEQUENCE
NameError: name 'SEQUENCE' is not defined
>>> sequence
'ATTGTCCCCC'
>>> len(sequence)
10
>>> new_sequence = sequence + 'afhalkfhlahl'
>>> new_sequence
'ATTGTCCCCCafhalkfhlahl'
>>> new_sequence * 2
'ATTGTCCCCCafhalkfhlahlATTGTCCCCCafhalkfhlahl'
>>> 'that's not going to work'
SyntaxError: invalid syntax
>>> "that's better"
"that's better"
>>> 'She said, "That is better"'
'She said, "That is better"'
>>> 'She said, "That' + "'" + 's hard to read."'
'She said, "That\'s hard to read."'
>>> len('\'')
1
>>> len('it\'s')
4
>>> """multiline string"""
'multiline string'
>>> #multipline
>>> """multiline string"""
'multiline string'
>>> 'one
SyntaxError: EOL while scanning string literal
>>> '''one
two
three'''
'one\ntwo\nthree'
>>> print (1+!)
SyntaxError: invalid syntax
>>> print (1+1)
2
>>> print("The Latin 'Oryctolagus cuniculus' means 'domestic rabit'.")
The Latin 'Oryctolagus cuniculus' means 'domestic rabit'.
>>> print('In 1859, cHARLES dARWIN REVOLUtionized biology')
In 1859, cHARLES dARWIN REVOLUtionized biology
>>> print('and our understanding of ourselves')
and our understanding of ourselves
>>> print('by publishing "On the Origin oF Species".")
      
SyntaxError: EOL while scanning string literal
>>> print('by publishing "On the Origin oF Species".')
by publishing "On the Origin oF Species".
>>> print('one\ttwo\nthree\tfour')
one	two
three	four
>>> numbers='''one
two
three'''
>>> print(numbers)
one
two
three
>>> print(1,2,3)
1 2 3
>>> print()

>>> print(1,'two','three, 4.0)
      
SyntaxError: EOL while scanning string literal
>>> print(1,'two','three',4.0)
1 two three 4.0
>>> radius = 5
>>> printf("The diameter of the circle is", radius * 2, "cm.")
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    printf("The diameter of the circle is", radius * 2, "cm.")
NameError: name 'printf' is not defined
>>> print("The diameter of the circle is", radius * 2, "cm.")
The diameter of the circle is 10 cm.
>>> help print
SyntaxError: invalid syntax
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> print('a','b','c') # The separator is a space by default
a b c
>>> print('a','b','c',sep=', ')
a, b, c
>>> print('a','b','c',sep=', ',end="")
a, b, c
>>> 
>>> print('a','b','c',sep=', ',end='')
a, b, c
>>> print('a','b','c',sep=', ',end='\t')
a, b, c	
>>> print('a','b','c',sep=', ',end='\n\n')
a, b, c

>>> def​ convert_to_celsius(fahrenheit: float) -> float:
 	​""" Return the number of Celsius degrees equivalent to fahrenheit degrees.​
​ 	>>> convert_to_celsius(75)​
	​23.88888888888889​
	​ """​
​ 	
	​​return​ (fahrenheit - 32.0) * 5.0 / 9.0
	
SyntaxError: invalid character in identifier
>>> def​ convert_to_celsius(fahrenheit: float) -> float:
 	​""" Return the number of Celsius degrees equivalent to fahrenheit degrees.​
​ 	>>> convert_to_celsius(75)​
	​23.88888888888889​
	​ """			   				  ​return​ (fahrenheit - 32.0) * 5.0 / 9.0
 	
SyntaxError: invalid character in identifier
>>> def​ convert_to_celsius(fahrenheit: float) -> float:
 	​""" Return the number of Celsius degrees equivalent to fahrenheit degrees.​
​ 	>>> convert_to_celsius(75)​
	​23.88888888888889​
	​ """return​ (fahrenheit - 32.0) * 5.0 / 9.0
 	
SyntaxError: invalid character in identifier
>>> def​ convert_to_celsius(fahrenheit: float) -> float:				​return​ (fahrenheit - 32.0) * 5.0 / 9.0
SyntaxError: invalid character in identifier
>>> def​ convert_to_celsius(fahrenheit: float) -> float:
	
SyntaxError: invalid character in identifier
>>> def	onvert_to_celsius(fahrenheit: float) -> float:
	return (fahrenheit - 32.0) * 5.0 / 9.0

>>> print('80,78.8 and 10.4 degress fahrenheit are equal to ',end='')
80,78.8 and 10.4 degress fahrenheit are equal to 
>>> print(convert_to_celsius(80), end=', \n')
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    print(convert_to_celsius(80), end=', \n')
NameError: name 'convert_to_celsius' is not defined
>>> print(onvert_to_celsius(80), end=', \n')
26.666666666666668, 
>>> print(convert_to_celsius(10.4), end='Celcius.\n')
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    print(convert_to_celsius(10.4), end='Celcius.\n')
NameError: name 'convert_to_celsius' is not defined
>>> print(onvert_to_celsius(10.4), end='Celcius.\n')
-12.0Celcius.
>>> species = input ()
Homo sapiens
>>> spiceis
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    spiceis
NameError: name 'spiceis' is not defined
>>> species
'Homo sapiens'
>>> population = input()
6973738433
>>> population
'6973738433'
>>> id(population	)
140580188794032
>>> type population
SyntaxError: invalid syntax
>>> type(population)
<class 'str'>
>>> population=int(poputlation)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    population=int(poputlation)
NameError: name 'poputlation' is not defined
>>> population=int(population)
>>> population
6973738433
>>> import rlcompleter, readline
readline.parse_and_bind('tab:complete')
SyntaxError: multiple statements found while compiling a single statement
>>> import rlcompleter, readline
>>> readline.parse_and_bind('tab:complete')

>>> help
Type help() for interactive help, or help(object) for help about object.
>>> hwlp
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    hwlp
NameError: name 'hwlp' is not defined
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help()

Welcome to Python 3.8's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.8/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> topics

Here is a list of available topics.  Enter any topic name to get more help.

ASSERTION           DELETION            LOOPING             SHIFTING
ASSIGNMENT          DICTIONARIES        MAPPINGMETHODS      SLICINGS
ATTRIBUTEMETHODS    DICTIONARYLITERALS  MAPPINGS            SPECIALATTRIBUTES
ATTRIBUTES          DYNAMICFEATURES     METHODS             SPECIALIDENTIFIERS
AUGMENTEDASSIGNMENT ELLIPSIS            MODULES             SPECIALMETHODS
BASICMETHODS        EXCEPTIONS          NAMESPACES          STRINGMETHODS
BINARY              EXECUTION           NONE                STRINGS
BITWISE             EXPRESSIONS         NUMBERMETHODS       SUBSCRIPTS
BOOLEAN             FLOAT               NUMBERS             TRACEBACKS
CALLABLEMETHODS     FORMATTING          OBJECTS             TRUTHVALUE
CALLS               FRAMEOBJECTS        OPERATORS           TUPLELITERALS
CLASSES             FRAMES              PACKAGES            TUPLES
CODEOBJECTS         FUNCTIONS           POWER               TYPEOBJECTS
COMPARISON          IDENTIFIERS         PRECEDENCE          TYPES
COMPLEX             IMPORTING           PRIVATENAMES        UNARY
CONDITIONAL         INTEGER             RETURNING           UNICODE
CONTEXTMANAGERS     LISTLITERALS        SCOPING             
CONVERSIONS         LISTS               SEQUENCEMETHODS     
DEBUGGING           LITERALS            SEQUENCES           

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> 
>>> population
6973738433
>>> population = population +1
>>> population
6973738434
>>> population
6973738434
>>> species = input("Please enter a species: ")
Please enter a species: Python curtus
>>> print(spicies)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    print(spicies)
NameError: name 'spicies' is not defined
>>> print(species)
Python curtus
>>> 
