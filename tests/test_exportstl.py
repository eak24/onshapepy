'''
exportstl
===

Demos 307 redirects with the Onshape API
'''

from onshape.client import Client

# stacks to choose from
stacks = {
    'cad': 'https://cad.onshape.com'
}

# create instance of the onshape client; change key to test on another stack
c = Client(stack=stacks['cad'], logging=True)

# get features for doc
did = "8ec353ba00f37f447b5a61f5"
wid = "04c36c786829759832bd3d1a"
eid = "2918f0f5adfa39d3047f19d0"

# get the STL export
stl = c.part_studio_stl(did, wid, eid)

# print to the console
print(stl.text)
