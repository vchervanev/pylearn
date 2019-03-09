class Graph:
    def __init__(self, size):
        self.size = size
        self.edges = [set() for _ in range(size)]

    def connect(self, a, b):
        self.edges[a].add(b)

    def connected(self, a, b):
        return b in self.edges[a]
