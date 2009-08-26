import os
import sys

if not os.environ.has_key('XIA2CORE_ROOT'):
    raise RuntimeError, 'XIA2CORE_ROOT not defined'

sys.path.append(os.path.join(os.environ['XIA2CORE_ROOT'],
                             'Python'))

from Driver.DriverFactory import DriverFactory
from Decorators.DecoratorFactory import DecoratorFactory

def Refmac5(DriverType = None):

    DriverInstance = DriverFactory.Driver(DriverType)
    CCP4DriverInstance = DecoratorFactory.Decorate(DriverInstance, 'ccp4')

    class Refmac5Wrapper(CCP4DriverInstance.__class__):

        def __init__(self):
            # generic things
            CCP4DriverInstance.__class__.__init__(self)
            self.set_executable('refmac5')

            # column labels: set the defaults to what we are expecting
            # from the data preparation step

            self._labin = {
                'FP':'F',
                'SIGFP':'SIGF',
                'FREE':'FreeR_flag'
                }

            self._labout = {
                'FC':'FC',
                'PHIC':'PHIC',
                'FWT':'2FOFCWT',
                'PHWT':'PH2FOFCWT',
                'DELFWT':'FOFCWT',
                'PHDELWT':'PHFOFCWT'
                }

            # possible refinement modes

            self._mode_restrained = 'RESTRAINED'
            self._mode_rigidbody = 'RIGIDBODY'

            self._mode = None
            
            return

        def set_labin(self, program_label, file_label):
            self._labin[program_label] = file_label
            return

        def set_labout(self, program_label, file_label):
            self._labout[program_label] = file_label
            return

        def set_mode_rigidbody(self):
            self._mode = self._mode_rigidbody
            return

        def set_mode_restrained(self):
            self._mode = self._mode_restrained
            return

        def refmac5(self):
            self.check_hklin()
            self.check_xyzin()
            self.check_hklout()
            self.check_xyzout()

            if not self._mode in [self._mode_restrained, self._mode_rigidbody]:
                raise RuntimeError, 'refinement mode %s not supported' % \
                      self._mode

            self.start()

            labin_command = 'labin'

            for token in self._labin:
                labin_command+= ' %s=%s' % (token, self._labin[token])

            labout_command = 'labout'

            for token in self._labout:
                labout_command+= ' %s=%s' % (token, self._labout[token])

            self.input(labin_command)
            self.input(labout_command)

            # N.B. sticking with the program defaults as far as possible
            # matrix weighting set to 0.2 => for lower resolution data.
            # The values chosen for the parameters below originated
            # from Dave Brown's example script, but should probably be
            # configurable at some point in the future...

            if self._mode == self._mode_restrained:
                self.input(
                    'make hydrogen all hout no cispeptide yes ssbridge yes')
                self.input('refinement type restrained')
                self.input('weight matrix 0.2')
                self.input('scale type simple lssc anisotropic experimental')
                self.input('solvent yes vdwprob 1.4 ionprob 0.8 mshrink 0.8')
                self.input('ncycle 15')
                
            elif self._mode == self._mode_rigidbody:
                self.input('refinement type rigidbody resolution 15 3.5')
                self.input('scale type simple lssc anisotropic experimental')
                self.input('solvent yes vdwprob 1.4 ionprob 0.8 mshrink 0.8')
                self.input('rigidbody ncycle 10')

            else:
                pass
                
            self.close_wait()

            self.check_for_errors()
            self.check_ccp4_errors()

            # at this stage I will probably want to get some of the information
            # from the refmac log graphs or something...

            return

    return Refmac5Wrapper()

if __name__ == '__main__':
    # FIXME write test...
    pass

