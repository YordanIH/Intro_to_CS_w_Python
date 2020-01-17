"""All three versions of linear search start at index 0. Rewrite all to search from
the end of the list instead of from the beginning. Make sure you test them.
"""
from typing import Any

def linear_search1(lst: list, value: Any) -> int:
    """Return the index of the first occurence of the value in lst, or return -1 if value is not in lst.
    >>> linear_search([2, 5, 1, -3], 5)
    1
    >>> linear_search([2, 4, 2], 2)
    0
    >>> linear_search([2, 5, 1, -3], 4)
    -1
    >>> linear_search([], 5)
    -1
    """
    # examine the items at each index i in lst, starting at index 0:
    # is lst[i] the value we are looking for?  if so, stop searching.

    i = len(lst) - 1 # The index of the next item in lst to examine.

    # Keep going until we reach the end of lst or until we find value.
    while i != -1 and lst[i] !=value:
        i = i - 1 
    # If we fell off the end of  the list,. we didn't find value.
    if i == -1 :
        return -1
    else:
        return i 

def linear_search2(lst: list, value: Any) -> int:
    """...Exactly the same docstring goes here...
    """

    for i in range(len(lst)-1,-1,-1):
        if lst[i] == value:
            return i 
    return -1

def linear_search3(lst: list, value: Any) -> int:
    """...Exactly the same docstring goes here..."""

    #Add the sentinel.
    lst.insert(0,value)

    i = len(lst)-1

    # Keep going until we find value.
    while lst[i] != value:
        i = i - 1
    
    #Remove the sentinel.
    lst.pop()

    # If we reached the end of the list we didn't find value
    if i == 0:
        return -1
    else:
        return i - 1

print(linear_search1([2, 5, 1, -3], 5))
print(linear_search2([2, 5, 1, -3], 5))
print(linear_search3([2, 5, 1, -3], 5))
