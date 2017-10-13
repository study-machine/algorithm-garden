from min_heap import *
from unionFind import *
from Component import *

class Kruscal(object):
    def __init__(self, graph):
        self.graph = graph
        self.min_heap = MinHeap()
        self.mst = []
        self.mst_weight=0
        component = SparseWeightedComponent(graph)
        root = 0
        for v in xrange(graph.vertexs):
            for e in graph.adj_iter(v):
                if component.is_connected(root,e.v1) or component.is_connected(root,e.v2):
                    self.min_heap.insert(e)      
        uf = UnionFind(graph.vertexs)
        while not self.min_heap.is_empty() and len(self.mst) < graph.vertexs:
            e = self.min_heap.extract_min()
            if uf.is_connected(e.v1,e.v2):
                continue
            self.mst.append(e)
            uf.union_element(e.v1,e.v2)
        if self.mst:
            self.mst_weight= reduce(lambda x,y:x+y,[e.weight for e in self.mst ])