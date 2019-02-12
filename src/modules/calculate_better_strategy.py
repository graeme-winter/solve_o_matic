import os
import sys
import math

if not 'SOM_ROOT' in os.environ:
    raise RuntimeError, 'SOM_ROOT undefined'

if not os.environ['SOM_ROOT'] in sys.path:
    sys.path.append(os.path.join(os.environ['SOM_ROOT'], 'lib'))

# external modules used here

# FIXME add an interrogate_image module - e.g. from fast_dp

from interrogate_image import interrogate_image

# now import the factories that we will need

from wrappers.mosflm.mosflm_factory import mosflm_factory
from wrappers.embl.embl_factory import embl_factory

# this will -
#
# calculate an inscribed circle resolution
# calculate a native and anomalous strategy

class calculate_better_strategy:

    def __init__(self):
        self._working_directory = os.getcwd()
        self._mosflm_factory = mosflm_factory()
        self._embl_factory = embl_factory()

        self._image = None

        self._interrogate_image = None
        self._images = []

        self._template = None
        self._directory = None
        self._beam = None
        self._matrix = None
        self._spacegroup = None
        self._mosaic = None
        self._anomalous = False

        self._resolution = None

        self._phi_start = None
        self._phi_end = None
        self._phi_width = None

        self._completeness = None

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
        self._template = self._interrogate_image.get_template()
        self._directory = self._interrogate_image.get_directory()
        return

    def set_spacegroup(self, spacegroup):
        self._spacegroup = spacegroup
        return

    def set_mosaic(self, mosaic):
        self._mosaic = mosaic
        return

    def set_matrix(self, matrix):
        self._matrix = matrix
        return

    def set_anomalous(self, anomalous = True):
        self._anomalous = anomalous
        return

    def set_beam(self, beam):
        self._beam = beam
    
    def get_phi_start(self):
        return self._phi_start

    def get_phi_end(self):
        return self._phi_end

    def get_phi_width(self):
        return self._phi_width

    def get_completeness(self):
        return self._completeness

    def get_resolution(self):
        return self._resolution

    # real methods

    def select_images(self):
        if len(self._interrogate_image.get_images()) < 20:
            self._images = self._interrogate_image.get_images()
        else:
            raise RuntimeError, 'implement something here'

        return

    def resolution(self):
        ii = self._interrogate_image
        size = ii.get_size()
        pixel = ii.get_pixel()
        d = ii.get_distance()
        l = ii.get_wavelength()

        r = 0.25 * (size[0] * pixel[0] + size[1] * pixel[1])

        theta = 0.5 * math.atan(r / d)

        self._resolution = l / (2 * math.sin(theta))

        return

    def strategy(self):
        best = self._embl_factory.strategy()
        if self._anomalous:
            best.write_log_file('strategy_anomalous.log')
        else:
            best.write_log_file('strategy_native.log')

        # FIXME need to get this from somewhere
        best.set_detector('pilatus6m')
        best.set_t_ref(0.5)
        best.set_T_max(807)
        best.set_t_min(0.067)
        best.set_trans_ref(25.0)
        best.set_S_max(10.0)
        best.set_w_min(0.1)

        # FIXME these should ideally be optional but...
        best.set_M_min(3.0)
        best.set_C_min(99.0)
        best.set_i2s(2.0)
        best.set_mos_dat('bestfile.dat')
        best.set_mos_par('bestfile.par')
        best.add_mos_hkl('bestfile.hkl')
        best.set_anomalous(self._anomalous)
        best.strategy()
        self._phi_start = best.get_phi_start()
        self._phi_end = best.get_phi_end()
        self._phi_width = best.get_phi_width()
        self._completeness = best.get_completeness()
        self._resolution = best.get_resolution()
        return

    def integrate(self):
        mi = self._mosflm_factory.integrate()
        mi.write_log_file('integrate.log')
        mi.set_matrix(self._matrix)
        mi.set_resolution(self._resolution)
        mi.set_mosaic(self._mosaic)
        mi.set_spacegroup(self._spacegroup)
        mi.set_template(self._template)
        mi.set_directory(self._directory)
        mi.set_beam(self._beam)
        if self._anomalous:
            mi.set_anomalous(self._anomalous)
        for image in self._images:
            mi.add_image(image)
        mi.integrate()
        return

    def calculate_strategy(self):

        self.select_images()
        self.resolution()
        self.integrate()
        self.strategy()

        return


if __name__ == '__main__':

    from characterise_diffraction import characterise_diffraction

    cd = characterise_diffraction()
    cd.set_image(sys.argv[1])
    cd.characterise()

    print 'Unit cell: %.3f %.3f %.3f %.3f %.3f %.3f' % cd.get_cell()
    print 'Spacegroup: %s' % cd.get_spacegroup()
    print 'Mosaic: %.2f' % cd.get_mosaic()

    cs = calculate_strategy()
    cs.set_image(sys.argv[1])
    cs.set_matrix(cd.get_matrix())
    cs.set_spacegroup(cd.get_spacegroup())
    cs.set_mosaic(cd.get_mosaic())
    cs.calculate_strategy()

    print 'Native'
    print 'Phi range: %.1f to %.1f' % (cs.get_phi_start(), cs.get_phi_end())
    print 'Phi width: %.1f' % cs.get_phi_width()
    print 'Completeness: %.2f' % cs.get_completeness()

    cs = calculate_strategy()
    cs.set_image(sys.argv[1])
    cs.set_matrix(cd.get_matrix())
    cs.set_spacegroup(cd.get_spacegroup())
    cs.set_mosaic(cd.get_mosaic())
    cs.set_anomalous(True)
    cs.calculate_strategy()

    print 'Anomalous'
    print 'Phi range: %.1f to %.1f' % (cs.get_phi_start(), cs.get_phi_end())
    print 'Phi width: %.1f' % cs.get_phi_width()
    print 'Completeness: %.2f' % cs.get_completeness()
