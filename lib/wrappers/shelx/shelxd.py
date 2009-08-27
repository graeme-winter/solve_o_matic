import os
import sys

if not os.environ.has_key('XIA2CORE_ROOT'):
    raise RuntimeError, 'XIA2CORE_ROOT not defined'

sys.path.append(os.path.join(os.environ['XIA2CORE_ROOT'],
                             'Python'))

from Driver.DriverFactory import DriverFactory

def Shelxd(DriverType = None):

    DriverInstance = DriverFactory.Driver(DriverType)

    class ShelxdWrapper(DriverInstance.__class__):

        def __init__(self):
            DriverInstance.__class__.__init__(self)

            self.set_executable('shelxd')

            self._name = None

        def set_name(self, name):
            self._name = name

            return

        def shelxd(self):
            if not self._name:
                raise RuntimeError, 'name not assigned'

            # check that the input files are present according to self._name

            self.add_command_line('%s_fa' % self._name)

            self.start()
            self.close_wait()

            # FIXME get the final CC weak from the .lst file

            return

    return ShelxdWrapper()

if __name__ == '__main__':
    # FIXME add test
    pass
