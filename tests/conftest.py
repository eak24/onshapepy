import pytest
from onshapepy.part import Part
from onshapepy.assembly import Assembly
from onshapepy.core.client import Client

@pytest.fixture
def cube():
    return Part("https://cad.onshape.com/documents/2d47b6abec9d1de1d2538372/w/39e483948767f72c97d2792f/e/0639ea3c439aa0947744d29a")

@pytest.fixture
def assembly():
 return Assembly("https://cad.onshape.com/documents/8ec353ba00f37f447b5a61f5/w/04c36c786829759832bd3d1a/e/6f1f9c485ff1e639f4db63c0")

@pytest.fixture
def client():
    return Client()
