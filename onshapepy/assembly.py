"""An OnShape assembly

"""

from onshapepy.uri import Uri
import json
from onshapepy.core.client import c


class Assembly:


    def __init__(self, url):
        """ Connect to an assembly that points to the assembly specified with the url.

        Args:
            - url (str): The url of the onshape item
        """
        # Accept either a url OR uri
        if isinstance(url, Uri):
            self.uri = url
        else:
            self.uri = Uri(url)


    def insert(self, part):
        """ Insert a part into this assembly.

        Args:
            - part (onshapepy.part.Part) A Part instance that will be inserted.

        Returns:
            - requests.Response: Onshape response data

        """
        params = {k: str(v) for k,v in part.params.items()}
        res=c.create_assembly_instance(self.uri.as_dict(), part.uri.as_dict(), params)
        return res