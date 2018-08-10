"""An OnShape assembly

"""

from onshapepy.uri import Uri
import json


class Assembly:


    def __init__(self, url):
        """ Connect to an assembly that points to the assembly specified with did, wid and eid.

        Parameters
        ----------
        url:
            The url of the onshape item
        """
        self.uri = Uri(url)


    def insert(self, part, client):
        """ Insert a part into this assembly.

        Parameters
        ----------
        part
            A Part instance that will be inserted.
        client
            A Client instance that does the inserting.

        Returns
        -------
        Response from the server

        """
        pass