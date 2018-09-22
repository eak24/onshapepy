import pytest
from onshapepy.part import Part
from onshapepy.assembly import Assembly
from onshapepy.document import Document
from onshapepy.uri import Uri
from datetime import datetime
from onshapepy.core.client import c


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
    return c

@pytest.fixture(scope="module")
def document(client, onshape_version, onshape_document):
    """This creates a new document for each test session based on the version of the code."""
    # make a name based on the current time
    name = "OnshapePy Test " + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    document = Document(onshape_document,
                        copy=True, name=name,
                        version=onshape_version)
    yield document
    # Clean up the document after tests are run and make sure it is in the trash
    document.delete()
    document.update()
    assert document.json["trash"]


# Set up command line options for users to customize tests.
def pytest_addoption(parser):

    parser.addoption("--onshape-version", action="store", default=None,
        help="version name of OnShape test document to run tests against. Defaults to current workspace.")

    url = "https://cad.onshape.com/documents/2d47b6abec9d1de1d2538372/w/39e483948767f72c97d2792f/e/180c6dd1839132a442f747ae"
    parser.addoption("--onshape-document", action="store", default=url,
                     help="The URL of the onshape document that will be tested against.")


@pytest.fixture(scope="module")
def onshape_version(request):
    return request.config.getoption("--onshape-version")

@pytest.fixture(scope="module")
def onshape_document(request):
    return request.config.getoption("--onshape-document")
