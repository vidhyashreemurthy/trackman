class node(object):
    def __init__(self, schema, table):
        self.schema = schema
        self.table = table
        self.links = []
    
    def __eq__(self, other):
        return self.schema == other.schema and self.table == other.table
    
    def add_link(self, nodes):
        for node in nodes:
            if node not in self.links:
                self.links.append(node)