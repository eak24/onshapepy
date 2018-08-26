import urllib.parse as parse


class Uri():
    """Helper functions for specifying an OnShape element URI

    Attributes
    ----------
    url: str
        The original URL used to define this uri
    did: str
        The document ID
    eid: str
        The element ID
    wvm: str
        workspace, version or microversion id
    wvm_type: str
        Workspace (w), Version (v) or Microversion (m)
        """

    def __init__(self, url):
        """ Set the did, eid and wid.

        Parameters
        ----------
        url: str
            the URL of the OnShape element

        """
        self.url = url
        path = parse.urlparse(url).path.split("/")
        # Expected parameters in the path
        d_expected = {3: "wvm_type", 2: "did", 6: "eid", 4: "wvm"}
        for index, name in d_expected.items():
            try:
                setattr(self, name, path[index])
            except IndexError:
                pass

    def as_dict(self):
        """ Return the URI object as a dictionary"""
        d = {k:v for (k,v) in self.__dict__.items()}
        return d