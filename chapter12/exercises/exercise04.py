# Two items; smallest first.
>>> find_two_smallest([1, 2])
(0, 1)
# Two items; smallest second.
>>> find_two_smallest([3, 2])
(1, 0)
# Two items; same values.
>>> find_two_smallest([3, 3])
(0, 1)
# Three items items; 2nd smallest is duplicated.
>>> find_two_smallest([3, 1, 3])
(1, 0)
# Multiple items: smallest at beginning; 2nd smallest at middle.
>>> find_two_smallest([1, 4, 2, 3, 4])
(0, 2)
# Multiple items: smallest at middle; 2nd smallest at end.
>>> find_two_smallest([4, 3, 1, 5, 6, 2])
(5, 3)
# Multiple items: smallest at end; 2nd smallest at beginning.
>>> find_two_smallest([-2, 4, 3, 2, 5, 6, -1])
(3, 4)