#a
#To find the complement we need go over the sequence
#  and change every character to their complement one


def complement(dna: str) -> str:
    """
    >>> complement("AATTGGCC")
        "TTAACCGG"
    """
    dict_of_complement={'A':'T','T':'A', 'C':'G', 'G':'C'}
    sequence_of_complement=''
    for char in dna:
        sequence_of_complement =sequence_of_complement + dict_of_complement[char]
    return sequence_of_complement 

print(complement("AATTGGCC"))
        
        