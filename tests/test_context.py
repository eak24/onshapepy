from onshapepy.core.context import Context
import pytest

def test_context_creation():
    context = Context()
    logging_status = context.client.conf['logging']
    context2 = Context()
    # Assert context is created only once
    assert id(context.instance) == id(context2.instance)
    context.client.update(conf={"logging": not logging_status})
    # Ensure updating the client works
    assert context.client.conf['logging'] is not logging_status
    # Make sure trying to change Context through the constructor breaks
    with pytest.raises(UserWarning):
        Context(client="this isn't good!")

