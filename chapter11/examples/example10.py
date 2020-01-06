#dictionaries
>>> bird_to_observations = {'canada goose':3, 'northern fulmar':1}
>>> bird_to_observations
{'canada goose': 3, 'northern fulmar': 1}
>>> bird_to_observations['northern fulmar']
1
>>> bird_to_observations['canada goose']
3
>>> bird_to_observations['long-tailed jaeger']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'long-tailed jaeger'
>>> dict1= {'canada goose': 3, 'northern fulmar': 1}
>>> dict2 = {'northern fulmar': 1, 'canada goose': 3}
>>> dict1==dict2
True
>>> 
###updating and checking membership
>>> bird_to_observations = {}
>>> 
>>> #Add a new key/value pair, 'snow goose': 33.
>>> bird_to_observations['snow goose'] = 33
>>> 
>>> # Add a new key/value pair, 'eagle': 999.
>>> bird_to_observations['eagle'] = 999
>>> bird_to_observations
{'snow goose': 33, 'eagle': 999}
>>> 
>>> # Change the value associated with key 'eagle' to 9.
>>> bird_to_observations['eagle'] = 9
>>> bird_to_observations
{'snow goose': 33, 'eagle': 9}
# delete an entry from a dictionary
>>> del bird_to_observations['snow goose']
>>> bird_to_observations
{'eagle': 9}
>>> del bird_to_observations['gannet']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'gannet'

#  in operator

>>> bird_to_observations = {'eagle': 999, 'snow goose': 33}
>>> 'eagle' in bird_to_observations
True
>>> if 'eagle' in bird_to_observations:
...     print('eagles have been seen')
eagles have been seen
>>> del bird_to_observations['eagle']
>>> 'eagle' in bird_to_observations
False
>>> if 'eagle' in bird_to_observations:
...     print('eagles have been seen')
>>> 