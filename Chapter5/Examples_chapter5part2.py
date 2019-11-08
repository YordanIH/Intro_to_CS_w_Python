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
======================== RESTART: Shell =======================
>>> not True
False
>>> not Flase
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    not Flase
NameError: name 'Flase' is not defined
>>> not Glase
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    not Glase
NameError: name 'Glase' is not defined
>>> not False
True
>>> True and True
True
>>> False adn False
SyntaxError: invalid syntax
>>> False and False
False
>>> True and False
False
>>> True and False
False
>>> True or Flase
True
>>> True or Fallse
True
>>> True or False
True
>>> False or False
False
>>> True
True
>>> int(True)
1
>>> int(False)
0
>>> cold = True
>>> windy = False
>>> (not cold) and windyy
False
>>> not (cold and windy)
True
>>> var = 13>17
>>> var
False
>>> var = 17<13
>>> var
False
>>> var = 17>13
>>> var
True
>>> 45>34
True
>>> 45>79
False
>>> 45<79
True
>>> 45<34
False
>>> 32.1>=23
True
>>> 23.1>=23.1
True
>>> 23.1<=23.1
True
>>> 23.1<=23
False
>>> 67.3 == 87
False
>>> 67.3 ==67
False
>>> 67.0 == 67
True
>>> 67.0 !=67
False
>>> 67.0 != 23
True
>>> def is_positive(x: float) -> bool:
	"""Return True if x is positive.


>>> is_positive(3)
True
>>> is_positive(-4.6)
False
"""
	return x > 0

>>> is_positive(3)
True
>>> is_positive(-4.6)
False
>>> is_positive(0)
False
>>> x=2
>>> y=5
>>> z=7
>>> x<y and y<z
True
>>> x = 5
>>> y = 10
>>> z = 20
>>> (x < y) and (y < z)
True
>>> x = 3
>>> (1 < x) and (x <=5)
True
>>> x = 7
>>> (1 < x) and (x <= 5)
False
>>> x = 3
>>> 1 < x <= 5
True
>>> 3 < 5 != True
True
>>> 3 < 5 !=Flase
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    3 < 5 !=Flase
NameError: name 'Flase' is not defined
>>> 3 < 5 !=False
True
>>> not 0
True
>>> no 1
SyntaxError: invalid syntax
>>> not 1
False
>>> not 34.2
False
>>>  not -87
 
SyntaxError: unexpected indent
>>> not -87
False
>>> not ''
True
>>> not 'bad'
False
>>> not None
True
>>> 1 / 0
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    1 / 0
ZeroDivisionError: division by zero
>>> (2<3) or (1 / 0)
True
>>> not 3
False
>>> ( 2 < 3) and (1 / 0)
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    ( 2 < 3) and (1 / 0)
ZeroDivisionError: division by zero
>>> 'A' < 'a'
True
>>> 'A' < 'a'
True
>>> 'A' < 'z'
True
>>> 'abc' < 'abd'
True
>>> 'abc' < 'abcd'
True
>>> 'Jan' in '01 Jan 1838'
True
>>> 'Feb' in '01 Jan 1838'
False
>>> date = input('Enter a date in the format DD MTH YYYY:')
Enter a date in the format DD MTH YYYY:24 Feb 2013
>>> Jan in date
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    Jan in date
NameError: name 'Jan' is not defined
>>> 'Jan' in date
False
>>> 'Feb' in date
True
>>> 'a' in 'abc'
True
>>> 'A' in'abc'
False
>>> '' in 'hph'
True
>>> '' in ''
True
>>> ph = float(input('Enter the pH level: ')))
SyntaxError: unmatched ')'
>>> ph = float(input('Enter the pH level: '))
Enter the pH level: 6.0
>>> if ph < 7.0 :
	print(ph "is aciddic.")
	
SyntaxError: invalid syntax
>>> if ph < 7.0 :
	print(ph, "is aciddic.")

	
6.0 is aciddic.
>>> print(help)
Type help() for interactive help, or help(object) for help about object.
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

>>> ph = float(input('Enter the pH level: '))
Enter the pH level: 8.0
>>> if ph < 7.0:
	print(ph, "is acidic.")

	
>>> if ph < 7.0	print(ph, "is acidic.")
SyntaxError: invalid syntax
>>> if ph < 7.0:print(ph, "is acidic.")

>>> if ph < 7.0:
print(ph, "is acidic.")
SyntaxError: expected an indented block
>>> ph = float(input('Enter the pH level: '))
Enter the pH level: 6.0
>>> if ph < 7.0:
	print(ph, "is acidic. ")
	print("You should be careful with that!")

	
6.0 is acidic. 
You should be careful with that!
>>> ph = float(input('Enter the pH level: '))
Enter the pH level: 8.0
>>> if ph < 7.0:
	print(ph, "is acidic. ")

	
>>> print("You should be careful with that!")
You should be careful with that!
>>> ph = float(input('Enter the pH level: '))
Enter the pH level: 8.0
>>> if ph < 7.0:
	print(ph, "is acidic. ")
print("You should be carefull with that." )
SyntaxError: invalid syntax
>>> ph = float(input('Enter the pH level: '))
Enter the pH level: 8.5
>>> if ph < 7.0:
	print(ph, "is acidic.")

	
>>> if ph > 7.0:
	print(ph,"is basic.")

	
8.5 is basic.
>>> 
