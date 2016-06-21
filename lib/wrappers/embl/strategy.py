import os
import sys

if not os.environ.has_key('XIA2CORE_ROOT'):
    raise RuntimeError, 'XIA2CORE_ROOT not defined'

sys.path.append(os.path.join(os.environ['XIA2CORE_ROOT'],
                             'Python'))

from Driver.DriverFactory import DriverFactory

def BestStrategy(DriverType = None):

    DriverInstance = DriverFactory.Driver(DriverType)

    class BestStrategyWrapper(DriverInstance.__class__):

        def __init__(self):
            DriverInstance.__class__.__init__(self)

            self.set_executable('best')

            # Input parameters - lower case per frame
            # upper case whole scan

            self._detector = None
            self._t_ref = None
            self._t_min = None
            self._T_max = None
            self._S_max = 10.0
            self._w_min = 0.05
            self._M_min = 3.0
            self._C_min = 0.99
            self._i2s = 2.0
            self._sensitivity = 1.0
            self._shape = 1.0
            self._mos_dat = None
            self._mos_par = None
            self._mos_hkl = []

            return

        def set_detector(self, detector):
            self._detector = detector

        def set_t_ref(self, t_ref):
            self._t_ref = t_ref

        def set_T_max(self, T_max):
            self._T_max = T_max

        def set_t_min(self, t_min):
            self._t_min = t_min

        def set_S_max(self, S_max):
            self._S_max = S_max

        def set_w_min(self, w_min):
            self._w_min = w_min

        def set_M_min(self, M_min):
            self._M_min = M_min

        def set_C_min(self, C_min):
            self._C_min = C_min

        def set_i2s(self, i2s):
            self._i2s = i2s

        def set_sensitivity(self, sensitivity):
            self._sensitivity = sensitivity

        def set_shape(self, shape):
            self._shape = shape

        def set_mos_dat(self, mos_dat):
            self._mos_dat = mos_dat

        def set_mos_par(self, mos_par):
            self._mos_par = mos_par

        def add_mos_hkl(self, mos_hkl):
            self._mos_hkl.append(mos_hkl)




        def best_strategy(self):

            return

    return BestStrategyWrapper()

if __name__ == '__main__':
    # FIXME add test
    pass



