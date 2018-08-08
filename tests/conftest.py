import pytest
from onshapepy.part import Part
from onshapepy.assembly import Assembly

@pytest.fixture
def cube():
    return Part("2d47b6abec9d1de1d2538372", "f2d396ba0762dc1f1dab3de1", "0639ea3c439aa0947744d29a")

@pytest.fixture
def assembly():
 return Assembly("8ec353ba00f37f447b5a61f5", "04c36c786829759832bd3d1a", "1a1dbfb527f96cc00c05e2ed")
