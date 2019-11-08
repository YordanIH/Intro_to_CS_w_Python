Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> 
= RESTART: /Users/yhalachev/Desktop/Intro to CS with Python/Chapter 6/experiment.py
The panda's scientific name is 'Ailuropoda melanoleuca'
>>> import experiment
The panda's scientific name is 'Ailuropoda melanoleuca'
>>> import eperiment
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    import eperiment
ModuleNotFoundError: No module named 'eperiment'
>>> import experiment
>>> 
= RESTART: /Users/yhalachev/Desktop/Intro to CS with Python/Chapter 6/experiment.py
The panda's scientific name is 'Phascolarctos cinereus'
>>> import experiment
The panda's scientific name is 'Phascolarctos cinereus'
>>> print(__name__)
__main__
>>> import echo
__name__ is echo
>>> 
= RESTART: /Users/yhalachev/Desktop/Intro to CS with Python/Chapter 6/import_echo.py
__name__ is echo
After import, __name__ is __main__ and echo.__name__ is echo
>>> 
= RESTART: /Users/yhalachev/Desktop/Intro to CS with Python/Chapter 6/main_example.py
I am the main program.
>>> 
= RESTART: /Users/yhalachev/Desktop/Intro to CS with Python/Chapter 6/temperature_program.py
Enter the temperature in degrees Fahrenheit: 95
It is above freezing. 
>>> 
= RESTART: /Users/yhalachev/Desktop/Intro to CS with Python/Chapter 6/temperature_program.py
Enter the temperature in degrees Fahrenheit: 23
It is below freezing. 
>>> 
= RESTART: /Users/yhalachev/Desktop/Intro to CS with Python/Chapter 6/baking.py
Enter the temperature in degrees Fahrenheit: 500
It is above freezing. 
Enter the baking temperature in degrees Fahrenheit: 500
Preheat ove to 500.0 degrees F (260.0 degrees C).
>>> 
= RESTART: /Users/yhalachev/Desktop/Intro to CS with Python/Chapter 6/baking.py
Traceback (most recent call last):
  File "/Users/yhalachev/Desktop/Intro to CS with Python/Chapter 6/baking.py", line 1, in <module>
    import temperature_program
  File "/Users/yhalachev/Desktop/Intro to CS with Python/Chapter 6/temperature_program.py", line 7
    fahrenheit = float(input("Enter the temperature in degrees Fahrenheit: "))
    ^
IndentationError: expected an indented block
>>> 
= RESTART: /Users/yhalachev/Desktop/Intro to CS with Python/Chapter 6/temperature_program.py
Enter the temperature in degrees Fahrenheit: 500
It is above freezing. 
>>> 
= RESTART: /Users/yhalachev/Desktop/Intro to CS with Python/Chapter 6/baking.py
Enter the baking temperature in degrees Fahrenheit: 500
Preheat ove to 500.0 degrees F (260.0 degrees C).
>>> import doctest
>>> doctest.testmod()
TestResults(failed=0, attempted=0)
>>> 
= RESTART: /Users/yhalachev/Desktop/Intro to CS with Python/Chapter 6/temperature_program.py
Enter the temperature in degrees Fahrenheit: 90
It is above freezing. 
>>> doctest.testmod()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    doctest.testmod()
NameError: name 'doctest' is not defined
>>> import doctest
>>> doctest.testmod()
TestResults(failed=0, attempted=0)
>>> doctest.testmod()
TestResults(failed=0, attempted=0)
>>> 
= RESTART: /Users/yhalachev/Desktop/Intro to CS with Python/Chapter 6/temperature_program.py
Enter the temperature in degrees Fahrenheit: 
Traceback (most recent call last):
  File "/Users/yhalachev/Desktop/Intro to CS with Python/Chapter 6/temperature_program.py", line 8, in <module>
    fahrenheit = float(input("Enter the temperature in degrees Fahrenheit: "))
ValueError: could not convert string to float: ''
>>> doctest.testmod()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    doctest.testmod()
NameError: name 'doctest' is not defined
>>> import doctest
>>> doctest.testmod()
TestResults(failed=0, attempted=0)
>>> import temperature_program
>>> import doctest
>>> doctest.teztmod()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    doctest.teztmod()
AttributeError: module 'doctest' has no attribute 'teztmod'
>>> doctest.testmod()
TestResults(failed=0, attempted=0)
>>> print(__name__)
__main__
>>> import temperature_program
>>> print(__name)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(__name)
NameError: name '__name' is not defined
>>> print(__name__)
__main__
>>> print(temperature_program.__name__)
temperature_program
>>> import imp.reload

Warning (from warnings module):
  File "<pyshell#25>", line 1
DeprecationWarning: the imp module is deprecated in favour of importlib; see the module's documentation for alternative uses
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    import imp.reload
ModuleNotFoundError: No module named 'imp.reload'; 'imp' is not a package
>>> from imp import reload
>>> imp.reload(temperature_program)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    imp.reload(temperature_program)
NameError: name 'imp' is not defined
>>> reload(temperture_program)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    reload(temperture_program)
NameError: name 'temperture_program' is not defined
>>> reload(temperature_program)
<module 'temperature_program' from '/Users/yhalachev/Desktop/Intro to CS with Python/Chapter 6/temperature_program.py'>
>>> import doctest
>>> doctest.testmod()
TestResults(failed=0, attempted=0)
>>> 
