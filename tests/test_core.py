from onshapepy.core.client import Client
from onshapepy.uri import Uri
from onshapepy.document import Document
import pytest
import json

# This is from a test document on OnShape, publicly available. It is a standard cube in a partStudio.

uri = Uri("https://cad.onshape.com/documents/2d47b6abec9d1de1d2538372/w/39e483948767f72c97d2792f/e/0639ea3c439aa0947744d29a")

def test_encode_configuration(client):
    s = client.encode_configuration(uri.did, uri.eid, {"Length": "5 meters", "height": "2 meters"})
    assert s == 'Length=5+meters;height=2+meters'

def test_rename_document(client):
    res = client.rename_document(uri.did, "Test")
    assert res.status_code == 200

def test_get_configuration(client):
    res = client.get_configuration(uri.as_dict())
    assert res.status_code == 200

def test_client_without_file():
    with pytest.raises(UserWarning):
        client = Client(conf_file="This file doesn't exist")

def test_document_setup(document, client):
    assert isinstance(document.name, str)


