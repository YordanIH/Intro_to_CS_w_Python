Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: /Users/yhalachev/Desktop/Intro to CS with Python/Chapter 6/temperature_program.py
Enter the temperature in degrees Fahrenheit: 500
It is above freezing. 
>>> import doctest
>>> doctest.testmod()
**********************************************************************
File "/Users/yhalachev/Desktop/Intro to CS with Python/Chapter 6/temperature_program.py", line 3, in __main__.convert_to_celsius
Failed example:
    convert_to_celsius(75)
Expected:
     23.88888888888889
Got:
    57.22222222222222
**********************************************************************
1 items had failures:
   1 of   1 in __main__.convert_to_celsius
***Test Failed*** 1 failures.
TestResults(failed=1, attempted=1)
>>> clear
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> restart
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    restart
NameError: name 'restart' is not defined
>>> 
============================ RESTART: Shell ===========================
>>> 
============================ RESTART: Shell ===========================
>>> import math
>>> dir(msth)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    dir(msth)
NameError: name 'msth' is not defined
>>> dir(math)
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
>>> help(floor)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    help(floor)
NameError: name 'floor' is not defined
>>> help(math(floor))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    help(math(floor))
NameError: name 'floor' is not defined
>>> help(math.floor)
Help on built-in function floor in module math:

floor(x, /)
    Return the floor of x as an Integral.
    
    This is the largest integer <= x.

>>> math.floor(-2.8)
-3
>>> abs(round(-4.3))
4
>>> help(math.ceil)
Help on built-in function ceil in module math:

ceil(x, /)
    Return the ceiling of x as an Integral.
    
    This is the smallest integer >= x.

>>> help(math.sine)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    help(math.sine)
AttributeError: module 'math' has no attribute 'sine'
>>> help(math.sin)
Help on built-in function sin in module math:

sin(x, /)
    Return the sine of x (measured in radians).

>>> dir(math)
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
>>> math.ceil(sin(34.5))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    math.ceil(sin(34.5))
NameError: name 'sin' is not defined
>>> math.ceil(math.sin(34.5))
1
>>> import calendar
>>> print(__name__)
__main__
>>> help(calendar.isleap)
Help on function isleap in module calendar:

isleap(year)
    Return True for leap years, False for non-leap years.

>>> calendar.isleap()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    calendar.isleap()
TypeError: isleap() missing 1 required positional argument: 'year'
>>> calendar.isleap(2019)
False
>>> calendar.isleap(2020)
True
>>> dir(calendar)
['Calendar', 'EPOCH', 'FRIDAY', 'February', 'HTMLCalendar', 'IllegalMonthError', 'IllegalWeekdayError', 'January', 'LocaleHTMLCalendar', 'LocaleTextCalendar', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'TextCalendar', 'WEDNESDAY', '_EPOCH_ORD', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_colwidth', '_locale', '_localized_day', '_localized_month', '_monthlen', '_nextmonth', '_prevmonth', '_spacing', 'c', 'calendar', 'datetime', 'day_abbr', 'day_name', 'different_locale', 'error', 'firstweekday', 'format', 'formatstring', 'isleap', 'leapdays', 'main', 'mdays', 'month', 'month_abbr', 'month_name', 'monthcalendar', 'monthrange', 'prcal', 'prmonth', 'prweek', 'repeat', 'setfirstweekday', 'sys', 'timegm', 'week', 'weekday', 'weekheader']
>>> help(calendar.leapdays)
Help on function leapdays in module calendar:

leapdays(y1, y2)
    Return number of leap years in range [y1, y2).
    Assume y1 <= y2.

>>> calendar.leapdays[2020,22050]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    calendar.leapdays[2020,22050]
TypeError: 'function' object is not subscriptable
>>> calendar.leapdays[2020,2050]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    calendar.leapdays[2020,2050]
TypeError: 'function' object is not subscriptable
>>> calendar.leapdays[2020, 2050)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> calendar.leapdays[2020, 2050]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    calendar.leapdays[2020, 2050]
TypeError: 'function' object is not subscriptable
>>> calendar.leapdays(2020, 2050)
8
>>> help(calendar.weekday)
Help on function weekday in module calendar:

weekday(year, month, day)
    Return weekday (0-6 ~ Mon-Sun) for year, month (1-12), day (1-31).

>>> calendar.weekday(2016, 7, 29)
4
>>> 
