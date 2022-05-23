implement a graph data structure with an adjacency list in python with descriptive comments

class Graph:
    def __init__(self):
        self.graph = {}
    
    # Add a node to the graph, with an empty list of edges
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []
    
    # Add an edge to the graph by adding the node to the list of edges of the other node
    def add_edge(self, node1, node2):
        if node1 in self.graph:
            self.graph[node1].append(node2)
        else:
            self.graph[node1] = [node2]
    
    # Remove an edge from the graph by removing the node from the list of edges of the other node
    def remove_edge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph[node1]:
            self.graph[node1].remove(node2)
    
    # Remove a node from the graph by removing all of its edges and then removing the node
    def remove_node(self, node):
        if node in self.graph:
            for edge in self.graph[node]:
                self.remove_edge(node, edge)
            del self.graph[node]
    
    # Check if two nodes are connected
    def is_connected(self, node1, node2):
        if node1 in self.graph and node2 in self.graph[node1]:
            return True
        return False