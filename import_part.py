from onshape.client import Client

# assembly to import into
assembly_id = "6f1f9c485ff1e639f4db63c0"
did = "8ec353ba00f37f447b5a61f5"
wid = "04c36c786829759832bd3d1a"

payload = r"""{
  "documentId": "8ec353ba00f37f447b5a61f5",
  "elementId": "2918f0f5adfa39d3047f19d0",
  "versionId": "",
  "microversionId": "",
  "isAssembly": false,
  "isWholePartStudio": true,
  "partId": "",
  "featureId": "",
  "configuration": "height=20+meter;poo=true"
}"""

# stacks to choose from
stacks = {
    'cad': 'https://cad.onshape.com'
}

# create instance of the onshape client; change key to test on another stack
c = Client(stack=stacks['cad'], logging=True)

c._api.request('post', "/api/assemblies/d/8ec353ba00f37f447b5a61f5/w/04c36c786829759832bd3d1a/e/6f1f9c485ff1e639f4db63c0/instances", body=payload)
