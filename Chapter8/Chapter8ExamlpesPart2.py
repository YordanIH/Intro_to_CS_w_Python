Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
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
>>> celegans_phenotypes4:]
SyntaxError: unmatched ']'
>>> celegans_phenotypes[4:]
['Dpy', 'Sma']
>>> celegans_copy = celegans_phenotypes[:]
>>> celegans_phenotypes[]5
SyntaxError: invalid syntax
>>> celegans_phenotypes[5]
'Sma'
>>> celegans_phenotypes[5] = 'lvl'
>>> celegans_phenotypes
['Emb', 'Hin', 'Unc', 'Lon', 'Dpy', 'lvl']
>>> celegans_copy
['Emb', 'Hin', 'Unc', 'Lon', 'Dpy', 'Sma']
>>> celegans_phenotypes = ['Emb', 'Him', 'Unc', 'lon', 'Dpy', 'Sma]
		       
SyntaxError: EOL while scanning string literal
>>> celegans_phenotypes = ['Emb', 'Him', 'Unc', 'lon', 'Dpy', 'Sma']
>>> celegans_alias = celegans_phenotypes
>>> celegans_phenotypes
['Emb', 'Him', 'Unc', 'lon', 'Dpy', 'Sma']
>>> celegans_phenotypes[5] = 'lvl'
>>> celegans_phenotypes
['Emb', 'Him', 'Unc', 'lon', 'Dpy', 'lvl']
>>> celegans_alias
['Emb', 'Him', 'Unc', 'lon', 'Dpy', 'lvl']
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
>>> from typing iport List, Any
SyntaxError: invalid syntax
>>> from typing import List, Any
>>> def remove_last_item(L: list[Any]) -> None:
	"""Remove the last item from L.
	Precondition: len(L) >= 0

	>>>remove_last_item([1, 3, 2, 4])
	"""
	del L[-1]

	
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    def remove_last_item(L: list[Any]) -> None:
TypeError: 'type' object is not subscriptable
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
>>> life[1[]0]
SyntaxError: invalid syntax
>>> life[1[0]]
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    life[1[0]]
TypeError: 'int' object is not subscriptable
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
>>> 
>>> 
