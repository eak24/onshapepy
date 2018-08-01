from onshape.part import Part
from onshape.assembly import Assembly
from onshape.client import Client

# load the client for this part
my_cube = Part("2d47b6abec9d1de1d2538372", "f2d396ba0762dc1f1dab3de1", "0639ea3c439aa0947744d29a")
my_pyramid = Assembly("8ec353ba00f37f447b5a61f5", "04c36c786829759832bd3d1a", "1a1dbfb527f96cc00c05e2ed")
c = Client()

def test_insert():

    # set various parameters
    my_cube.params["h"] = {}
    my_cube.params["h"]["value"] = 5 * 20
    my_cube.params["h"]["units"] = "inch"

    # Insert into the assembly
    my_pyramid.insert(my_cube, c)