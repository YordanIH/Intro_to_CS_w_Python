dictionary={'name': 1,'name2': 2,'name4':1, 'name3': 2}

def count_duplicates(dict: dict) ->int:
    
    duplicates=0
    values=list(dictionary.values())
    print(values)

    for item in values:
        if  values.count(item) >=2:
            duplicates +=1

            num=values.count(item)
            for i in range(num):
                values.remove(item)

    return duplicates
        
        


print(count_duplicates(dictionary))