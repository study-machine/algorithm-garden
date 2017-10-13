# -*- coding: utf-8 -*-
# @Time    : 17-10-11 上午11:15
# @Author  : wxy
# @File    : Dijkstra.py

from indexMinHeap import *
from Edge import *


class Dijkstra(object):
    def __init__(self, graph, s):
        self.s = s
        self.graph = graph
        n = graph.vertexs
        self.marked = [False for _ in xrange(n)]
        self.dist_to = [0 for _ in xrange(n)]
        self._from = [None for _ in xrange(n)]
        self.mh = IndexMinHeap(n)

        self._from[s] = Edge(s, s, 0)
        self.marked[s] = True
        self.mh.insert(s, self.dist_to[s])
        while not self.mh.is_empty():
            v = self.mh.extract_min_index()
            self.marked[v] = True
            for e in self.graph.g[v]:
                w = e.other(v)
                if not self.marked[w]:
                    if not self.dist_to[w] or self.dist_to[v] + e.weight < self.dist_to[w]:
                        self.dist_to[w] = self.dist_to[v] + e.weight
                        self._from[w] = e
                    if not self.mh.contain(w):
                        self.mh.insert(w, self.dist_to[w])
                    else:
                        self.mh.change(w, self.dist_to[w])

    def has_path_to(self, w):
        return self.marked[w]

    def shortest_dist_to(self, w):
        if not self.has_path_to(w):
            return False
        return self.dist_to[w]

    def shortest_path(self, w):
        if not self.has_path_to(w):
            return False
        stack = []
        e = self._from[w]
        while e.v1 != self.s:
            stack.insert(0,e)
            e = self._from[e.v1]
        stack.insert(0,e)
        return iter(stack)

    def show_path(self, w):
        if not self.has_path_to(w):
            print 'no path'
            return
        it = self.shortest_path(w)
        while 1:
            try:
                print it.next(),
            except StopIteration:
                print 'ok'
                return
            print '->',
