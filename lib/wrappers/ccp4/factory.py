import os

from cad import Cad
from freerflag import Freerflag
from mtzdump import Mtzdump
from pdbset import Pdbset
from reindex import Reindex
from truncate import Truncate
from unique import Unique

class ccp4_factory:

    def __init__(self):
        self._working_directory = os.getcwd()
        return

    def set_working_directory(self, working_directory):
        self._working_directory = working_directory
        return

    def cad(self):
        _cad = Cad()
        _cad.set_working_directory(self._working_directory)
        return _cad

    def freerflag(self):
        _freerflag = Freerflag()
        _freerflag.set_working_directory(self._working_directory)
        return _freerflag

    def mtzdump(self):
        _mtzdump = Mtzdump()
        _mtzdump.set_working_directory(self._working_directory)
        return _mtzdump

    def pdbset(self):
        _pdbset = Pdbset()
        _pdbset.set_working_directory(self._working_directory)
        return _pdbset

    def reindex(self):
        _reindex = Reindex()
        _reindex.set_working_directory(self._working_directory)
        return _reindex

    def truncate(self):
        _truncate = Truncate()
        _truncate.set_working_directory(self._working_directory)
        return _truncate

    def unique(self):
        _unique = Unique()
        _unique.set_working_directory(self._working_directory)
        return _unique



    
