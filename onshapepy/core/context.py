"""The context of OnShapePy holds all shared state, such as authentication info. It is a singleton."""
from onshapepy.core.client import Client


class Context:

    instance = None

    def __init__(self, **kwargs):
        if not Context.instance:
            Context.instance = Context.__Context(kwargs)
        else:
            Context.instance.update(kwargs)

    def __getattr__(self, name):
        return getattr(self.instance, name)

    class __Context:
        def __init__(self, kwargs):
            self.client = None
            self.update(kwargs)

        def update(self, kwargs):
            if "client" in kwargs:
                self.client = kwargs["client"]
            else:
                self.client = Client()

