>>> #whales count
>>> whales = [5,4,7,3,2,3,2,6,4,2,1,7,1,3]
>>> whales
[5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
>>> #putting an index to refer to a particular list item
>>> whales[4]
2
>>> #length of a list
>>> len(whales)
14
>>> #getting the last item of a list
>>> whales[len(whales)-1]
3
>>> #why the last item is len() -1
>>> whales[len(whales)]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    whales[len(whales)]
IndexError: list index out of range
>>> #indexing backwards
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
>>> #assigning items in the list to other variables
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
>>> #modifying lists
>>> nobles = ['helium', 'none', 'argon', 'krypton', 'xenon', 'radon']
>>> nobles[1]=='neon'
False
>>> nobles[1]='neon'
>>> nobles
['helium', 'neon', 'argon', 'krypton', 'xenon', 'radon']
>>> nobles[1]
'neon'
>>> #apart from stings lists are mutable
>>> name = 'Darwin'
>>> capitalized = name.upper()
>>> print(capitalized)
DARWIN
>>> print(name)
Darwin
>>> #isotope,lists functions
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
>>> #delete from list
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
>>> #slicing lists
>>> celegans_phenotypes = ['Emb', 'Hin', 'Unc', 'Lon', 'Dpy', 'Sma']
>>> celegans_phenotypes
['Emb', 'Hin', 'Unc', 'Lon', 'Dpy', 'Sma']
>>> useful_markers = celegans_phenotypes[0:4]
>>> useful_markers
['Emb', 'Hin', 'Unc', 'Lon']
>>> useful_markers = celegans_phenotypes[1:4]
>>> 
>>> useful_markers
['Hin', 'Unc', 'Lon']
>>> useful_markers = celegans_phenotypes[0:4]
>>> useful_markers = celegans_phenotypes[0:5]
>>> useful_markers
['Emb', 'Hin', 'Unc', 'Lon', 'Dpy']
>>> useful_markers = celegans_phenotypes[0:6]
>>> useful_markers
['Emb', 'Hin', 'Unc', 'Lon', 'Dpy', 'Sma']
>>> useful_markers = celegans_phenotypes[0:4]
>>> celegans_phenotypes[:4]
['Emb', 'Hin', 'Unc', 'Lon']
>>> celegans_phenotypes[4:]
['Dpy', 'Sma']
>>> celegans_copy = celegans_phenotypes[:]
>>> celegans_phenotypes[5]
'Sma'
>>> celegans_phenotypes[5] = 'lvl'
>>> celegans_phenotypes
['Emb', 'Hin', 'Unc', 'Lon', 'Dpy', 'lvl']
>>> celegans_copy
['Emb', 'Hin', 'Unc', 'Lon', 'Dpy', 'Sma']
>>> celegans_phenotypes = ['Emb', 'Him', 'Unc', 'lon', 'Dpy', 'Sma']
>>> #Aliasing
>>> celegans_alias = celegans_phenotypes
>>> celegans_phenotypes
['Emb', 'Him', 'Unc', 'lon', 'Dpy', 'Sma']
>>> celegans_phenotypes[5] = 'lvl'
>>> celegans_phenotypes
['Emb', 'Him', 'Unc', 'lon', 'Dpy', 'lvl']
>>> celegans_alias
['Emb', 'Him', 'Unc', 'lon', 'Dpy', 'lvl']
>>> #mutable parameters
>>> def remove_last_item(L: list) ->list:
	"""Return list L with the last item removed.

	Precondition: len(L)>=0

	>>> remove_last_item([1,3,2,4])
	[1,3,2]
	"""
	del L[-1]
	return L

>>> celegans_markers = ['Emb', 'Him','Unc', 'Lon', 'Dpy', 'Lvl']
>>> remove_last_item(celegans_markers)
['Emb', 'Him', 'Unc', 'Lon', 'Dpy']
>>> def remove_last_item(L: list) ->list:
	"""Return list L with the last item removed.

	Precondition: len(L)>=0

	>>> remove_last_item([1,3,2,4])
	[1,3,2]
	"""
	del L[-1]

	
>>> remove_last_item(celegans_markers)
>>> celegans_markers
['Emb', 'Him', 'Unc', 'Lon']

>>> def remove_last_item(L: List[Any]) -> None:
	"""Remove the last item from L.
	Precondition: len(L) >= 0

	>>>remove_last_item([1, 3, 2, 4])
	"""
	del L[-1]

	
>>> #List Methods
>>> colors = ['red', 'orange', 'greem']
>>> colors.extend(['black', 'blue'])
>>> colors
['red', 'orange', 'greem', 'black', 'blue']
>>> colors.append('purple')
>>> colors
['red', 'orange', 'greem', 'black', 'blue', 'purple']
>>> colors.insert(2, 'yellow')
>>> 
>>> colors
['red', 'orange', 'yellow', 'greem', 'black', 'blue', 'purple']
>>> colors.remove('black')
>>> colors
['red', 'orange', 'yellow', 'greem', 'blue', 'purple']
>>> colors = 'red orange yellow green blue purple'.split()
>>> colors
['red', 'orange', 'yellow', 'green', 'blue', 'purple']
>>> sorted_colors = colors.sort()
>>> print(sorted_colors)
None
>>> colors
['blue', 'green', 'orange', 'purple', 'red', 'yellow']
>>> #nested lists
>>> life = [['Canada',76.5], ['United States', 75,5], ['Mexico', 72.0]]
>>> life[0]
['Canada', 76.5]
>>> life[2]
['Mexico', 72.0]
>>> life[1]
['United States', 75, 5]
>>> life[1][0]
'United States'
>>> life[1][1]
75
>>> canada = life[0]
>>> canada
['Canada', 76.5]
>>> canada[0]
'Canada'
>>> canada[1]
76.5
>>> life = [['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0]]
>>> canada = life[0]
>>> canada[1] =80.0
>>> canada
['Canada', 80.0]
>>> life
[['Canada', 80.0], ['United States', 75.5], ['Mexico', 72.0]]

