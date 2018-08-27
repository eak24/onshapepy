from onshapepy.uri import Uri

def test_uri():
    new_uri = Uri(
        "https://cad.onshape.com/documents/de0b979bd2526029daafe060/w/8043876c6f38336511d43098/e/df8a8fc984dc38ed3da6f964")
    assert new_uri.did == "de0b979bd2526029daafe060"
    assert new_uri.wvm == "8043876c6f38336511d43098"
    assert new_uri.eid == "df8a8fc984dc38ed3da6f964"
    assert new_uri.wvm_type == "w"
    assert new_uri.as_dict() == {'did': 'de0b979bd2526029daafe060', 'wvm': '8043876c6f38336511d43098', 'eid': 'df8a8fc984dc38ed3da6f964', 'wvm_type': 'w'}