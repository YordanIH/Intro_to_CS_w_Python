Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> species = input("Please enter species: ")
Please enter species: Python curtus
>>> species
'Python curtus'
>>> "Computer' + 'Science'
SyntaxError: EOL while scanning string literal
>>> 'Computer' + 'Science'
'ComputerScience'
>>> 'Computer' + ' Science'
'Computer Science'
>>> 'Darwin\'s'
"Darwin's"
>>> 'H2O' * 3
'H2OH2OH2O'
>>> 'CO2' * 00
''
>>> 'They\'ll hibernate uring the winter.'
"They'll hibernate uring the winter."
>>> '\"Absolutely not,\" he said.'
'"Absolutely not," he said.'
>>> '\"He said,\'Absolutely not,\"\' recalled Mel.'
'"He said,\'Absolutely not,"\' recalled Mel.'
>>> '"He said,'Absolutely not,'" recalled Mel.'
SyntaxError: invalid syntax
>>> '"He said,\'Absolutely not,'"recalled Mel.'
SyntaxError: EOL while scanning string literal
>>> '"He said,\'Absolutely not,\'"recalled Mel.'
'"He said,\'Absolutely not,\'"recalled Mel.'
>>> '\"He said,"\'Absolutely not,'\"recalled Mel.'
SyntaxError: unexpected character after line continuation character
>>> '''" He said, 'Absolutely not,'" recalled Mel.'''
'" He said, \'Absolutely not,\'" recalled Mel.'
>>> '''"He said, 'Absolutely not,'" recalled Mel.'''
'"He said, \'Absolutely not,\'" recalled Mel.'
>>> print('''"He said, 'Absolutely not,'" recalled Mel.''')
"He said, 'Absolutely not,'" recalled Mel.
>>> 'hydrogen sulficde'
'hydrogen sulficde'
>>> 'left\right'
'left\right'
>>> 'left\\rigt'
'left\\rigt'
>>> "left\right"
'left\right'
>>> "left\\right"
'left\\right'
>>> "A\nB\nC"
'A\nB\nC'
>>> 'A\nB\nC'
'A\nB\nC'
>>> 'A/nB/nC'
'A/nB/nC'
>>> 'A\nB\nC'
'A\nB\nC'
>>> print('A\nB\nC')
A
B
C
>>> print('left\right')
leftight
>>> print('left\\right')
left\right
>>> len('')
0
>>> x=3
>>> y=12.5
>>> print('The rabbit is ' + x )
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print('The rabbit is ' + x )
TypeError: can only concatenate str (not "int") to str
>>> rint('The rabbit is ' + str(x))
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    rint('The rabbit is ' + str(x))
NameError: name 'rint' is not defined
>>> print('The rabbit is ' + str(x))
The rabbit is 3
>>> print('The rabbit is ' + str(x) + '.')
The rabbit is 3.
>>> print('The rabbit is ' + str(x) + 'years old.')
The rabbit is 3years old.
>>> print('The rabbit is ' + str(x) + ' years old.')
The rabbit is 3 years old.
>>> print(str(y) + 'is average.')
12.5is average.
>>> print(str(y) + ' is average.')
12.5 is average.
>>> print(str(y) + ' * ' + str(x))
12.5 * 3
>>> print(str(y) + ' * ' + str(x) + ' is ' + str (x*y))
12.5 * 3 is 37.5
>>> first = 'John'
>>> last = 'Doe'
>>> print(last+ ', ' + first)
Doe, John
>>> help input
SyntaxError: invalid syntax
>>> help(input)
Help on built-in function input in module builtins:

input(prompt=None, /)
    Read a string from standard input.  The trailing newline is stripped.
    
    The prompt string, if given, is printed to standard output without a
    trailing newline before reading input.
    
    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
    On *nix systems, readline is used if available.

>>> num=float(input("Please enter number:"))
Please enter number:16
>>> num
16.0
>>> print(num)
16.0
>>> def repeat(s: str,n: int) -> str:
	return s * 3

>>> repeat('yes', 4)
'yesyesyes'
>>> def repeat(s: str,n: int) -> str:
	return s * n

>>> repeat('yes', 4)
'yesyesyesyes'
>>> repeat('no',0)
''
>>> repeat('no',-2)
''
>>> repeat('yesmaybe', 3)
'yesmaybeyesmaybeyesmaybe'
>>> def totla_length(s1: str,s2: str) -> int:
	return len('s1' + 's2')

>>> total_length('yes', 'no')
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    total_length('yes', 'no')
NameError: name 'total_length' is not defined
>>> totla_length('yes','no')
4
>>> totla_length('yes','no')
4
>>> totla_length('yes','')
4
>>> def totla_length(s1: str,s2: str) -> int:
	return len(s1 + s2)

>>> totla_length('yes','no')
5
>>> totla_length('yes','')
3
>>> totla_length('YES!!!!','Noooooo')
14
>>> 
