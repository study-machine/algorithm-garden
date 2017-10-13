from indexMinHeap import *


class Prim(object):
    def __init__(self, graph):
        self.graph = graph
        self.min_heap = IndexMinHeap(graph.vertexs)
        self.edgeTo = [None for _ in xrange(graph.vertexs)]
        self.marked = [False for _ in xrange(graph.vertexs)]
        self.mst = []
        self.mst_weight = 0

        self.visit(0)
        while not self.min_heap.is_empty():
            v = self.min_heap.extract_min_index()
            assert self.edgeTo[v]
            self.mst.append(self.edgeTo[v])
            self.visit(v)
            

        if self.mst:
            self.mst_weight = reduce(
                lambda x, y: x + y, [e.weight for e in self.mst])

    def visit(self, v):
        self.marked[v] = True
        for e in self.graph.g[v]:
            w = e.other(v)
            if not self.marked[w]:
                if not self.edgeTo[w]:
                    self.edgeTo[w] = e
                    self.min_heap.insert(w, e.weight)
                elif e.weight < self.edgeTo[w].weight:
                    self.edgeTo[w] = e
                    self.min_heap.change(w, e.weight)
