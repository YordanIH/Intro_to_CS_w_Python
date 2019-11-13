
def mystery_function(values):
    
""" Takes as value nested lists and returns the same

This function is meant to reverse the order of items in the inner lists but keep the orde
in the outher one
>>>mystery_function([[1,2,3],[3,4,5],[3,2,1]])
[[3, 2, 1], [5, 4, 3], [1, 2, 3]]
"""
    #defining an empty list
    result = []
    
    for sublist in values:
        result.append([sublist[0]])
        ##Reversing each individual list by putting the next
        #value infromt of the previous one in the list
        
        for i in sublist[1:]:
            result[-1].insert(0, i)
    return result

