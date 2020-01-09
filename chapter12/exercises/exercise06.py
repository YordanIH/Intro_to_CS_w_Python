"""
>>> find_two_smallest([809, 834, 477, 478, 307, 122, 96, 96, 324, 476]
(6,6)
"""
from typing import List, Tuple

def find_two_smallest(L: List[float]) -> Tuple[int, int]:
    # Get a sorted copy of the list so that the two smallest items are at the 
    # front
    temp_list = sorted(L)
    smallest = temp_list[0]
    next_smallest = temp_list[1]

    if temp_list[0] == temp_list[1]:
        min1=L.index(smallest)
        min2=L.index(smallest,(L.index(smallest)+1) )
    
    else:
        

    # Find the indices in the original list L
        min1 = L.index(smallest)
        min2 = L.index(next_smallest)

    return (min1, min2)

print(find_two_smallest([809, 834, 96, 478, 307, 122, 96, 100, 324, 476]))