class Graph():
  def __init__(self):
    self.relations = {}
  def __str__(self):
    return str(self.relations)

  def add_node(self, node):
    self.relations.update({node:[]})

  def create_link(self, nodeA, nodeB):
    self.link_node(nodeA, nodeB)
    self.link_node(nodeB, nodeA)

  def link_node(self, origin, destiny):
    self.relations[origin].append(destiny)

  def print_graph(self):
    for (key, value) in self.relations:
      print (key + ' : ' + "".join(value))
    
