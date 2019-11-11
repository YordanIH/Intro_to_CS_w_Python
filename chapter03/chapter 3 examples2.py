Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def get_weekday(current_weekday: int,days_ahead: int) ->int:
          ​​"""Return which day of the week it will be days_ahead days from​
​ 	​  current_weekday.​
​ 	
​ 	​  current_weekday is the current day of the week and is in the​
​ 	​  range 1-7, indicating whether today is Sunday (1), Monday (2),​
​ 	​  ..., Saturday (7).​
​ 	​  days_ahead is the number of days after today.​
​ 	​  >>> get_weekday(3, 1)​
​ 	​  4​
​ 	​  >>> get_weekday(6, 1)​
​ 	​  7​
​ 	​  >>> get_weekday(7, 1)​
​ 	​  1​
​ 	​   >>> get_weekday(1, 0)​
​ 	​   1​
​ 	​    >>> get_weekday(4, 7)​
​ 	​    4​
​ 	​    >>> get_weekday(7, 72)​
​ 	​    2​​ 	​    """

        return current_weekday + days_ahead % 7
SyntaxError: invalid character in identifier
>>> def get_weekday(current_weekday: int,days_ahead: int) ->int:
	return current_weekday + days_ahead % 7

>>> get_weekday(3,1)
4
>>> get_weekday(6,1)
7
>>> get_weekday(7,1)
8
>>> def get_weekday(current_weekday: int,days_ahead: int) ->int:
	return current_weekday + days_ahead % 7

>>> get_weekday(7, 1)
8
>>> def get_weekday(current_weekday: int,days_ahead: int) ->int:
	return (current_weekday + days_ahead) % 7

>>> get_weekday(7, 1)
1
>>> get_weekday(6,1)
0
>>> def get_weekday(current_weekday: int,days_ahead: int) ->int:
	return (current_weekday + days_ahead - 1 ) % 7 +1

>>> get_weekday	(3, 1)
4
>>> get_weekday (6, 1)
7
>>> get_weekday (7, 1)
1
>>> get_weekday (1, 0)
1
>>> get_weekday (4, 7)
4
>>> get_weekday (7, 72)
2
>>> def get_birthday_weekday(current_weekday: int, current_day: int,
			 birthday_day: int) _> int:
	
SyntaxError: invalid syntax
>>> def get_birthday_weekday(current_weekday: int, current_day: int,
			 birthday_day: int) ->int:
     ​   ​"""Return the day of the week it will be on birthday_day,​
​ 	​...     given that the day of the week is current_weekday and the​
​ 	​...     day of the year is current_day.​
​ 	​...​”"""
     
SyntaxError: invalid character in identifier
>>> def get_birthday_weekday(current_weekday: int, current_day: int,
			 birthday_day: int) ->int:
     ​   """Return the day of the week it will be on birthday_day,​
​ 	​...     given that the day of the week is current_weekday and the​
​ 	​...     day of the year is current_day.​
​ 	​...​”"""
     
SyntaxError: invalid character in identifier
>>> def get_birthday_weekday(current_weekday: int, current_day: int,
			 birthday_day: int) ->int:
	days_diff = days_difference(current_day, birthday_day)
	return get_weekday(current_weekday, days_diff)

>>> get_birthday_weekday(5, 3, 4)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    get_birthday_weekday(5, 3, 4)
  File "<pyshell#34>", line 3, in get_birthday_weekday
    days_diff = days_difference(current_day, birthday_day)
NameError: name 'days_difference' is not defined
>>> def days_difference(current_day: int, birthday_day: int) ->int:
	return mod(birthday_day - current_day)

>>> days_difference(4, 5)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    days_difference(4, 5)
  File "<pyshell#38>", line 2, in days_difference
    return mod(birthday_day - current_day)
NameError: name 'mod' is not defined
>>> def days_difference(current_day: int, birthday_day: int) ->int:
	return birthday_day - current_day

>>> get_birthday_weekday(5, 3, 4)
6
>>> get_birthday_weekday(5,3, 116)
6
>>> get_birthday_weekday(6, 116, 3
		     )
5
>>> get_birthday_weekday(2,116,3)
1
>>> 
= RESTART: /Users/yhalachev/Desktop/Intro to CS with Python/Chapter 3 Excercises/writting a py script.py
>>> 
= RESTART: /Users/yhalachev/Desktop/Intro to CS with Python/Chapter 3 Excercises/writting a py script.py
>>> 
= RESTART: /Users/yhalachev/Desktop/Intro to CS with Python/Chapter 3 Excercises/writting a py script.py
26.666666666666668
26.0
-12.0
>>> def f(x):
	x = 2 * X

	
>>> res= f(3)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    res= f(3)
  File "<pyshell#50>", line 2, in f
    x = 2 * X
NameError: name 'X' is not defined
>>> ef f(x):
	x = 2 * x
	
SyntaxError: invalid syntax
>>> res = f(3)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    res = f(3)
  File "<pyshell#50>", line 2, in f
    x = 2 * X
NameError: name 'X' is not defined
>>> def f(x):
	x = 2 * x

	
>>> res = f(3)
>>> res
>>> print(re)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    print(re)
NameError: name 're' is not defined
>>> t
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    t
NameError: name 't' is not defined
>>> print(res)
None
>>> id(res)
4530011744
>>> def f(x):
	x = 2 * x
	return None

>>> print(f(3))
None
>>> def pie_percent(n: int) -> int:
	return int(100 / n)

>>> pie_percent	(3)
33
>>> pie_percent(0)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    pie_percent(0)
  File "<pyshell#68>", line 2, in pie_percent
    return int(100 / n)
ZeroDivisionError: division by zero
>>> 
