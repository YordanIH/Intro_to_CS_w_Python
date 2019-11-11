Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> min(2,3,4)
2
>>> max(2,-3,4,7,-5)
7
>>> max(2,-3,min(4,7),-5)
4
>>> min(max(3,4),abs(-5))
4
>>> abs(min(4,6,max(2,8)))
4
>>> round(max(5.572,3.258),abs(-2))
5.57
>>> x=7.5
>>> x
7.5
>>> int x
SyntaxError: invalid syntax
>>> x
7.5
>>> int x = 7.5
SyntaxError: invalid syntax
>>> round(7.5)
8
>>> def f(num):
	"""this function will return the parameter trippled"""
	return num*3

>>> f(3)
9
>>> def f1(num1: int, num2: int) ->int:
	"""this function takes only integer vakues and returns the absolute vlaue of the difference between the two parameters"""

	
>>> def f1(num1: int, num2: int) ->int:
	"""this function takes only integer vakues and returns the absolute vlaue of the difference between the two parameters
		and example  is:
		>>>f1(3,5)
		2
"""
	return abs(num1-num2)

>>> f1(3,5)
2
>>> def km_to_mi(km):
""" this function givesthe miles corresponding to kilometers"""
SyntaxError: expected an indented block
>>> def km_to_mi(km):
	""" this function givesthe miles corresponding to kilometers"""
	return 1.6 * km

>>> km_to_mi(20)
32.0
>>> km_to_mi(4)
6.4
>>> 
