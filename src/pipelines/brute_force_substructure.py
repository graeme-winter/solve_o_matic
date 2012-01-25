import os
import sys

#if not 'SOM_ROOT' in os.environ:
#    raise RuntimeError, 'SOM_ROOT undefined'
#
#if not os.environ['SOM_ROOT'] in sys.path:
#    sys.path.append(os.path.join(os.environ['SOM_ROOT'], 'src'))
    
from cctbx.sgtbx import space_group, space_group_symbols
from cctbx.uctbx import unit_cell

def guess_nha(cell, pointgroup):
    '''Guess # heavy atoms likely to be in here (as a floating point number)
    based on Matthews coefficient, average proportion of methionine in
    protein sequences and typical mass of an amino acid.'''

    sg = space_group(space_group_symbols(pointgroup).hall())    
    uc = unit_cell(cell)

    n_ops = len(sg.all_ops())

    v_asu = uc.volume() / n_ops

    return 0.023 * v_asu / (2.7 * 128)

def generate_enantiomorph_unique_spacegroups(pointgroup):
    '''Generate an enantiomorph unique list of chiral spacegroups which
    share a pointgroup with this pointgroup.'''
    
    sg = space_group(space_group_symbols(pointgroup).hall())
    pg = sg.build_derived_patterson_group()

    eu_list = []

    for j in range(1, 231):
        sg_test = space_group(space_group_symbols(j).hall())

        if not sg_test.is_chiral():
            continue
        
        pg_test = sg_test.build_derived_patterson_group()
        if pg_test == pg:
            enantiomorph = sg_test.change_basis(
                sg_test.type().change_of_hand_op())
            if not sg_test in eu_list and not \
               enantiomorph in eu_list:
                eu_list.append(sg_test)

    return [
        sg_test.type().universal_hermann_mauguin_symbol().replace(' ', '') \
        for sg_test in eu_list]


if __name__ == '__main__':

    cell = [51.6432, 51.6432, 157.6767, 90.0000, 90.0000, 90.0000]
    pointgroup = 'P422'

    print guess_nha(cell, pointgroup)
    print generate_enantiomorph_unique_spacegroups(pointgroup)

