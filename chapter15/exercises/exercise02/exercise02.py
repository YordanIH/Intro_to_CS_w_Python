line_intersect([[-1, -1], [1, 1]], [[-1, 1], [1, -1]])
[0, 0]
"""The arguments intersect so we expect to get their point of intersection."""
line_intersect([[0, 0], [0, 0]], [[0, 0], [0, 1]])
None
"""The first argument is not a pair of distinct points so they can’t intersect."""
line_intersect([[0, 0], [0, 1]], [[0, 0], [0, 0]])
None
"""The second argument is not a pair of distinct points so they can’t intersect."""
line_intersect([[0, 0], [1, 0]], [[0, 0], [2, 0]])
[[0, 0], [1, 0]]
"""The lines are coincident so we expect the first line as the return value."""
line_intersect([[0, 0], [2, 0]], [[0, 0], [1, 0]])
[[0, 0], [2, 0]]
"""Same as the previous, but we switch the order. We still expect the first line as the
return value."""
line_intersect([[0, 0], [1, 0]], [[0, 1], [1, 1]])
None
 """The lines are parallel but not coincident, so they don’t intersect. This ensures we
detect coincident lines properly."""