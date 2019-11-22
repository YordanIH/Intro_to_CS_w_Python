from typing import TextIO
from io import StringIO

def read_molecule(reader: TextIO) -> list:
    line = reader.readline()
    if not line:
        return None

    key, name = line.split()
    molecule=[name]

    reading = True
    serial_number =1
    while reading:

        line = reader.readline()
        if line.startswith('END'):
            reading = False
        else:
            key,num,atom_type,x,y,z= line.split()
            if int(num) != serial_number:
                print("Serial number {} was expected and insted received {}".format(serial_number,num))
            molecule.append([atom_type,x,y,z])
            serial_number +=1
            
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