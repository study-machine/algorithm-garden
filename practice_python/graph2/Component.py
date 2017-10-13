# -*- coding: utf-8 -*-
# @Time    : 17-10-12 下午3:00
# @Author  : wxy
# @File    : Component.py

class Component(object):
    def __init__(self, graph):
        self.graph = graph
        n = graph.vertexs
        self.visted = [False for _ in xrange(n)]
        self.id = [0 for _ in xrange(n)]
        self.ccount = 0

        for v in xrange(n):
            if not self.visted[v]:
                self.dfs(v)
                self.ccount += 1

    def dfs(self, v):
        self.visted[v] = True
        self.id[v] = self.ccount
        for w in self.graph.g[v]:
            if not self.visted[w]:
                self.dfs(w)
