import urllib.parse as parse


class Uri():
    """Helper functions for specifying an OnShape element URI"""

    def __init__(self, url):
        """ Set the did, eid and wid.

        Parameters
        ----------
        url: str
            the URL of the OnShape element

        """
        path = parse.urlparse(url).path.split("/")

        self.url = url
        self.wvm = path[3]
        self.did = path[2]
        self.eid = path[6]

        self.__setattr__(self.wvm+"id", path[4])

    def as_dict(self):
        """ Return the URI object as a dictionary"""
        d = {k:v for (k,v) in self.__dict__.items()}
        return d