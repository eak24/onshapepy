'''
client
======

Low-level convenience functions for working with the Onshape API. No custom objects are handled here - only dictionaries.
Function names should be equivalent to the OnShape REST API names
'''

from onshapepy.core.onshape import Onshape

import mimetypes
import random
import string
import os
import json
from pathlib import Path
from ruamel.yaml import YAML

yaml = YAML()

class Client:
    '''
    Defines methods for testing the Onshape API. Comes with several methods:

    - Create a document
    - Delete a document
    - Get a list of documents

    Attributes:
        - stack (str, default='https://cad.onshape.com'): Base URL
        - logging (bool, default=True): Turn logging on or off
    '''

    def __init__(self, conf=None, conf_file=".onshapepy"):
        '''
        Instantiates a new Onshape client.

        Attributes:
            - conf: the configuration that generated this client. This is read-only and for testing purposes.

        Args:
            - configuration (dict, optional): a dictionary of configuration options. Default behavior is to load this from a YAML file that
                is located in user's home directory and name '.onshapepy'. For options that can be set, look
                at the documentation section on 'configuration'.
        '''

        default_conf = {
            'stack': 'https://cad.onshape.com',
            'logging': False,
            'creds': None
        }

        try:
            user_conf = yaml.load(Path.home().joinpath(conf_file))
            default_conf.update(user_conf)
        except:
            pass

        if conf:
            default_conf.update(conf)

        self.conf = default_conf

        self._stack = default_conf['stack']
        self._api = Onshape(default_conf['stack'], default_conf['creds'], default_conf['logging'])

    def update(self, conf):
        """Update the client with a new configuration

        Args:
            - conf (dict): a client configuration dictionary.
        """
        Client(self.conf.update(conf))



    def create_document(self, name='Test Document', owner_type=0, public=True):
        '''
        Create a new document.

        Args:
            - name (str, default='Test Document'): The doc name
            - owner_type (int, default=0): 0 for user, 1 for company, 2 for team
            - public (bool, default=False): Whether or not to make doc public

        Returns:
            - requests.Response: Onshape response data
        '''

        payload = {
            'name': name,
            'ownerType': owner_type,
            'isPublic': public
        }

        return self._api.request('post', '/api/documents', body=payload)

    def rename_document(self, did, name):
        '''
        Renames the specified document.

        Args:
            - did (str): Document ID
            - name (str): New document name

        Returns:
            - requests.Response: Onshape response data
        '''

        payload = {
            'name': name
        }

        return self._api.request('post', '/api/documents/' + did, body=payload)

    def del_document(self, did):
        '''
        Delete the specified document.

        Args:
            - did (str): Document ID

        Returns:
            - requests.Response: Onshape response data
        '''

        return self._api.request('delete', '/api/documents/' + did)

    def get_document(self, did):
        '''
        Get details for a specified document.

        Args:
            - did (str): Document ID

        Returns:
            - requests.Response: Onshape response data
        '''

        return self._api.request('get', '/api/documents/' + did)

    def list_documents(self):
        '''
        Get list of documents for current user.

        Returns:
            - requests.Response: Onshape response data
        '''

        return self._api.request('get', '/api/documents')

    def copy_workspace(self, uri, new_name):
        '''
        Copy the current workspace.

        Args:
            - uri (dict): the uri of the workspace being copied. Needs to have a did and wid key.
            - new_name (str): the new name of the copied workspace.

        Returns:
            - requests.Response: Onshape response data
        '''

        payload = {
            'isPublic': True,
            'newName': new_name
        }

        return self._api.request('post', '/api/documents/' + uri['did'] + '/workspaces/' + uri['wvm'] + '/copy', body=payload)

    def create_workspace(self, did, name, version_id=None):
        '''
        Create a workspace in the specified document.

        Args:
            - did (str): the document id of where to create the new workspace
            - name (str): the new name of the copied workspace.
            - version_id (str): the ID of the version to be copied into a new workspace

        Returns:
            - requests.Response: Onshape response data
        '''

        payload = {
            'isPublic': True,
            'name': name,
        }

        if version_id:
            payload['versionId'] = version_id

        return self._api.request('post', '/api/documents/d/' + did + '/workspaces', body=payload)

    def create_assembly(self, did, wid, name='My Assembly'):
        '''
        Creates a new assembly element in the specified document / workspace.

        Args:
            - did (str): Document ID
            - wid (str): Workspace ID
            - name (str, default='My Assembly')

        Returns:
            - requests.Response: Onshape response data
        '''

        payload = {
            'name': name
        }

        return self._api.request('post', '/api/assemblies/d/' + did + '/w/' + wid, body=payload)

    def get_features(self, did, wid, eid):
        '''
        Gets the feature list for specified document / workspace / part studio.

        Args:
            - did (str): Document ID
            - wid (str): Workspace ID
            - eid (str): Element ID

        Returns:
            - requests.Response: Onshape response data
        '''

        return self._api.request('get', '/api/partstudios/d/' + did + '/w/' + wid + '/e/' + eid + '/features')

    def get_partstudio_tessellatededges(self, did, wid, eid):
        '''
        Gets the tessellation of the edges of all parts in a part studio.

        Args:
            - did (str): Document ID
            - wid (str): Workspace ID
            - eid (str): Element ID

        Returns:
            - requests.Response: Onshape response data
        '''

        return self._api.request('get', '/api/partstudios/d/' + did + '/w/' + wid + '/e/' + eid + '/tessellatededges')

    def upload_blob(self, did, wid, filepath='./blob.json'):
        '''
        Uploads a file to a new blob element in the specified doc.

        Args:
            - did (str): Document ID
            - wid (str): Workspace ID
            - filepath (str, default='./blob.json'): Blob element location

        Returns:
            - requests.Response: Onshape response data
        '''

        chars = string.ascii_letters + string.digits
        boundary_key = ''.join(random.choice(chars) for i in range(8))

        mimetype = mimetypes.guess_type(filepath)[0]
        encoded_filename = os.path.basename(filepath)
        file_content_length = str(os.path.getsize(filepath))
        blob = open(filepath)

        req_headers = {
            'Content-Type': 'multipart/form-data; boundary="%s"' % boundary_key
        }

        # build request body
        payload = '--' + boundary_key + '\r\nContent-Disposition: form-data; name="encodedFilename"\r\n\r\n' + encoded_filename + '\r\n'
        payload += '--' + boundary_key + '\r\nContent-Disposition: form-data; name="fileContentLength"\r\n\r\n' + file_content_length + '\r\n'
        payload += '--' + boundary_key + '\r\nContent-Disposition: form-data; name="file"; filename="' + encoded_filename + '"\r\n'
        payload += 'Content-Type: ' + mimetype + '\r\n\r\n'
        payload += blob.read()
        payload += '\r\n--' + boundary_key + '--'

        return self._api.request('post', '/api/blobelements/d/' + did + '/w/' + wid, headers=req_headers, body=payload)

    def part_studio_stl(self, did, wid, eid):
        '''
        Exports STL export from a part studio

        Args:
            - did (str): Document ID
            - wid (str): Workspace ID
            - eid (str): Element ID

        Returns:
            - requests.Response: Onshape response data
        '''

        req_headers = {
            'Accept': 'application/vnd.onshape.v1+octet-stream'
        }
        return self._api.request('get', '/api/partstudios/d/' + did + '/w/' + wid + '/e/' + eid + '/stl', headers=req_headers)

# Below are functions added for AguaClara

    def create_assembly_instance(self, assembly_uri, part_uri, configuration):
        '''
        Insert a configurable part into an assembly.

        Args:
            - assembly (dict): eid, wid, and did of the assembly into which will be inserted
            - part (dict): eid and did of the configurable part
            - configuration (dict): the configuration

        Returns:
            - requests.Response: Onshape response data
        '''

        payload = {
          "documentId": part_uri["did"],
          "elementId": part_uri["eid"],
          # could be added if needed:
          # "partId": "String",
          # "featureId": "String",
          # "microversionId": "String",
          "versionId": part_uri["wvm"],
          # "microversionId": "String",
          "isAssembly": False,
          "isWholePartStudio": True,
          "configuration": self.encode_configuration(part_uri["did"], part_uri["eid"], configuration)
        }
        return self._api.request('post', '/api/assemblies/d/' + assembly_uri["did"] + '/' + assembly_uri["wvm_type"] +
                                 '/' + assembly_uri["wvm"] + '/e/' + assembly_uri["eid"] + '/instances', body=payload)

    def encode_configuration(self, did, eid, parameters):
        '''
        Encode parameters as a URL-ready string

        Args:
            - did (str): Document ID
            - eid (str): Element ID
            - parameters (dict): key-value pairs of the parameters to be encoded
        Returns:
            - configuration (str): the url-ready configuration string.
        '''
        # change to the type of list the API is expecting
        parameters = [{"parameterId": k, "parameterValue": v} for (k,v) in parameters.items()]

        payload = {
            'parameters':parameters

        }
        req_headers = {
            'Accept': 'application/vnd.onshape.v1+json',
            'Content-Type': 'application/json'
        }

        res = self._api.request('post', '/api/elements/d/' + did  + '/e/' + eid + '/configurationencodings', body=payload, headers=req_headers)

        return json.loads(res.content.decode("utf-8"))["encodedId"]


    def get_configuration(self, uri):
        '''
        get the configuration of a PartStudio

        Args:
            - uri (dict): points to a particular element

        Returns:
            - requests.Response: Onshape response data
        '''

        req_headers = {
            'Accept': 'application/vnd.onshape.v1+json',
            'Content-Type': 'application/json'
        }
        return self._api.request('get', '/api/partstudios/d/' + uri["did"] + '/' + uri["wvm_type"] + '/' + uri["wvm"] + '/e/' + uri["eid"] + '/configuration', headers=req_headers)


    ############### Part Studio ###########################

    def update_configuration(self, did, wid, eid, payload):
        '''
        Update the configuration specified in the payload

        Args:
            - did (str): Document ID
            - eid (str): Element ID
            - payload (json): the request body
        Returns:
            - configuration (str): the url-ready configuration string.
        '''

        req_headers = {
            'Accept': 'application/vnd.onshape.v1+json',
            'Content-Type': 'application/json'
        }

        res = self._api.request('post', '/api/partstudios/d/' + did + '/w/' + wid + '/e/' + eid + '/configuration', body=payload, headers=req_headers)

        return res

    def evaluate_featurescript(self, uri, script, queries=[]):
        """

        Args:
            uri (dict): Location including did, eid, wvm
            queries ([dict]):
            script (str): A FeatureScript function to run.

        Returns:
            - requests.Response: Onshape response data
        """
        req_headers = {
            'Accept': 'application/vnd.onshape.v1+json',
            'Content-Type': 'application/json'
        }

        payload = {
            'queries': queries,
            'script': script

        }

        return self._api.request('post',
                                 '/api/partstudios/d/' + uri["did"] + '/' + uri["wvm_type"] + '/' + uri["wvm"] + '/e/' +
                                 uri["eid"] + '/featurescript', body=payload, headers=req_headers)

    def element_list(self, uri):
        return self._api.request('get',
                                 '/api/documents/d/' + uri["did"] + '/' + uri["wvm_type"] + '/' + uri["wvm"] +
                                 '/elements')

    def get_versions(self, uri):
        return self._api.request('get', '/api/documents/d/' + uri["did"] + '/versions')


# Start the default client. To change the client, just change this value.
c=Client()
