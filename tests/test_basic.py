from apikey.client import Client


def test_new_doc():
    # stacks to choose from
    stacks = {
        'cad': 'https://cad.onshape.com'
    }

    # create instance of the onshape client; change key to test on another stack
    c = Client(stack=stacks['cad'], logging=True)

    # make a new document and grab the document ID and workspace ID
    new_doc = c.new_document(public=True).json()
    assert new_doc['name'] == 'Test Document'