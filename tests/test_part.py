from onshapepy.part import Config
import pint
import pytest

u = pint.UnitRegistry()

def test_get_part_params(cube):
    print(cube.params)
    assert cube.params['has_fillet']
    assert 100*u.mm == cube.params['L']
    assert 100*u.mm == cube.params['h']
    assert 'Default' == cube.params['fillet_type']
    assert 100*u.mm == cube.params['w']


def test_set_part_params(cube):
    cube.config.update({'h': 200 * u.mm})
    assert 200*u.mm == cube.params['h']
    #reset to original
    cube.config.update({'h': 100 * u.mm})
    assert 100 * u.mm == cube.params['h']