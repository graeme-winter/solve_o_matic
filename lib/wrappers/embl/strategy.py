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

            return

        def best_strategy(self):

            return

    return BestStrategyWrapper()

if __name__ == '__main__':
    # FIXME add test
    pass



