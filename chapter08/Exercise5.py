"""In this exercise, you’ll create a list and then answer questions about that list.

Assign a list that contains the atomic numbers of the six alkaline earth metals—beryllium (4), magnesium (12), calcium (20), strontium (38), barium (56), and radium (88)—to a variable called alkaline_earth_metals.
Which index contains radium’s atomic number? Write the answer in two ways, one using a positive index and one using a negative index.
Which function tells you how many items there are in alkaline_earth_metals?
Write code that returns the highest atomic number in alkaline_earth_metals. (Hint: Use one of the functions from Table 10, ​List Functions​.)"""

#Assign a list that contains the atomic numbers of the six alkaline earth metals—beryllium (4), magnesium (12), calcium (20), strontium (38), barium (56), and radium (88)—to a variable called alkaline_earth_metals.
>>> alkaline_earth_metals = [4,12,20,38,56,88 ]
>>> alkaline_earth_metals
[4, 12, 20, 38, 56, 88]
#Which index contains radium’s atomic number? Write the answer in two ways, one using a positive index and one using a negative index.
>>> alkaline_earth_metals.index(88)
5
>>> alkaline_earth_metals[-1]
88
#Which function tells you how many items there are in alkaline_earth_metals?
>>> len(alkaline_earth_metals)
6
#Write code that returns the highest atomic number in alkaline_earth_metals. (Hint: Use one of the functions from Table 10, ​List Functions​.)"""
max(alkaline_earth_metals)
88
