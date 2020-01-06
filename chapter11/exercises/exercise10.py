
dict1 = {
    'jgoodall': {'surname': 'Goodall',
                 'forename': 'Jane',
                 'born': 1934,
                 'died': None,
                 'notes': 'primate researcher', 'author': ['In the Shadow of Man',
                                                           'The Chimpanzees of Gombe']}, 
    'rfranklin': {'surname': 'Franklin',
                'forename': 'Rosalind',
                'born': 1920,
                'died': 1957,
                'notes': 'contributed to discovery of DNA'},
    'rcarson': {'surname': 'Carson', 
                'forename': 'Rachel',
                'born': 1907,
                'died': 1964,
                'notes': 'raised awareness of effects of DDT', 'author': ['Silent Spring']}
}


def db_headings(dict1: dict):
    """This program returns all the keys in the dictionary of dictionaries
    >>> db_headings(dict1)
    {'died', 'notes', 'surname', 'author', 'born', 'jgoodall', 'rfranklin', 'rcarson', 'forename'}
    """
    headings = set()
    for i in dict1.keys():
        headings.add(i)
    for j in dict1.values():
        for m in j.keys():
            headings.add(m)
    return headings
    

print(db_headings(dict1))