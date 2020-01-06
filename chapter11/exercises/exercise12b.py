vector1={1: 3, 3: 4}
vector2={2: 4, 3: 5, 5: 6}
def sparse_dot(vector1, vector2):
    """
    >>> sparse_dot({1: 3, 3: 4}, {2: 4, 3: 5, 5: 6})
    20
    """ 
    dot = 0
    for key1 in vector1:
        if key1 in vector2:
            dot = dot + vector1[key1] * vector2[key1]
    return dot