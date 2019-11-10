Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #whales count
>>> whales = [5,4,7,3,2,3,2,6,4,2,1,7,1,3]
>>> whales
[5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
>>> whale[4]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    whale[4]
NameError: name 'whale' is not defined
>>> whales[4]
2
>>> len(whales)
14
>>> whales[len(whales)-1]
3
>>> whales[len(whales)]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    whales[len(whales)]
IndexError: list index out of range
>>> whales[-1]
3
>>> whales[-2]
1
>>> whales[-14]
5
>>> whales[-15]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    whales[-15]
IndexError: list index out of range
>>> third = whales[2]
>>> print('Third day:', third)
Third day: 7
>>> whales = []
>>> #empty list
>>> whales[0]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    whales[0]
IndexError: list index out of range
>>> whales[-1]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    whales[-1]
IndexError: list index out of range
>>> krypton = ['Krypton', 'Kr', -157.2,-153.4]
>>> krypton[1]
'Kr'
>>> krypton[2]
-157.2
>>> def average(L: list) -> float:
	"""Return the average of the vlaues in L.

>>> average([1.4, 1.6, 1.8])
1.7
"""

	
>>> 
>>> def average(L: list[float]) -> float:
	"""Return the average of the vlaues in L.

>>> average([1.4, 1.6, 1.8])
1.7
"""

	
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    def average(L: list[float]) -> float:

TypeError: 'type' object is not subscriptable
>>> from typing import list
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    from typing import list
ImportError: cannot import name 'list' from 'typing' (/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/typing.py)
>>> from typing import List
>>> def average(L: List[float]) -> float:
	"""Return the average of the vlaues in L.

>>> average([1.4, 1.6, 1.8])
1.7
"""

	
>>> nobles = ['helium', 'none', 'argon', 'krypton', 'xenon', 'radon']
>>> nobles[1]==neon
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    nobles[1]==neon
NameError: name 'neon' is not defined
>>> nobles[1]=='neon'
False
>>> nobles[1]='neon'
>>> nobles
['helium', 'neon', 'argon', 'krypton', 'xenon', 'radon']
>>> nobles[1]
'neon'
>>> #isotope
>>> half_lives = [887.7, 24100.0, 6563.0, 14, 373300.0]
>>> len(half_lives)
5
>>> max(half_lives)
373300.0
>>> min(half_lives)
14
>>> sum(half_lives)
404864.7
>>> sorted(half_lives)
[14, 887.7, 6563.0, 24100.0, 373300.0]
>>> half_lives
[887.7, 24100.0, 6563.0, 14, 373300.0]
>>> #concatenation
>>> original = ['H', 'He', 'Li']
>>> final = original + ['Be]
		    
SyntaxError: EOL while scanning string literal
>>> final = original + ['Be']
>>> final
['H', 'He', 'Li', 'Be']
>>> ['H', 'He', 'Li'] + ['Be']
['H', 'He', 'Li', 'Be']
>>> ['H', 'He', 'Li'] + 'Be'
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    ['H', 'He', 'Li'] + 'Be'
TypeError: can only concatenate list (not "str") to list
>>> #multiply
>>> metals = ['Fe', 'Ni']
>>> metals * 3
['Fe', 'Ni', 'Fe', 'Ni', 'Fe', 'Ni']
>>> #delete from lis
>>> metals = ['Fe', 'Ni']
>>> del metals[0]
>>> metals
['Ni']
>>> #the in operator in lists
>>> nobles = ['helion', 'neon', 'argon', 'krypton', 'xenon', 'radon']
>>> gas=input('Enter a gas: ')
Enter a gas: argon
>>> if gas in nobles:
	print('{} is noble.'.format(gas))

	
argon is noble.
>>> gas = input('Enter a gas: ')
Enter a gas: nitrogen
>>> if gas in nobles:
	print('{} is noble.'.format(gas))

	
>>> 
>>> [1,2] in [0, 1, 2, 3]
False
>>> 
