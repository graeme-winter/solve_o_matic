# strategy pipeline customised to work at Diamond...

import os
import sys
import math

if not 'SOM_ROOT' in os.environ:
    raise RuntimeError, 'SOM_ROOT undefined'

if not os.environ['SOM_ROOT'] in sys.path:
    sys.path.append(os.path.join(os.environ['SOM_ROOT'], 'src'))
    
# import the modules that we will need

from modules.module_factory import module_factory

class strategy_pipeline:

    def __init__(self):
        
        self._working_directory = os.getcwd()
        self._factory = module_factory()
        self._image = None

        self._matrix = None
        self._spacegroup = None
        self._cell = None
        self._mosaic = None

        self._phi_start = None
        self._phi_end = None
        self._phi_width = None
        
        self._completeness = None

        self._resolution = None

        return

    def set_working_directory(self, working_directory):
        self._working_directory = working_directory
        self._ccp4_factory.set_working_directory(working_directory)
        return

    def set_image(self, image):
        self._image = image
        return

    def get_working_directory(self):
        return self._working_directory

    def get_spacegroup(self):
        return self._spacegroup
    
    def get_cell(self):
        return self._cell
    
    def get_mosaic(self):
        return self._mosaic
    
    def get_matrix(self):
        return self._matrix

    def get_phi_start(self):
        return self._phi_start
    
    def get_phi_end(self):
        return self._phi_end
    
    def get_phi_width(self):
        return self._phi_width

    def get_n_images(self):
        return self._n_images
    
    def get_completeness(self):
        return self._completeness

    def get_resolution(self):
        return self._resolution

    def strategy_pipeline(self):

        assert(self._image)

        cd = self._factory.characterise_diffraction()
        cd.set_image(self._image)
        cd.characterise()

        self._cell = cd.get_cell()
        self._spacegroup = cd.get_spacegroup()
        self._mosaic = cd.get_mosaic()

        cs = self._factory.calculate_strategy()
        cs.set_image(self._image)
        cs.set_matrix(cd.get_matrix())
        cs.set_spacegroup(cd.get_spacegroup())
        cs.set_mosaic(cd.get_mosaic())
        cs.calculate_strategy()
        
        self._phi_start = cs.get_phi_start()
        self._phi_end = cs.get_phi_end()
        self._phi_width = cs.get_phi_width()
        self._completeness = cs.get_completeness()
        self._resolution = cs.get_resolution()

        # derived things

        phi_range = self._phi_end - self._phi_start

        if phi_range < 0.0:
            phi_range += 360.0

        self._n_images = int(phi_range / self._phi_width)

        if self._n_images * self._phi_width < phi_range:
            self._n_images += 1

        return

if __name__ == '__main__':

    sp = strategy_pipeline()
    sp.set_image(sys.argv[1])

    sp.strategy_pipeline()

    print 'Unit cell: %.3f %.3f %.3f %.3f %.3f %.3f' % sp.get_cell()
    print 'Spacegroup: %s' % sp.get_spacegroup()
    print 'Mosaic: %.2f' % sp.get_mosaic()
    print 'Phi range: %.1f to %.1f' % (sp.get_phi_start(), sp.get_phi_end())
    print 'Phi width: %.1f' % sp.get_phi_width()
    print 'No. images: %d' % sp.get_n_images()
    print 'Completeness: %.2f' % sp.get_completeness()
    print 'Resolution:   %.2f' % sp.get_resolution()
    
                 
    
        
