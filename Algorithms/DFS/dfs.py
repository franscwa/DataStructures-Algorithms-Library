//implement depth first search in python with descriptive comments



def depthFirstSearch(graph, start, end, path=[]):
        # add the starting node to the path
        path = path + [start]
        # if the starting node is the same as the ending node, return the path
        if start == end:
            return path
        # if the starting node is not in the graph, return None
        if not graph.has_key(start):
            return None
        # loop through each node in the graph
        for node in graph[start]:
            # if the node is not in the path, recursively call the depthFirstSearch function
            if node not in path:
                newpath = depthFirstSearch(graph, node, end, path)
                # if a new path is found, return it
                if newpath: return newpath
        # if no new path is found, return None
        return None