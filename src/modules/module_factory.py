import os

from intensity_data_preparation import intensity_data_preparation as \
     _intensity_data_preparation
from pdb_preparation import pdb_preparation as _pdb_preparation
from rigid_body_refine import rigid_body_refine as _rigid_body_refine
from refine import refine as _refine
from interrogate_mtz import interrogate_mtz as _interrogate_mtz

class module_factory:

    def __init__(self):
        self._working_directory = os.getcwd()
        return

    def set_working_directory(self, working_directory):
        self._working_directory = working_directory
        return

    def intensity_data_preparation(self):
        intensity_data_preparation = _intensity_data_preparation()
        intensity_data_preparation.set_working_directory(
            self._working_directory)
        return intensity_data_preparation

    def pdb_preparation(self):
        pdb_preparation = _pdb_preparation()
        pdb_preparation.set_working_directory(self._working_directory)
        return pdb_preparation

    def rigid_body_refine(self):
        rigid_body_refine = _rigid_body_refine()
        rigid_body_refine.set_working_directory(self._working_directory)
        return rigid_body_refine

    def refine(self):
        refine = _refine()
        refine.set_working_directory(self._working_directory)
        return refine

    def interrogate_mtz(self):
        interrogate_mtz = _interrogate_mtz()
        interrogate_mtz.set_working_directory(self._working_directory)
        return interrogate_mtz

    

        
