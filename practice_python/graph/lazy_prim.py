from min_heap import *

class LazyPrim(object):
    def __init__(self, graph):
        self.graph = graph
        self.min_heap=MinHeap()
        self.marked=[False for _ in xrange(graph.vertexs)]
        self.mst=[]
        self.mst_weight=0

        self._visit(0)
        while not self.min_heap.is_empty():
            e = self.min_heap.extract_min()
            if self.marked[e.v1]==self.marked[e.v2]:
                continue
            self.mst.append(e)

            if not self.marked[e.v1]:
                self._visit(e.v1)
            else:
                self._visit(e.v2)

        if self.mst:
            self.mst_weight = reduce(lambda x,y:x+y,[e.weight for e in self.mst])



    def _visit(self,v):
        assert not self.marked[v]
        self.marked[v]=True
        for e in self.graph.g[v]:
            if not self.marked[e.other(v)]:
                self.min_heap.insert(e)

