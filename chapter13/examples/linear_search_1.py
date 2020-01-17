from typing import Any

def linear_search(lst: list, value: Any) -> int:
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

    i = 0 # The index of the next item in lst to examine.

    # Keep going until we reach the end of lst or until we find value.
    while i != len(lst) and lst[i] !=value:
        i = i+1
    # If we fell off the end of  the list,. we didn't find value.
    if i == len(lst):
        return -1
    else:
        return i 
        
