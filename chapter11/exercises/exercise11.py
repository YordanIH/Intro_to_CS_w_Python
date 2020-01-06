dict_of_dict = {
    'jgoodall': {'surname': 'Goodall',
                'forename': 'Jane',
                'born': 1934,
                'died': None,
                'notes': 'primate researcher'},
    'rfranklin': {'surname': 'Franklin',
                'forename': 'Rosalind',
                'born': 1920,
                'died': 1957,
                'notes': 'contributed to discovery of DNA'},
    'rcarson': {'surname': 'Carson', 
                'forename': 'Rachel',
                'born': 1907,
                'died': 1964,
                'notes': 'raised awareness of effects of DDT', }
}

def db_consistent(dict_of_dict: dict) -> bool:
    
    inner_keys_list = []
    
    for key in dict_of_dict:
        inner_keys = list(dict_of_dict[key].keys())
        inner_keys.sort()
        inner_keys_list.append(inner_keys)
    for i in range(1, len(inner_keys_list)):
        if len(inner_keys_list[0]) != len(inner_keys_list[i]):
            return False
        for j in range(len(inner_keys_list[0])):
            if inner_keys_list[0][j] != inner_keys_list[i][j]:
                return False
    return True
        

print(db_consistent(dict_of_dict))
