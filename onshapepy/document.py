"""Represents an Onshape document"""
from onshapepy.core.context import Context
from onshapepy.uri import Uri
import json


class Document:
    def __init__(self, name, uri=None, copy=True):
        """Create a document. If a URI is passed in and copy is set to true, then make a copy of that workspace. If
        there is a uri, but copy is set to false, load the document specified. If there is no uri, make a new
        document."""
        c = Context().client

        self.json = None

        # Make a copy:
        if uri and copy:
            res = c.copy_workspace(uri.as_dict(), name)
            payload = res.json()
            url = 'https://cad.onshape.com/documents/' + payload["newDocumentId"] + "/w/" + payload["newWorkspaceId"]
            self.uri = Uri(url)
        # Reference an existing doc:
        elif uri:
            self.uri = uri
        # Make a new, blank doc:
        else:
            res = c.new_document(name=name, public=True)
            self.uri = Uri('https://cad.onshape.com/documents/' + res.json()["id"])

        self.update()

    def delete(self):
        """Delete the Onshape document"""
        c = Context().client
        c.del_document(self.uri.did)

    def update(self):
        c = Context().client
        self.json = c.get_document(self.uri.did).json()

    @property
    def name(self):
        return self.json["name"]


