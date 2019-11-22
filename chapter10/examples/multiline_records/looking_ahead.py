from typing import TextIO

def read_all_molecules(reader: TextIO) -> list:
    """Read zero or more molecules from reader,
    returning a list of the molecules read.
    """

    result = []
    line = reader.readline()
    while line:
        molecule, line  = read_molecule(reader, line)
        result.append(molecule)
    return result

def read_molecule(reader: TextIO, line: str) -> list:
    """Read a molecule from reader, where line refers to the first line of
    the molecule to be read. Return the molecule and the first line after it
    (or the empty string if the end of file has been reached).
    """
    
    fields = line.split()
    molecule = [fields[1]]

    line = reader.readline()

    while line and not line.startswith('COMPND'):
        fields = line.split()
        if fields[0]== 'ATOM':
            key, num, atom_type, x, y, z = fields
            molecule.append([atom_type, x, y, z])
        line = reader.readline()

    return molecule, line


if __name__=='__main__':
    molecule_file = open("multimol2.pdb", 'r')
    molecules = read_all_molecules(molecule_file)
    molecule_file.close()
    print(molecules)
