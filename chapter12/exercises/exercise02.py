#a
index=0
smallest=L[0]

for i in range(1,len(L)):
    if L[i] < smallest:
        smallest=L[i]
        index = i 

#b 
def min_index(L: list) -> tuple:
""" (list) -> (object, int)
    Return a tuple containing the smallest item from L and its index.
    >>> min_index([4, 3, 2, 4, 3, 6, 1, 5])
    (1, 6)
    """
    index=0
    smallest=L[0]

    for i in range(1,len(L)):
        if L[i] < smallest:
            smallest=L[i]
            index = i 
    return (smallest, index)

print(min_index([4, 3, 2, 4, 3, 6, 1, 5]))

#c

def min_or_max_index(L:list,P:bool) -> tuple:
    if P == True :
        index=0
        smallest=L[0]

        for i in range(1,len(L)):
            if L[i] < smallest:
                smallest=L[i]
                index = i 
        return (smallest, index)
    else :
        index = 0
        biggest = L[0]

        for i in range(1,len(L)):
            if L[i] > biggest:
                biggest = L[i]
                index = i 
        return (biggest, index)    
       
print(min_or_max_index([4, 3, 2, 4, 3, 6, 1, 5],False))



