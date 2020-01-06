vector1={1: 3, 3: 4}
vector2={2: 4, 3: 5, 5: 6}
def sparse_add(vector1: dict, vector2: dict)-> dict:
    """
    >>> sparse_add(vector1,vector2)
    {1: 3, 3: 9, 2: 4, 5: 6}
    """
    sum_vector = vector1.copy()

    for key in vector2:
        if key in sum_vector:
            sum_vector[key] = sum_vector[key] + vector2[key]
        else:
            sum_vector[key] = vector2[key]
    return sum_vector

print(sparse_add(vector1,vector2))
