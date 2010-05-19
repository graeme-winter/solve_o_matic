import os
import sys

if not 'CCP4' in os.environ:
    raise RuntimeError, 'CCP4 undefined'

class check_pdb_ligands:
    '''A class to check that the ligands in a PDB file all appear in the
    CCP4 monomer dictionary.'''

    def __init__(self):

        self._known_monomers = []

        monomer = os.path.join(os.environ['CCP4'], 'lib', 'data', 'monomers')

        for dirpath, dirnames, filenames in os.walk(monomer):
            for filename in filenames:
                self._known_monomers.append(filename.replace('.cif', ''))

        return

if __name__ == '__main__':

    cpl = check_pdb_ligands()

