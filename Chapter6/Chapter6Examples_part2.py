Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import temperature
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import temperature
ModuleNotFoundError: No module named 'temperature'
>>> import temperature
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import temperature
ModuleNotFoundError: No module named 'temperature'
>>> import temperature

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    import temperature
ModuleNotFoundError: No module named 'temperature'
>>> echo
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    echo
NameError: name 'echo' is not defined
>>> echo $Pythonpath
SyntaxError: invalid syntax
>>> 
= RESTART: /Users/yhalachev/Desktop/Intro to CS with Python/Chapter 6/temperature.py
>>> import temperature
>>> celsius = tempearature.convert_to_celsius(33.3)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    celsius = tempearature.convert_to_celsius(33.3)
NameError: name 'tempearature' is not defined
>>> celsius = temperature.convert_to_celsius(33.3)
>>> temperature.above_freezing(celsius)
True
>>> restart
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    restart
NameError: name 'restart' is not defined
>>> import exmPLE
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    import exmPLE
ModuleNotFoundError: No module named 'exmPLE'
>>> import example
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    import example
ModuleNotFoundError: No module named 'example'
>>> import importlib
>>> example = importlib.reload(example)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    example = importlib.reload(example)
NameError: name 'example' is not defined
>>> import math
>>> math.pi
3.141592653589793
>>> math.pi = 3
>>> math.pi
3
>>> math = importliib.reload(math)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    math = importliib.reload(math)
NameError: name 'importliib' is not defined
>>> math = importlib.reload(math)
>>> math.pi
3
>>> 
= RESTART: /Users/yhalachev/Desktop/Intro to CS with Python/Chapter 6/experiment.py
The panda's scientific name is 'Ailuropoda melanoleuca'
>>> import experiment
The panda's scientific name is 'Ailuropoda melanoleuca'
>>> 
