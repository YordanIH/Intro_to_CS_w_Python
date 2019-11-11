"""10.Variable units refers to the nested list [[’km’, ’miles’, ’league’], [’kg’, ’pound’, ’stone’]]. Using units and either slicing or indexing with positive indices, write expressions that produce the following:

The first item of units (the first inner list)
The last item of units (the last inner list)
The string ’km’
The string ’kg’
The list [’miles’, ’league’]
The list [’kg’, ’pound’]
"""

>>> units = [['km','miles','league'],['kg','pound','stone']]
#The first item of units (the first inner list)
>>> units[0]
['km', 'miles', 'league']
#The last item of units (the last inner list)
>>> units[1]
['kg', 'pound', 'stone']
#The string ’km’
>>> units[0][0]
'km'
#The string ’kg’
>>> units[1][0]
'kg'
#The list [’miles’, ’league’]
>>> units[0][1:3]
['miles', 'league']
#The list [’kg’, ’pound’]
>>> units[1][0:2]
['kg', 'pound']

"""11.Repeat the previous exercise using negative indices"""


#The first item of units (the first inner list)
>>> units[-2]
['km', 'miles', 'league']

#The last item of units (the last inner list)
>>> units[-1]
['kg', 'pound', 'stone']

#The string ’km’
>>> units[-2][-3]
'km'

#The string ’kg’
>>> units[-2][-3:-1]
['km', 'miles']

#The list [’miles’, ’league’]
>>> units[-2][-2:]
['miles', 'league']

#The list [’kg’, ’pound’]
>>> units[-1][-3:-1]
['kg', 'pound']
