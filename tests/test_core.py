from onshapepy.core.client import Client
from onshapepy.uri import Uri

# This is from a test document on OnShape, publicly available. It is a standard cube in a partStudio.
# https://cad.onshape.com/documents/8ec353ba00f37f447b5a61f5/w/04c36c786829759832bd3d1a/e/2918f0f5adfa39d3047f19d0
uri = Uri("https://cad.onshape.com/documents/8ec353ba00f37f447b5a61f5/w/04c36c786829759832bd3d1a/e/2918f0f5adfa39d3047f19d0")

def test_new_doc(client):
    # make a new document and grab the document ID and workspace ID
    new_doc = client.new_document(public=True).json()
    assert new_doc['name'] == 'Test Document'

def test_encode_configuration(client):
    s = client.encode_configuration(uri.did, uri.eid, {"Length": "5 meters", "height": "2 meters"})
    assert s == 'Length=5+meters;height=2+meters'

def test_rename_document(client):
    res = client.rename_document(uri.did, "Test")
    assert res.status_code == 200

def test_get_configuration(client):
    res = client.get_configuration(uri.as_dict())
    assert res.status_code == 200