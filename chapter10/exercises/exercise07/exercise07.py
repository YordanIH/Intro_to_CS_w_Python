from typing import TextIO
from io import StringIO

def read_molecule(reader: TextIO) -> list:
    line = reader.readline()
    if not line:
        return None

    if not (line.startswith('CMNT') or line.isspace()):
        key, name = line.split()

        molecule = [name]
    else:
        molecule = None

    reading = True
    while reading:
        line = reader.readline()
        if line.startswith('END'):
            reading = False
        elif not (line.startswith('CMNT') or line.isspace()):
            key, num, atom_type, x, y, z = line.split()
            if molecule == None:
                molecule = []
            molecule.append([atom_type, x, y, z])
    return molecule

def read_all_molecules(reader: TextIO) -> list:
    result = []
    reading = True
    while reading:
        molecule = read_molecule(reader)
        if molecule:
            result.append(molecule)
        else:
            reading = False
    return result

if __name__=='__main__':
    molecule_file = open("multimol.pdb", 'r')
    molecules = read_all_molecules(molecule_file)
    molecule_file.close()
    print(molecules)