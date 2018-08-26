'''
OnShape part that maps to a part studio
'''

from onshapepy.core.client import Client
from onshapepy.core.context import Context
from onshapepy.core.utils import parse_quantity
import json
from onshapepy.uri import Uri
import pint
u = pint.UnitRegistry()
q = u.Quantity


class Part():
    """A part is used to configure a part studio. This reflects a part at a specific OnShape version. Anything that
    updates the part will then create a new instance of part to be used.


    """

    def __init__(self, url, params=None):
        """
        Args:
            - url (str): the url of the Part Studio
            - params (dict, opt): dict of parameter objects. These are objects that return valid parameter settings
                when encoded as a string.
        """
        self.uri = Uri(url)
        self._configuration = Configuration(self)
        #post defined params if necessary
        if params:
            self._configuration.update(params)
        else:
            self._configuration.get_params()
        self._measurements = Measurements(self)
        self._measurements.update()

    @property
    def measurements(self):
        return self._measurements.measurements


    @property
    def params(self):
        return self._configuration.params

    @params.setter
    def params(self, dict):
        """Set configuration variables for an OnShape part."""
        self._configuration.update(dict)
        self._measurements.update()


class Configuration:
    """The collection of configuration values. This class simplifies interacting with the configuration REST API and
    some caching to reduce wait times."""

    def __init__(self, parent):
        """Holds the configuration state specified by the uri. The most recent server response is held in raw_res. This
        is used to generate a list of easier to understand and serialize dictionary of config values."""
        self.res = None
        self.parent = parent

    @property
    def payload(self):
        return json.loads(self.res.content.decode("utf-8"))

    def update(self, params=None):
        """Push params to OnShape and synchronize the local copy
        """
        c = Context().client
        uri = self.parent.uri
        if not params or not self.res:
            self.get_params()
            return
        d = self.payload
        for k, v in params.items():
            m = d["currentConfiguration"][self.parameter_map[k]]["message"]
            if isinstance(v, bool) or isinstance(v, str):
                m["value"] = v
            else:
                try:
                    m["expression"] = str(v)
                except KeyError:
                    m["value"] = str(v)

        res = c.update_configuration(uri.did, uri.wvm, uri.eid, json.dumps(d))

        # If it was a good request, update config to be consistent with online.
        if res.status_code == 200:
            self.res = res

    def get_params(self):
        """Manually pull params defined in config from OnShape and return a python representation of the params.
        Quantities are converted to pint quantities, Bools are converted to python bools and Enums are converted
        to strings. Note that Enum names are autogenerated by OnShape and do not match the name on the OnShape UI."""
        client = Context().client
        self.res = client.get_configuration(self.parent.uri.as_dict())

    @property
    def params(self):
        """Get the params of response data from the API.

        Returns:
            - d (dict): Dictionary mapping of all configuration values
        """
        payload = self.payload
        d = {}
        for i, p in enumerate(payload["currentConfiguration"]):
            type_name = p["typeName"]
            cp = payload["configurationParameters"][i]["message"]
            name = cp["parameterName"]
            if type_name == "BTMParameterQuantity":
                try:
                    v = q(p["message"]["expression"])
                except:
                    v = q(p["message"]["value"], p["message"]["units"])
            elif type_name == "BTMParameterBoolean":
                v = p["message"]["value"]
            elif type_name == "BTMParameterEnum":
                enum = p["message"]["value"]
                enum_map = {d['message']['option']: i for i, d in enumerate(cp['options'])}
                v = cp['options'][enum_map[enum]]['message']['optionName']
            d[name] = v
        return d

    @property
    def parameter_map(self):
        payload = self.payload
        parameter_map = {}
        for i, p in enumerate(payload["currentConfiguration"]):
            name = payload["configurationParameters"][i]["message"]["parameterName"]
            parameter_map[name] = i
        return parameter_map


class Measurements:
    """Result of "output dimensions" as specified with the "Measure" features within the part Studio"""

    def __init__(self, parent):
        self.res = None
        self.parent = parent

    def update(self):
        """ Update all local variable names to match OnShape. """
        c = Context().client
        uri = self.parent.uri
        script = r"""
        function(context, queries) {
            return getVariable(context, "measurements");
        }
        """

        self.res = c.evaluate_featurescript(uri.as_dict(), script)

    @property
    def payload(self):
        return json.loads(self.res.content.decode("utf-8"))

    @property
    def measurements(self):
        m_dictionary = {}
        for m in self.payload["result"]["message"]["value"]:
            name = m["message"]["key"]['message']['value']
            q = m["message"]['value']['message']
            m_dictionary[name] = u(parse_quantity(q))
        return m_dictionary