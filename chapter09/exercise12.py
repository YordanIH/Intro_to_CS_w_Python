'''When remove_neg([1, 2, 3, -3, 6, -1, -3, 1]) is executed, it produces [1, 2, 3, 6, -3, 1]. The for loop traverses the elements of the list, and when a negative value (like -3 at position 3) is reached, it is removed, shifting the subsequent values one position earlier in the list (so 6 moves into position 3). The loop then continues on to process the next item, skipping over the value that moved into the removed item’s position. If there are two negative numbers in a row (like -1 and -3), then the second one won’t be removed.

Rewrite the code to avoid this problem.'''





from typing import List

def remove_neg(num_list: List[float]) -> None:
    """Remove the negative numbers from the list num_list.
    >>> numbers = [-5, 1, -3, 2]
    >>> remove_neg(numbers)
    >>> numberd
    [1, 2]
    """

    index = 0
    while index < len(num_list):
        if num_list[index] < 0:
            del num_list[index]
        else:
            index +=1
    print(num_list)
    
remove_neg([-1,-2,4,5,5, -3])
