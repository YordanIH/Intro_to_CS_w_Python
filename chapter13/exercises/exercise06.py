#a
"""
for each pair of items in the unsorted list:
    if the pair is out of order :
        swap them
"""

#b
#The end of the unsorted list
"""begining is 0
end is len(lst)-1

#Keep going until the last item of the list is reached
while beginig < len(lst) :
    for each pair of items in the unsorted list:
    if the pair is out of order :
        swap them
    begining = begining + 1
"""
#c
def bubble_sort_2(L: list):
    
    begining = 0

    while begining != len(L) - 1:
        for i in range(len(L) -1 , begining, -1):
            if L[i] > L[i - 1]:
                L[i],L[i - 1] = L[i - 1], L[i]
        begining = begining + 1
    return L
    


