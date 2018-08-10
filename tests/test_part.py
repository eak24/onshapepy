from onshapepy.part import Config
import pint

u = pint.UnitRegistry()

def test_build_cube(cube, client, assembly):
    cube.params.update({"h": 5*u.meter})
    res = assembly.insert(cube, client)

    assert res.status_code == 200

def test_build_cube_missing_param(cube, client, assembly):
    # a missing param doesnt get changed.
    cube.params.update({"missing_param": 1*u.meter})
    res = assembly.insert(cube, client)

    assert res.status_code == 200


def test_config_class(client):
    config = Config("https://cad.onshape.com/documents/2d47b6abec9d1de1d2538372/w/39e483948767f72c97d2792f/e/0639ea3c439aa0947744d29a")
    assert config.get_params()["h"]