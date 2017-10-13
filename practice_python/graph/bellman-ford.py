# -*- coding: utf-8 -*-
# @Time    : 17-10-13 上午10:31
# @Author  : wxy
# @File    : bellman-ford.py
from Edge import *


class BellmanFord(object):
    def __init__(self, graph, s):
        self.graph = graph
        self.s = s
        n = graph.vertexs
        self.dist_to = [0 for _ in xrange(n)]
        self._from = [None for _ in xrange(n)]
        self.has_nc = False

        # Bellman-Ford
        self.dist_to[s] = 0
        self._from[s] = Edge(s, s, 0)

        for i in xrange(1, n):
            for v in xrange(n):
                for e in self.graph.g[v]:
                    if not self._from[e.v2] or self.dist_to[e.v1] + e.wt < self.dist_to[e.v2]:
                        self.dist_to[e.v2] = self.dist_to[e.v1] + e.wt
                        self._from[e.v2] = e

        self.detect_nc()

    def detect_nc(self):
        for v in xrange(self.graph.vertexs):
            for e in self.graph.g[v]:
                if self._from[e.v1] and self.dist_to[e.v1] + e.wt < self.dist_to[e.v2]:
                    return True
        return False