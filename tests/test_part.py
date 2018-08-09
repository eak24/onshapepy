def test_build_cube(cube, client, assembly):
    cube.params.update({"h": {"value":"5", "units":"meter"}})
    res = assembly.insert(cube, client)

    assert res.status_code == 200

def test_build_cube_missing_param(cube, client, assembly):
    # a missing param doesnt get changed.
    cube.params.update({"missing_param": {"value":"5", "units":"meter"}})
    res = assembly.insert(cube, client)

    assert res.status_code == 200


def test_get_current_configuration(cube, client):
    cube.update_configuration(client)

    assert cube.params["h"]