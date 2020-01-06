from typing import Dict,Set

def count_values(dictionary: dict) -> int:
    """ Input is a dictionary and the output is the number of distict values it has"""
    return len(set(dictionary.values()))

dictionary={"red": 1, 'green' : 1, 'blue' : 2 ,'turundjav' : 3 , 'orange' : 2}
print(count_values(dictionary))