import time
import example02
import example03
import example04

from typing import Callable, List, Any

def time_find_two_smallest(find_func: Callable[[List[float]], Any],lst: List[float]) -> float:
    """Return how many seconds find_func(lst) took to execute."""

    t1 = time.perf_counter()
    find_func(lst)
    t2 = time.perf_counter()
    return (t2 - t1)

if __name__ == '__main__':
    # Gather the sea level pressures
    sea_levels = []
    sea_levels_file = open('sea_levels.txt', 'r')
    for line in sea_levels_file:
        sea_levels.append(float(line))
    sea_levels_file.close()

    # Time each of the approaches
    find_remove_find_time = time_find_two_smallest(example02.find_two_smallest, sea_levels)
    sort_get_minimums_time = time_find_two_smallest(example03.find_two_smallest, sea_levels)
    walk_through_time = time_find_two_smallest(example04.find_two_smallest, sea_levels)
    
    print ('"Find, remove, find" took {:.8f}ms.'.format(find_remove_find_time))
    print ('"Sort, get minimus" took {:.8f}ms.'.format(sort_get_minimums_time))
    print('"Walk through the list" took {:.8f}ms.'.format(walk_through_time))
