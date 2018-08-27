import pytest
from onshapepy.part import Part
from onshapepy.assembly import Assembly
from onshapepy.document import Document
from onshapepy.core.context import Context
from onshapepy.uri import Uri
from datetime import datetime


@pytest.fixture
def cube(document):
    return Part(document.find_element("cube"))


@pytest.fixture
def versioned_cube():
    return Part("https://cad.onshape.com/documents/2d47b6abec9d1de1d2538372/v/460c8d693cb4140726eada1a/e/"
                "0639ea3c439aa0947744d29a")


@pytest.fixture
def assembly(document):
    return Assembly(document.find_element("pyramid"))


@pytest.fixture(scope="module")
def client():
    return Context().client


@pytest.fixture(scope="module")
def document(client):
    """This creates a new document for each test session based on the version of the code."""
    document = Document("https://cad.onshape.com/documents/2d47b6abec9d1de1d2538372/"
                        "w/39e483948767f72c97d2792f", copy=True, name="OnshapePy Test " +
                                                                      datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    yield document
    # Clean up the document after tests are run and make sure it is in the trash
    document.delete()
    document.update()
    assert document.json["trash"]
