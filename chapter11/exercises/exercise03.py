from typing import Set,Tuple
Compoundset=set(tuple())

def  mating_pairs(male: set, female: set) -> Compoundset:
    """This function takes two equal sized sets and returns a set of tupples.
    Each tuple is made out of the one element of each two starting sets.
    >>> male={'mgerbil1','mgerbil2','mgerbil3','mgerbil4','mgerbil5'}
    >>> female={'fgerbil1','fgerbil2','fgerbil3','fgerbil4','fgerbil5'}
    >>> mating_pairs(male, female)
    {('mgerbil2', 'fgerbil4'), ('mgerbil1', 'fgerbil2'), ('mgerbil4', 'fgerbil3'), ('mgerbil5', 'fgerbil5'), ('mgerbil3', 'fgerbil1')}
    """
    set_of_pairs=set()
    found =True
    while found:
        if len(male)>0 and len(female)>0:
            malegerbil=male.pop()
            femalegerbil=female.pop()
            pairs=(malegerbil,femalegerbil)
            set_of_pairs.add(pairs)
        else:
            found=False
    return set_of_pairs

if __name__ == '__main__':
    male={'mgerbil1','mgerbil2','mgerbil3','mgerbil4','mgerbil5'}
    female={'fgerbil1','fgerbil2','fgerbil3','fgerbil4','fgerbil5'}
    print(mating_pairs(male,female))