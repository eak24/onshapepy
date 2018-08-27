from onshapepy.core.utils import ElementType


def test_find_name(document):
    uri = document.find_element("cube")
    assert uri.did
    uri = document.find_element("cube", ElementType.PARTSTUDIO)
    assert uri is None
    uri = document.find_element("cube", ElementType.ASSEMBLY)
    assert uri is None
