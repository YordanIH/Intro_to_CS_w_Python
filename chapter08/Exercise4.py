"""Variable ids refers to the list [4353, 2314, 2956, 3382, 9362, 3900].
Using list methods, do the following:

Remove 3382 from the list.
Get the index of 9362.
Insert 4499 in the list after 9362.
Extend the list by adding [5566, 1830] to it.
Reverse the list.
Sort the list."""

#Remove 3382 from the list.
>>> ids=[4353,2314,2956,3382,9362,3900]
>>> ids.remove(3382)
>>> ids
[4353, 2314, 2956, 9362, 3900]
#Get the index of 9362.
>>> ids.index(9362)
3
#Insert 4499 in the list after 9362.
>>> ids.insert(4,4499)
>>> ids
[4353, 2314, 2956, 9362, 4499, 3900]
#Extend the list by adding [5566, 1830] to it.
>>> ids.extend([5566,1830])
>>> ids
[4353, 2314, 2956, 9362, 4499, 3900, 5566, 1830]
#Reverse the list.
>>> ids.reverse()
>>> ids
[1830, 5566, 3900, 4499, 9362, 2956, 2314, 4353]
#Sort the list
>>> ids.sort()
>>> ids
[1830, 2314, 2956, 3900, 4353, 4499, 5566, 9362]
