import os
import sys

if not os.environ.has_key('XIA2CORE_ROOT'):
    raise RuntimeError, 'XIA2CORE_ROOT not defined'

sys.path.append(os.path.join(os.environ['XIA2CORE_ROOT'],
                             'Python'))

from Driver.DriverFactory import DriverFactory
from Decorators.DecoratorFactory import DecoratorFactory

def Pointless(DriverType = None):

    DriverInstance = DriverFactory.Driver(DriverType)
    CCP4DriverInstance = DecoratorFactory.Decorate(DriverInstance, 'ccp4')

    class PointlessWrapper(CCP4DriverInstance.__class__):

        def __init__(self):
            # generic things
            CCP4DriverInstance.__class__.__init__(self)
            self.set_executable('pointless.test')
            
            return

        def check_origin(self):
            self.check_hklin()
            self.check_xyzin()
            self.check_hklout()

            self.start()

            self.close_wait()
            self.check_for_errors()
            self.check_ccp4_errors()

            # get the reindexing operation which was applied...

            return

    return PointlessWrapper()

if __name__ == '__main__':


