Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> help(list())
Help on list object:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |  
 |  append(self, object, /)
 |      Append object to the end of the list.
 |  
 |  clear(self, /)
 |      Remove all items from list.
 |  
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |  
 |  sort(self, /, *, key=None, reverse=False)
 |      Sort the list in ascending order and return None.
 |      
 |      The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
 |      order of two equal elements is maintained).
 |      
 |      If a key function is given, apply it once to each list item and sort them,
 |      ascending or descending, according to their function values.
 |      
 |      The reverse flag can be set to sort in descending order.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> 
>>> kingdoms = ['Bacteria','Protozoa','Chromista','Plantae','Fungi','Animalia']
>>> kindoms[0]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    kindoms[0]
NameError: name 'kindoms' is not defined
>>> kingdoms[0]
'Bacteria'
>>> kingdoms[-1]
'Animalia'
>>> kingdoms[:3]
['Bacteria', 'Protozoa', 'Chromista']
>>> kingdoms[2:5]
['Chromista', 'Plantae', 'Fungi']
>>> kingdoms[-2]
'Fungi'
>>> kingdoms[-2:0]
[]
>>> kingdoms[-2:-1]
['Fungi']
>>> kingdoms[-3:-1]
['Plantae', 'Fungi']
>>> kingdoms[-3:]
['Plantae', 'Fungi', 'Animalia']
>>> kingdoms[-2:]
['Fungi', 'Animalia']
>>> kingdoms[:]
['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
>>> kingdoms[-6]
'Bacteria'
>>> kingdoms[-5]
'Protozoa'
>>> kingdoms[6]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    kingdoms[6]
IndexError: list index out of range
>>> kingdoms[5]
'Animalia'
>>> kingdoms[-6:-3]
['Bacteria', 'Protozoa', 'Chromista']
>>> kingdoms[-4:-1]
['Chromista', 'Plantae', 'Fungi']
>>> kingdoms[-1:0]
[]
>>> kingdoms[-1:]
['Animalia']
>>> kingdoms[-2:]
['Fungi', 'Animalia']
>>> kingdoms[1:0]
[]
>>> appointments = ['9:00','10:30','14:00','15:00','15:30']
>>> appointments.append(['16:30'])
>>> appointments
['9:00', '10:30', '14:00', '15:00', '15:30', ['16:30']]
>>> appointments.pop()
['16:30']
>>> appointments
['9:00', '10:30', '14:00', '15:00', '15:30']
>>> appointments.append('16:30')
>>> appointments
['9:00', '10:30', '14:00', '15:00', '15:30', '16:30']
>>> appointments + ["16:30']
		
SyntaxError: EOL while scanning string literal
>>> appointments + ['16:30']
['9:00', '10:30', '14:00', '15:00', '15:30', '16:30', '16:30']
>>> appointments.pop()
'16:30'
>>> appointments.pop()
'15:30'
>>> appointments
['9:00', '10:30', '14:00', '15:00']
>>> appointments.append(15)
>>> appointments
['9:00', '10:30', '14:00', '15:00', 15]
>>> appointments.pop()
15
>>> appointments.append('15:30')
>>> appointments
['9:00', '10:30', '14:00', '15:00', '15:30']
>>> appointments+['16:30']
['9:00', '10:30', '14:00', '15:00', '15:30', '16:30']
>>> appointments
['9:00', '10:30', '14:00', '15:00', '15:30']
>>> appointments = appointments+['16:30']
>>> appointments
['9:00', '10:30', '14:00', '15:00', '15:30', '16:30']
>>> appointments.pop()
'16:30'
>>> appointments += [16:30]
SyntaxError: invalid syntax
>>> appointments += ['16:30']
>>> appointments
['9:00', '10:30', '14:00', '15:00', '15:30', '16:30']
>>> #exercise 4
>>> ids=[4353,2314,2956,3382,9362,3900]
>>> ids.remove(3382)
>>> ids
[4353, 2314, 2956, 9362, 3900]
>>> ids.index[9362]
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    ids.index[9362]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> ids.index(9362)
3
>>> inds.insert(3,4499)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    inds.insert(3,4499)
NameError: name 'inds' is not defined
>>> ids.insert(3,4499)
>>> ids
[4353, 2314, 2956, 4499, 9362, 3900]
>>> ids.remove(4499)
>>> ids
[4353, 2314, 2956, 9362, 3900]
>>> ids.insert(4,4499)
>>> ids
[4353, 2314, 2956, 9362, 4499, 3900]
>>> ids.extend([5566,1830])
>>> ids
[4353, 2314, 2956, 9362, 4499, 3900, 5566, 1830]
>>> ids.reverse()
>>> ids
[1830, 5566, 3900, 4499, 9362, 2956, 2314, 4353]
>>> ids.sort()
>>> ids
[1830, 2314, 2956, 3900, 4353, 4499, 5566, 9362]
>>> ids.sort(reverse=true)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    ids.sort(reverse=true)
NameError: name 'true' is not defined
>>> ids.sort(reverse=true)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    ids.sort(reverse=true)
NameError: name 'true' is not defined
>>> ids.sort(reverse=True)
>>> IDS
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    IDS
NameError: name 'IDS' is not defined
>>> ids
[9362, 5566, 4499, 4353, 3900, 2956, 2314, 1830]
>>> #excercise5
>>> 
