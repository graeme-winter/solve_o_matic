import os
import sys

if not 'SOM_ROOT' in os.environ:
    raise RuntimeError, 'SOM_ROOT undefined'

if not os.environ['SOM_ROOT'] in sys.path:
    sys.path.append(os.path.join(os.environ['SOM_ROOT'], 'lib'))

# external modules used here

# FIXME add an interrogate_image module - e.g. from fast_dp

from interrogate_image import interrogate_image
    
# now import the factories that we will need

from wrappers.mosflm.mosflm_factory import mosflm_factory

# this will -
#
# read the image header from the first image
# see what images we have available
# select useful images
# run indexing / characterisation
# return these results and also a resolution limit

class characterise_diffraction:

    def __init__(self):
        self._working_directory = os.getcwd()
        self._mosflm_factory = mosflm_factory()

        self._image = None

        self._interrogate_image = None
        self._images = []
        
        self._matrix = None
        self._spacegroup = None
        self._cell = None
        self._mosaic = None

        return

    def set_working_directory(self, working_directory):
        self._working_directory = working_directory
        self._mosflm_factory.set_working_directory(working_directory)
        return

    def get_working_directory(self):
        return self._working_directory
    
    def set_image(self, image):
        self._image = image
        self._interrogate_image = interrogate_image()
        self._interrogate_image.set_image(image)
        return

    def get_spacegroup(self):
        return self._spacegroup
    
    def get_cell(self):
        return self._cell
    
    def get_mosaic(self):
        return self._mosaic
    
    def get_matrix(self):
        return self._matrix

    # useful methods

    def select_images(self):
        if len(self._interrogate_image.get_images()) < 20:
            self._images = self._interrogate_image.get_images()
        else:
            raise RuntimeError, 'implement something here'

        return

    def index(self):
        ii = self._interrogate_image
        mi = self._mosflm_factory.index()

        mi.write_log_file('index.log')
        
        mi.set_template(ii.get_template())
        mi.set_directory(ii.get_directory())

        for image in self._images:
            mi.add_image(image)

        mi.index()

        self._cell = mi.get_cell()
        self._spacegroup = mi.get_spacegroup()
        self._matrix = mi.get_matrix()
        self._mosaic = mi.get_mosaic()

    def characterise(self):

        self.select_images()
        self.index()

        return

if __name__ == '__main__':
    
    cd = characterise_diffraction()
    cd.set_image(sys.argv[1])
    cd.characterise()

    print 'Unit cell: %.3f %.3f %.3f %.3f %.3f %.3f' % cd.get_cell()
    print 'Spacegroup: %s' % cd.get_spacegroup()
    print 'Mosaic: %.2f' % cd.get_mosaic()
        
        
    
        
    
