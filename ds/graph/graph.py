from collections import deque

class Graph:
    def __init__(self, size):
        self.size = size
        self.edges = [set() for _ in range(size)]

    def connect(self, a, b):
        self.edges[a].add(b)

    def connected(self, a, b):
        return b in self.edges[a]

class DFS:
    @staticmethod
    def explore(graph, start, *, pre_visit=None, post_visit=None, cycle=None):
        def null():
            pass
        pre_visit = pre_visit or null
        cycle = cycle or null
        post_visit = post_visit or null

        path = deque([])
        visited = [False for _ in range(graph.size)]
        queue = deque([start])
        while len(queue):
            v = queue.popleft()
            if not visited[v]:
                path.append(v)
                pre_visit(v)
                # post visit marker
                queue.insert(0, v) 
                for node in reversed(sorted(graph.edges[v])):
                    queue.insert(0, node)
                visited[v] = True
            elif path[-1] == v:
                path.pop()
                post_visit(v)
            else:
                cycle(list(path))
