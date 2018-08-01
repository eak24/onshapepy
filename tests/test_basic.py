from onshape.client import Client

# This is from a test document on OnShape, publicly available. It is a standard cube in a partStudio.
# https://cad.onshape.com/documents/8ec353ba00f37f447b5a61f5/w/04c36c786829759832bd3d1a/e/2918f0f5adfa39d3047f19d0
did = "8ec353ba00f37f447b5a61f5"
wid = "04c36c786829759832bd3d1a"
eid = "2918f0f5adfa39d3047f19d0"
vid = "b06892ff35a9ef5787d66485"

part_in_another_doc = {"did": "2d47b6abec9d1de1d2538372", "vid": "f2d396ba0762dc1f1dab3de1", "eid": "0639ea3c439aa0947744d29a"}
part = {"did": did, "wid": wid, "eid": eid, "vid": vid}
assembly = part.copy()
assembly["eid"]= "6f1f9c485ff1e639f4db63c0"

def setup_client():
    c = Client()
    return c

def test_new_doc():
    c=setup_client()
    # make a new document and grab the document ID and workspace ID
    new_doc = c.new_document(public=True).json()
    assert new_doc['name'] == 'Test Document'

def test_encode_configuration():
    c=setup_client()
    s = c.encode_configuration(did, eid, {"Length": "5 meters", "height": "2 meters"})
    assert s == 'Length=5+meters;height=2+meters'

def test_rename_document():
    c=setup_client()
    res = c.rename_document(did, "Test")
    assert res.status_code == 200

def test_insert_configured_part():
    c=setup_client()
    res = c.insert_configured_part(assembly, part_in_another_doc, {"h": "3 m"})
    assert res.status_code == 200

def test_get_configuration():
    c = setup_client()
    res = c.get_configuration(part)
    assert res.status_code == 200