'''Draw a memory model showing the effect of the following statements:

​ 	values = [0, 1, 2]
​ 	values[1] = values
'''

>>> values = [0,1,2]
>>> values[1] = values
>>> values
[0, [...], 2]
