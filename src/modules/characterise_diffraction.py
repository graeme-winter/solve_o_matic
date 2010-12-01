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


