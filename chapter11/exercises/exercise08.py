dictionary={'R': 0.3,'B': 0.3, 'G': 0.4}

def is_balanced(dictionary: dict) ->bool:
    """This function tell us if the colors are balanced
    >>> is_balanced(dictionary)
    >>> True
    """
    sum = 0
    for items in dictionary.values():
        sum=sum+items
    if sum==1:
        return True
    else :
        return False

print(is_balanced(dictionary))
