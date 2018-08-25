import pytest
from onshapepy.part import Part
from onshapepy.assembly import Assembly
from onshapepy.core.context import Context
from onshapepy.uri import Uri
from datetime import datetime


@pytest.fixture
def cube():
    return Part("https://cad.onshape.com/documents/2d47b6abec9d1de1d2538372/w/39e483948767f72c97d2792f/e/0639ea3c439aa0947744d29a")

@pytest.fixture
def versioned_cube():
    return Part("https://cad.onshape.com/documents/2d47b6abec9d1de1d2538372/v/460c8d693cb4140726eada1a/e/0639ea3c439aa0947744d29a")

@pytest.fixture
def assembly():
 return Assembly("https://cad.onshape.com/documents/8ec353ba00f37f447b5a61f5/w/04c36c786829759832bd3d1a/e/6f1f9c485ff1e639f4db63c0")

@pytest.fixture(scope="module")
def client():
    return Context().client

@pytest.fixture(scope="module")
def document(client):
    """This creates a new document for each test session based on the version of the code."""
    document = client.copy_workspace(Uri("https://cad.onshape.com/documents/2d47b6abec9d1de1d2538372/w/39e483948767f72c97d2792f/e/0639ea3c439aa0947744d29a").as_dict(), "OnshapePy Test " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    yield document
