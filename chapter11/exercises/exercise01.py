def find_dups(numbers_list: list) -> set :
    """ (list) -> set
    Return the number of duplicates numbers from L.
    >>> find_dups([1, 1, 2, 3, 4, 2])
    {1, 2}
    >>> find_dups([1, 2, 3, 4])
    set()
    """ 
    new_numbers_list = []
    for items in numbers_list:
        if numbers_list.count(items)>=2:
            new_numbers_list.append(items)
    print(set(new_numbers_list)) 

if __name__ == '__main__':
    find_dups([1, 1, 2, 3, 4, 2])
    find_dups([1, 2, 3, 4])

