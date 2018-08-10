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

    def __init__(self, url, params=None, client=Client()):
        """
        Args:
            - url (str): the url of the Part Studio
            - params (dict, opt): dict of parameter objects. These are objects that return valid parameter settings
                when encoded as a string.
        """
        self.uri = Uri(url)
        self.config = Config(url)
        self.config.set(params)
        self.client = client
        self.params = self.config.get_params()


class Config:
    """The collection of configuration values. This class simplifies interacting with the configuration REST API"""

    def __init__(self, url, client=Client()):
        """Holds the configuration state specified by the uri. The most recent server response is held in raw_res. This
        is used to generate a list of easier to understand and serialize dictionary of config values."""
        self.uri = Uri(url)
        self.client = client
        self.raw = None

    def set(self, params):
        """Specify the name of a config parameter and its value and set it in the payload."""
        pass

    def post_params(self):
        """Manually push params defined in config to OnShape"""
        pass

    def get_params(self):
        """Manually pull params defined in config from OnShape and update local copy"""
        res = self.client.get_configuration(self.uri.as_dict())
        self.raw = json.loads(res.content.decode("utf-8"))["currentConfiguration"]
        d = {}
        for p in self.raw:
            if "units" in p["message"]:
                value = string_to_quantity(p["message"]["value"], p["message"]["units"])
                name = p["message"]["parameterId"]
                d[name] = value
        return d

def string_to_quantity(value, units):
    """Convert a quantity defined by a value and a units string into a quantity"""
    import pint
    u = pint.UnitRegistry()
    q = u.Quantity
    return q(value, units)


class OutputDims:
    pass
