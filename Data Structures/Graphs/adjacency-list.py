class AdjacencyList(object):
    def __init__(self, n):
        self.n = n
        self.alist = [[] for i in range(n)]

    def add_edge(self, u, v):
        self.alist[u].append(v)
        self.alist[v].append(u)

    def get_adj_list(self):
        return self.alist