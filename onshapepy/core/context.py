"""The context of OnShapePy holds all shared state, such as authentication info. It is a singleton."""
from onshapepy.core.client import Client


class Context:

    instance = None

    def __init__(self, **kwargs):
        if not Context.instance:
            Context.instance = Context.__Context(**kwargs)
        else:
            if kwargs:
                raise UserWarning("Can't set context options through the initializer once the context is created. "
                                  "Instead, update the particular field of context you would like to or move the option"
                                  " to the initial instantiation of context.")

    def __getattr__(self, name):
        return getattr(self.instance, name)

    class __Context:
        def __init__(self, **kwargs):

            #initialize client
            if 'client' in kwargs:
                self.client = kwargs["client"]
            else:
                self.client = Client()




