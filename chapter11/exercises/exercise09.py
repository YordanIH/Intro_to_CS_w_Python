dict1={"item1":1,"item2":2,"item3":3}
dict2={"item1":1,"item3":3}

def dict_intersect(dict1: dict, dict2: dict):
    dict_intersect={}
    for (keys,values) in dict1.items():
        if keys in dict2 and values==dict2[keys]:
            dict_intersect[keys]=values
    return dict_intersect


print(dict_intersect(dict1,dict2))