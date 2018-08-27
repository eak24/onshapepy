"""Represents an Onshape document"""
from onshapepy.core.context import Context
from onshapepy.uri import Uri
from onshapepy.core.utils import ElementType


class Document:
    def __init__(self, url, copy=False, name=None):
        """Link to/copy a document. If copy is set to true, then make a copy of that workspace. If copy is set to false,
        load the document specified. If the url is an empty string and name is set, make a new, blank document"""
        c = Context().client

        self.json = None
        self.e_list = None

        # Make a copy:
        if url and copy and name:
            res = c.copy_workspace(Uri(url).as_dict(), name)
            payload = res.json()
            url = 'https://cad.onshape.com/documents/' + payload["newDocumentId"] + "/w/" + payload["newWorkspaceId"]
            self.uri = Uri(url)
        # Reference an existing doc:
        elif url and not copy:
            self.uri = Uri(url)
        # Make a new, blank doc:
        elif name:
            res = c.new_document(name=name, public=True)
            self.uri = Uri('https://cad.onshape.com/documents/' + res.json()["id"])

        self.update()

    def delete(self):
        """Delete the Onshape document"""
        c = Context().client
        c.del_document(self.uri.did)

    def update(self):
        """All client calls to update this instance with Onshape."""
        c = Context().client
        self.json = c.get_document(self.uri.did).json()
        self.e_list = c.element_list(self.uri.as_dict()).json()

    @property
    def name(self):
        return self.json["name"]

    def find_element(self, name, type=ElementType.ANY):
        """Find an elemnent in the document with the given name - could be a PartStudio, Assembly or blob.

        Args:
            name: str
                the name of the element.

        Returns:
            - onshapepy.uri of the element
        """
        c = Context().client

        for e in self.e_list:
            # if a type is specified and this isn't it, move to the next loop.
            if type.value and not e['elementType'] == type:
                continue
            if e["name"] == name:
                uri = self.uri
                uri.eid = e["id"]
                return uri


