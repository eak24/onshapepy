'''
part
====

OnShape part that maps to an element of a part studio
'''

class Part():
    """a part is used to configure a part studio.
    """

    def configure(assembly):
        """
        Args:
            - assembly (dict): a dict with the did, wid, and eid of the assembly into which the part will be inserted.
        """
