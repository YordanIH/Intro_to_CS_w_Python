#Using the in Operator on Tuples, Sets, and Dictionaries
>>> odds = set([1, 3, 5, 7, 9])
>>> 9 in odds
True
>>> 8 in odds
False
>>> '9' in odds
False
>>> evens = (0, 2, 4, 6, 8)
>>> 4 in evens
True
>>> 11 in evens
False
>>> bird_to_observations = {'canada goose': 183, 'long-tailed jaeger': 71, 'snow goose': 63, 'northern fulmar': 1}
>>> 
>>> 'snow goose' in bird_to_observations
True
>>> 183 in bird_to_observations
False
