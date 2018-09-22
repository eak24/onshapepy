"""Represents an Onshape document"""
from onshapepy.uri import Uri
from onshapepy.core.utils import ElementType
from onshapepy.core.client import c


class Document:
    def __init__(self, url, copy=False, name=None, version=None):
        """Link to/copy a document. If copy is set to true, then make a copy of that workspace. If copy is set to false,
        load the document specified. If the url is an empty string and name is set, make a new, blank document.

        Args:
            - url (str): The URL of the document to be copied.
            - copy (bool): Whether or not to copy the document.
            - name (str): The name of the copied or new document.
            - version (str): The Onshape version name of the version to be copied or referenced.

            """

        self.json = None
        self.e_list = None

        # Make a copy:
        if url and copy and name:
            uri = Uri(url)
            # If a version is specified, set/override the uri/url version TODO:
            # if version:
            #     for v in c.get_versions(uri.as_dict()).json():
            #         if v['name'] == version:
            #             uri.wvm = v['id']
            #             uri.wvm_type = 'v'
            #             break
            # res = c.create_workspace(uri.did, name, version_id=uri.wvm)
            # uri.wvm = res.json()['id']
            # uri.wvm_type = 'w'
            res = c.copy_workspace(uri.as_dict(), name)
            payload = res.json()
            url = 'https://cad.onshape.com/documents/' + payload["newDocumentId"] + "/w/" + payload["newWorkspaceId"]
            self.uri = Uri(url)
        # Reference an existing doc:
        elif url and not copy:
            self.uri = Uri(url)
        # Make a new, blank doc:
        elif name:
            res = c.create_document(name=name, public=True)
            self.uri = Uri('https://cad.onshape.com/documents/' + res.json()["id"])

        self.update()

    def delete(self):
        """Delete the Onshape document"""
        c.del_document(self.uri.did)

    def update(self):
        """All client calls to update this instance with Onshape."""
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

        for e in self.e_list:
            # if a type is specified and this isn't it, move to the next loop.
            if type.value and not e['elementType'] == type:
                continue
            if e["name"] == name:
                uri = self.uri
                uri.eid = e["id"]
                return uri


