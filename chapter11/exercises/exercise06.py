def least_likely(dictionary: dict) -> str:
    smallest=1
    name=''

    for particle in dictionary:
        probability=dictionary[particle]
        if smallest>probability:
            smallest=probability
            name=particle
    return name

dictionary={'neutron': 0.55, 'proton': 0.21, 'meson': 0.03, 'muon': 0.07, 'neutrino': 0.14}
print(least_likely(dictionary))

        

        
