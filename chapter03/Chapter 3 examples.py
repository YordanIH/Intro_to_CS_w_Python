Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> abs(-9)
9
>>> abs(3.3)
3.3
>>> day_temp=3
>>> night_temp=10
>>> abs(day_temp-night_temp)
7
>>> abs(-7)+ abs(3.3)
10.3
>>> pow(abs(2),round(4.3))
16
>>> int(34.6)
34
>>> int(-4.3)
-4
>>> float(21)
21.0
>>> help(abs)
Help on built-in function abs in module builtins:

abs(x, /)
    Return the absolute value of the argument.

>>> help(pow)
Help on built-in function pow in module builtins:

pow(base, exp, mod=None)
    Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments
    
    Some types, such as ints, are able to use a more efficient algorithm when
    invoked using the three argument form.

>>> round (3.8)
4
>>> round(-3.8)
-4
>>> int(-3.8)
-3
>>> int(3.8)
3
>>> round(-3.3)
-3
>>> round(-3.5)
-4
>>> help(round)
Help on built-in function round in module builtins:

round(number, ndigits=None)
    Round a number to a given precision in decimal digits.
    
    The return value is an integer if ndigits is omitted or None.  Otherwise
    the return value has the same type as the number.  ndigits may be negative.

>>> round(3.141586286, 2)
3.14
>>> help(round)
Help on built-in function round in module builtins:

round(number, ndigits=None)
    Round a number to a given precision in decimal digits.
    
    The return value is an integer if ndigits is omitted or None.  Otherwise
    the return value has the same type as the number.  ndigits may be negative.

>>> pow(2,3,2)
0
>>> pow(2,4)
16
>>> pow(2.4.3)
SyntaxError: invalid syntax
>>> pow(2.4,3)
13.823999999999998
>>> pow(2,4,3)
1
>>> x=15
>>> id(x)
4379421776
>>> id(-9)
140360339583728
>>> id(23.1)
140359532405232
>>> id(x)
4379421776
>>> shoe_size = 8.5
>>> id(shoe_size)
140359532407024
>>> fahrenheit=77.7
>>> id(fahrenheit)
140359532405232
>>> id(abs)
140360336994608
>>> id(round)
140360336997408
>>> i=3
>>> j=3
>>> k= 4 -1
>>> id(3)
4379421392
>>> id(j)
4379421392
>>> id(k)
4379421392
>>> f=0.0
>>> g=0.0
>>> id(f)
140359800657040
>>> id(g)
140359533011888
>>> convert_to_celsius(212)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    convert_to_celsius(212)
NameError: name 'convert_to_celsius' is not defined
>>> def convert_to_celsius(fahrenheit):
	return(fahrenheit - 32) * 5 / 9
;
SyntaxError: invalid syntax
>>> def convert_to_celsius(fahrenheit):
	return (fahrenheit - 32) * 5 / 9

>>> convert_to_celsius(80)
26.666666666666668
>>> def return(x)
SyntaxError: invalid syntax
>>> def return (x):
	
SyntaxError: invalid syntax
>>> def quadratic(a, b, c, x):
	first = a * x ** 2
	second = b * x
	third = c
	return first + second + third

>>> quadrtic(2, 3, 4, 0.5)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    quadrtic(2, 3, 4, 0.5)
NameError: name 'quadrtic' is not defined
>>> quadratic(2, 3, 4, 0.5)
6.0
>>> quadratic(2, 3, 4, 1.5)
13.0
>>> (-3) ** 2
9
>>> (-3) ** 3
-27
>>> -3 ** 2
-9
>>> first
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    first
NameError: name 'first' is not defined
>>> quadratic(1,2,3)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    quadratic(1,2,3)
TypeError: quadratic() missing 1 required positional argument: 'x'
>>> help(quadratic)
Help on function quadratic in module __main__:

quadratic(a, b, c, x)

>>> def f (x):
	x = 2 * x
	return x

>>> x = 1
>>> x
1
>>> x = f(x + 1) + f (x + 2)
>>> x
10
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











        ​
          
