#!/usr/bin/env python
# sites.py
#
# An object to store atomic position information, particularly for
# substructure searches. N.B. this may be input (i.e. we don't know where
# they are, but we do know what there are and how many there should be) or
# output, with the positions in the asymmetric unit included, in Angstroms.
#
# N.B. this will also include some crystallographic functionality, for
# example inverting the substructure, calculating fractional coordinates
# and so on.

import math

class sites:
    '''A class to represent heavy atom substructure information.'''

    def __init__(self, species = None, number = 0):
        self._sites = { }
        self._species = species
        self._number = number
        self._unit_cell = None
        self._symmetry = None

        return

    def self_sites_cartesian(self, sites):
        pass

    def self_sites_fractional(self, sites):
        pass

    def get_sites_cartesian(self):
        pass

    def get_sites_fractional(self):
        pass

    def set_unit_cell(self, unit_cell):
        self._unit_cell = unit_cell
        return

    def set_symmatry(self, symmetry):
        # check this
        self._symmetry = symmetry
        return

    def set_species(self, species):
        # check this
        self._species = species
        return

    def set_number(self, number):
        self._number = number
        return

    def get_species(self):
        return self._species

    def get_number(self):
        return self._number

    def get_unit_cell(self):
        return self._unit_cell

    def get_symmetry(self):
        return self._symmetry

    def read_pdb(self, pdb):
        pass

if __name__ == '__main__':
    pass
