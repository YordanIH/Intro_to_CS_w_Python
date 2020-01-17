#a
"""
for each pair of items in the usorted list:
    if the pair is out of order :
        swap them
"""

#b
#The end of the unsorted list
"""end = len(lst) - 1

#Keep going until the last item of the list is reached
while end != 0 :
    for each pair of items in the usorted list:
    if the pair is out of order :
        swap them
    end = end -1
"""
#c
def bubble_sort(lst: list):
    end = len(lst) - 1

    while end != 0:
        for i in range(0,end):
            if lst[i] > lst[i + 1]:
                lst[i],lst[i + 1] = lst[i + 1], lst[i]
        end = end - 1
        print(lst)
    return lst
    


print(bubble_sort([3, 8, 4, -1, 6, 7, 1, 2, 5,10]))


