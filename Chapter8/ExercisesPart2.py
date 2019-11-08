Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> alkaline_earth_metals = ['beryllium','cccccckvuiuecjtrirjffucicuikdtjvgjlhbeherhcumagnesium' ]
>>> alkaline_earth_metals = [4,12,20,38,56,88 ]
>>> alkaline_earth_metals
[4, 12, 20, 38, 56, 88]
>>> alkaline_earth_metals.intex(88)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    alkaline_earth_metals.intex(88)
AttributeError: 'list' object has no attribute 'intex'
>>> alkaline_earth_metals.intex('88')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    alkaline_earth_metals.intex('88')
AttributeError: 'list' object has no attribute 'intex'
>>> alkaline_earth_metals.index(88)
5
>>> alkaline_earth_metals.index(88,reverse=True)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    alkaline_earth_metals.index(88,reverse=True)
TypeError: index() takes no keyword arguments
>>> alkaline_earth_metals[-1]
88
>>> alkaline_earth_metals.[5]
SyntaxError: invalid syntax
>>> alkaline_earth_metals[5]
88
>>> len(alkaline_earth_metals)
6
>>> max(alkaline_earth_metals)
88
>>> temps = [25.2,16.8,31.4,23.9,28,22.5,19.6]
>>> temps
[25.2, 16.8, 31.4, 23.9, 28, 22.5, 19.6]
>>> tmps.sort
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    tmps.sort
NameError: name 'tmps' is not defined
>>> temps.sort
<built-in method sort of list object at 0x7fa1f004ac40>
(
>>> )
>>> 
>>> temps.sort()
>>> temps
[16.8, 19.6, 22.5, 23.9, 25.2, 28, 31.4]
>>> cool_temps = temps[:2]
>>> warm_temps = temps[2:]
>>> temps
[16.8, 19.6, 22.5, 23.9, 25.2, 28, 31.4]
>>> cool_temps
[16.8, 19.6]
>>> warm_temps
[22.5, 23.9, 25.2, 28, 31.4]
>>> temps_in_celsius = cool_temps.extend(warm_temps)
>>> temps_in_celsius
>>> temps_in_celsius
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> cool_temps
[16.8, 19.6, 22.5, 23.9, 25.2, 28, 31.4]
>>> temps_in_celsius=cool_temps[:]
>>> temps_in_celsius
[16.8, 19.6, 22.5, 23.9, 25.2, 28, 31.4]
>>> test = cool_temps.extend(warm_temps)[]
SyntaxError: invalid syntax
>>> cool_temps = temps[:2]
>>> warm_temps = temps[2:]
>>> temps_in_celsius = cool_temps
>>> temps_in_celsius
[16.8, 19.6]
>>> temps_in_celsius = cool_temps +warm_temps
>>> temps_in_celsius
[16.8, 19.6, 22.5, 23.9, 25.2, 28, 31.4]
>>> 
>>> def same_first_last(L: list) -> bool
SyntaxError: invalid syntax
>>> def same_first_last(L: list) -> bool:
	"""Preconditions:len(L) >=2
Return True if and only if the first item of the list is the same as the last.

	>>> same_first_last([3,4,2,8,3])
	True
	>>> same_first_lsst('apple','banana','pear'])
	False
	>>> same_first_last([4.0, 4.5])
	False
	"""

	
>>> def same_first_last(L: list) -> bool:
	"""Preconditions:len(L) >=2
Return True if and only if the first item of the list is the same as the last.

	>>> same_first_last([3,4,2,8,3])
	True
	>>> same_first_lsst('apple','banana','pear'])
	False
	>>> same_first_last([4.0, 4.5])
	False
	"""
	return L[0]==L[-1]

>>> same_first_last([3,4,2,8,3])
True
>>> same_first_lsst('apple','banana','pear'])
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> same_first_lsst(['apple','banana','pear'])
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    same_first_lsst(['apple','banana','pear'])
NameError: name 'same_first_lsst' is not defined
>>> same_first_last(['apple','banana','pear'])
False
>>> same_first_last(['apple','banana','pear','apple'])
True
>>> def same_first_last(L: list) -> bool:
	"""Preconditions:len(L) >=2
Return True if and only if the first item of the list is the same as the last.

	>>> same_first_last([3,4,2,8,3])
	True
	>>> same_first_lsst('apple','banana','pear'])
	False
	>>> same_first_last([4.0, 4.5])
	False
	"""
	return L[0]==L[-1]
KeyboardInterrupt
>>> same_first_last([4.0, 4.5])
False
>>> same_first_last([4.0, 4.5, 4.0])
True
>>> def is_longer(L1: list,L2: list) ->bool:
	"""Return True if and only if the lenght of L1 is longer that the length of L2.
>>> is_longer([1, 2, 3], [4, 5])
​True​
>>> is_longer(['abcdef'], ['ab', 'cd', 'ef'])​
False

​>>> is_longer(['a', 'b', 'c'], [1, 2, 3]​
False

"""
	return len(L1)>len(L2)

>>> 
>>> is_longer([1, 2, 3], [4, 5])
True
>>> is_longer(['abcdef'], ['ab', 'cd', 'ef'])
False
>>> is_longer(['a', 'b', 'c'], [1, 2, 3])
False
>>> values = [0,1,2]
>>> values[1] = values
>>> values
[0, [...], 2]
>>> print(values)
[0, [...], 2]
>>> values[1]
[0, [...], 2]
>>> units = [['km','miles','league'],['kg','pound','stone']]
>>> units[0]
['km', 'miles', 'league']
>>> units[-1]
['kg', 'pound', 'stone']
>>> units[0][0]
'km'
>>> units[1][0]
'kg'
>>> units[0][1:3]
['miles', 'league']
>>> units[1][0:2]
['kg', 'pound']
>>> units[-2]
['km', 'miles', 'league']
>>> units[1]
['kg', 'pound', 'stone']
>>> units[-2][-3]
'km'
>>> units[-2][-3:-1]
['km', 'miles']
>>> units[-2][-2:]
['miles', 'league']
>>> units[-1][-2:0]
[]
>>> units[-1][-2:]
['pound', 'stone']
>>> units[-1][-3:-1]
['kg', 'pound']
>>> 
