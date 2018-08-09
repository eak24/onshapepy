from onshapepy.core.client import Client

def test_insert(cube, assembly):

    # Insert into the assembly
    assembly.insert(cube, Client())
