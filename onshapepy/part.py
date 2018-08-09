'''
part
====

OnShape part that maps to a part studio
'''

from onshapepy.core.client import Client
import json
from onshapepy.uri import Uri

class Part():
    """A part is used to configure a part studio. This reflects a part at a specific OnShape version. Anything that
    updates the part will then create a new instance of part to be used.


    """

    def __init__(self, url, params={}):
        """
        Args:
            - url (str): the url of the Part Studio
            - params (dict, opt): dict of parameter objects. These are objects that return valid parameter settings
                when encoded as a string.
        """
        self.uri = Uri(url)
        self.params = params


    def update_server(self):
        """Send the current configuration to the server
        :return:
        TODO: when OnShape releases the ability to update a part instance in an assembly with new configuration, write this.
        """
        pass

    def update_configuration(self, client):
        """Get the current configuration from OnShape and put it into the part's configuration.
        :return:
        """
        res = client.get_configuration(self.uri.as_dict())
        res_configuration = json.loads(res.content.decode("utf-8"))["currentConfiguration"]
        new_configuration = {}

        for p in res_configuration:
            new_param = {}
            new_param["value"] = p["message"]["value"]
            new_param["units"] = p["message"]["units"] if "units" in p["message"] else None
            new_configuration[p["message"]["parameterId"]] = new_param

        self.params.update(new_configuration)
