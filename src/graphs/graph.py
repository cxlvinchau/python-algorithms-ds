from typing import Tuple


class Graph:

    def __init__(self):
        self.succs = dict()
        self.vertices = set()
        self.edges = set()

    def add_vertex(self, v: int):
        self.vertices.add(v)

    def add_edge(self, e: Tuple[int, int]):
        for v in e:
            if v not in self.vertices:
                self.vertices.add(v)
        self.edges.add(e)
        self.succs.setdefault(e[0], set()).add(e[1])

    def get_succs(self, v):
        if v in self.succs:
            return self.succs[v]
        return set()

    def to_dot(self):
        r = "digraph {\n"
        for s, t in self.edges:
            r += f"{s} -> {t}\n"
        return r +"}"


class UndirectedGraph(Graph):

    def add_edge(self, e: Tuple[int, int]):
        s, t = e
        if s != t:
            self.edges.add(set(e))
            self.succs.setdefault(s, set()).add(t)
            self.succs.setdefault(t, set()).add(s)


class WeightedGraph(Graph):

    def __init__(self):
        super().__init__()
        self.weights = dict()

    def add_edge(self, e: Tuple[int, int], weight=None):
        super().add_edge(e)
        if weight is not None:
            self.weights[e] = weight