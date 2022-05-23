#implement an adjacency list in python with descriptive comments

# An adjacency list is a data structure that represents a graph. 
# Each node in the graph is represented by a list, and each list 
# contains the nodes that are adjacent to that node. 

# In this implementation, each node is represented by a tuple, 
# which contains the node's value and a list of its adjacent nodes. 

graph = {
    'A': ('B', 'C', 'D'),
    'B': ('A', 'E', 'F'),
    'C': ('A', 'G', 'H'),
    'D': ('A', 'I', 'J'),
    'E': ('B', 'K', 'L'),
    'F': ('B', 'M', 'N'),
    'G': ('C', 'O', 'P'),
    'H': ('C', 'Q', 'R'),
    'I': ('D', 'S', 'T'),
    'J': ('D', 'U', 'V'),
    'K': ('E',),
    'L': ('E',),
    'M': ('F',),
    'N': ('F',),
    'O': ('G',),
    'P': ('G',),
    'Q': ('H',),
    'R': ('H',),
    'S': ('I',),
    'T': ('I',),
    'U': ('J',),
    'V': ('J',)
}