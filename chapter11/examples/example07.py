>>> (8)
8
>>> type((8))
<class 'int'>
>>> (8,)
(8,)
>>> type((8,))
<class 'tuple'>
>>> (5 + 3 )
8
>>> (5+3,)
(8,)
>>> life = (['Canada', 76.5], ['United States', 75.5],['Mexico',72.0])
>>> life[0] = life[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> life[0][1] = 80.0
>>> life
(['Canada', 80.0], ['United States', 75.5], ['Mexico', 72.0])
>>> canada = ['Canada', 76.5]
>>> usa = ['United States', 75.5]
>>> mexico = ['Mexico', 72.0]
>>> life = (canada, usa, mexico)
>>> mexico = ['Mexico', 72.5]
>>> life
(['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0])
>>> mexico
['Mexico', 72.5]
>>> life[0][1] = 80.0
>>> canada
['Canada', 80.0]