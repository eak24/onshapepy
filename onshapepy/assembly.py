"""An OnShape assembly

"""

class Assembly:


    def __init__(self, did, wid, eid):
        self.uri = {"did": did, "wid": wid, "eid": eid}


    def insert(self, part, client):
        client.insert_configured_part(self.uri, part.uri, {n: str(v["value"]) + str(v["units"]) for n,v in part.params.items()})