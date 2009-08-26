import os
import sys

if not 'SOM_ROOT' in os.environ:
    raise RuntimeError, 'SOM_ROOT undefined'

if not os.environ['SOM_ROOT'] in sys.path:
    sys.path.append(os.path.join(os.environ['SOM_ROOT'], 'lib'))
    
# now import the factories that we will need

from wrappers.ccp4.ccp4_factory import ccp4_factory

# first pass this module will just provide a wrapper for the rigid body
# refinement in refmac5...

class rigid_body_refine:

    def __init__(self):
        self._working_directory = os.getcwd()
        self._ccp4_factory = ccp4_factory()

        self._hklin = None
        self._hklout = None

        self._xyzin = None
        self._xyzout = None

        return

    def set_working_directory(self, working_directory):
        self._working_directory = working_directory
        self._ccp4_factory.set_working_directory(working_directory)
        return

    def get_working_directory(self):
        return self._working_directory

    def set_hklin(self, hklin):
        self._hklin = hklin
        return

    def set_xyzin(self, xyzin):
        self._xyzin = xyzin
        return

    def set_xyzout(self, xyzout):
        self._xyzout = xyzout
        return

    def ccp4(self):
        return self._ccp4_factory

    def rigid_body_refine(self):
        if not self._hklin:
            raise RuntimeError, 'hklin not defined'

        if not self._xyzin:
            raise RuntimeError, 'xyzin not defined'

        if not self._xyzout:
            raise RuntimeError, 'xyzout not defined'

        name = os.path.split(self._hklin)[-1][:-4]

        hklout = os.path.join(self.get_working_directory(),
                              '%s_refmac5_rb.mtz' % name)

        refmac5 = self.ccp4().refmac5()

        refmac5.set_hklin(self._hklin)
        refmac5.set_hklout(hklout)
        refmac5.set_xyzin(self._xyzin)
        refmac5.set_xyzout(self._xyzout)

        refmac5.set_mode_rigidbody()
        refmac5.refmac5()

        os.remove(hklout)

        return

if __name__ == '__main__':
    # then I should run a test...
    pass


        
    
    
        
