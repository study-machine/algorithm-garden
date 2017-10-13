from Edge import *


class Graph(object):
    def __init__(self, vertexs, is_directed):
        self._vertexs = vertexs
        self._is_directed = is_directed
        self._edges = 0

    @property
    def vertexs(self):
        return self._vertexs

    @property
    def edges(self):
        return self._edges

    def add_edge(self, v1, v2):
        pass

    def has_edge(self, v1, v2):
        pass

    def print_graph(self):
        if hasattr(self, 'g'):
            for i in xrange(self.vertexs):
                print i, self.g[i]


class SparseGraph(Graph):
    def __init__(self, *args):
        super(SparseGraph, self).__init__(*args)
        self.g = [[] for _ in xrange(self._vertexs)]

    def add_edge(self, v1, v2):
        self.g[v1].append(v2)
        if v1 != v2 and not self._is_directed:
            self.g[v2].append(v1)

    def has_edge(self, v1, v2):
        return v1 in self.g[v1]

    def adj_iter(self, v):
        for adj in self.g[v]:
            yield adj


class DenseGraph(Graph):
    def __init__(self, *arg):
        super(DenseGraph, self).__init__(*arg)
        self.g = [[0 for _ in xrange(self._vertexs)]
                  for _ in xrange(self._vertexs)]

    def add_edge(self, v1, v2):
        self.g[v1][v2] = 1
        if v1 != v2 and not self._is_directed:
            self.g[v2][v1] = 1

    def has_edge(self, v1, v2):
        return self.g[v1][v2]

    def adj_iter(self, v):
        for i, adj in enumerate(self.g[v]):
            yield i, adj


class SparseWeightedGraph(SparseGraph):
    def __init__(self, *args):
        super(SparseWeightedGraph, self).__init__(*args)

    def add_edge(self, v1, v2, weight):
        if v1 == v2:
            return
        self.g[v1].append(Edge(v1, v2, weight))

        if not self._is_directed:
            self.g[v2].append(Edge(v2, v1, weight))

    def has_edge(self, v1, v2):
        for v in self.g[v1]:
            if v.other(v) == v2:
                return True

    def adj_iter(self, v):
        for adj in self.g[v]:
            yield adj


class DenseWeightedGraph(DenseGraph):
    def __init__(self, *args):
        super(DenseWeightedGraph, self).__init__(*args)

    def add_edge(self, v1, v2, weight):
        self.g[v1][v2] = Edge(v1, v2, weight)

        if not self._is_directed:
            self.g[v2][v1] = Edge(v2, v1, weight)

    def has_edge(self, v1, v2):
        for v in self.g[v1]:
            if v and v.other(v) == v2:
                return True

    def adj_iter(self, v):
        for adj in self.g[v]:
            if adj:
                yield adj