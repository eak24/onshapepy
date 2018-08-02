from tests.test_client import setup_client
from onshapepy.part import Part
from tests.test_client import assembly
from tests.test_client import part

my_cube = Part("2d47b6abec9d1de1d2538372", "f2d396ba0762dc1f1dab3de1", "0639ea3c439aa0947744d29a")

def test_build_cube():
    c = setup_client()
    my_cube.params.update({"h": "5 meter"})
    res = c.insert_configured_part(assembly, my_cube.uri, my_cube.params)

    assert res.status_code == 200

def test_build_cube_missing_param():
    # a missing param doesnt get changed.
    c = setup_client()
    my_cube.params.update({"missing_param": "5 meter"})
    res = c.insert_configured_part(assembly, my_cube.uri, my_cube.params)

    assert res.status_code == 200


def test_get_current_configuration():
    my_cube.update_configuration()

    assert my_cube.params["h"]