class Graph(object):
  def __init__(self):
    self.relations = {}
  def __str__(self):
    return str(self.relations)

def add_node(graph, node):
  graph.relations.update({node:[]})

def create_link(graph, nodeA, nodeB):
  link_node(graph, nodeA, nodeB)
  link_node(graph, nodeB, nodeA)

def link_node(graph, origin, destiny):
  graph.relations[origin].append(destiny)
