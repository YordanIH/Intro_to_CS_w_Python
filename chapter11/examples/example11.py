#Looping over Dictionaries
>>> bird_to_observations = {'canada goose': 183, 'long-tailed jaeger': 71,'snow goose': 63, 'northern fulmar':1}
>>> for bird in bird_to_observations:
...     print(bird, bird_to_observations[bird])
... 
canada goose 183
long-tailed jaeger 71
snow goose 63
northern fulmar 1

#Dictionary Operations
>>> scientist_to_birthdate = {'Newton' : 1642, 'Darwin' : 1809, 'Turing' : 1912}
>>> scientist_to_birthdate.keys()
dict_keys(['Newton', 'Darwin', 'Turing'])
>>> scientist_to_birthdate.values()
dict_values([1642, 1809, 1912])
>>> scientist_to_birthdate.items()
dict_items([('Newton', 1642), ('Darwin', 1809), ('Turing', 1912)])
>>> scientist_to_birthdate.get('Newton')
1642
>>> scientist_to_birthdate.get('Curie',1876)
1876
>>> scientist_to_birthdate
{'Newton': 1642, 'Darwin': 1809, 'Turing': 1912}
>>> researcher_to_birthdate = {'Curie': 1876, 'Hopper' : 1906, 'Franklin' : 1920}
>>> scientist_to_birthdate.update(researcher_to_birthdate)
>>> scientist_to_birthdate
{'Newton': 1642, 'Darwin': 1809, 'Turing': 1912, 'Curie': 1876, 'Hopper': 1906, 'Franklin': 1920}
>>> researcher_to_birthdate
{'Curie': 1876, 'Hopper': 1906, 'Franklin': 1920}
>>> researcher_to_birthdate.clear()
>>> researcher_to_birthdate
{}

#Common use of items() with dictionaries
>>> scientist_to_birthdate = {'Newton' : 1642, 'Darwin' : 1809, 'Turing' : 1912}
>>> for scientist, birthdate in scientist_to_birthdate.items():
...     print(scientist, 'was born in', birthdate)
Newton was born in 1642
Darwin was born in 1809
Turing was born in 1912