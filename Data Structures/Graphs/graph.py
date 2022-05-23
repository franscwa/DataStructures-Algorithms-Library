implement a graph data structure in python



class Graph:

def __init__(self):

self.nodes = set()

self.edges = defaultdict(list)

self.distances = {}

def add_node(self, value):

self.nodes.add(value)

def add_edge(self, from_node, to_node, distance):

self.edges[from_node].append(to_node)

self.edges[to_node].append(from_node)

self.distances[(from_node, to_node)] = distance

def get_nodes(self):

return self.nodes

def get_edges(self):

return self.edges

def get_distance(self, from_node, to_node):

return self.distances[(from_node, to_node)]