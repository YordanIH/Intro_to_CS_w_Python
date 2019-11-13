#Nesting Loops in Loops
outer = ['Li','Na','K']
inner = ['F', 'Cl', 'Br']
for metal in outer:
    for halogen in inner:
        print(metal + halogen)
