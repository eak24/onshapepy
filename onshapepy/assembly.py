"""An OnShape assembly

"""

from onshapepy.uri import Uri
import json


class Assembly:


    def __init__(self, url):
        """ Connect to an assembly that points to the assembly specified with did, wid and eid.

        Args:
            - url (str): The url of the onshape item
        """
        self.uri = Uri(url)


    def insert(self, part, client):
        """ Insert a part into this assembly.

        Args:
            - part (onshapepy.part.Part) A Part instance that will be inserted.
            - client (onshapepy.core.client.Client) A Client instance that does the inserting.

        Returns:
            - requests.Response: Onshape response data

        """
        pass