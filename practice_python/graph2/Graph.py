# -*- coding: utf-8 -*-
# @Time    : 17-10-12 下午2:49
# @Author  : wxy
# @File    : Graph.py
from Edge import *


class Graph(object):
    def __init__(self, n, is_directed=False):
        self.vertexs = n
        self.edges = 0
        self.is_directed = is_directed
        self.g = []

    def show(self):
        for i in xrange(self.vertexs):
            print i, self.g[i]


class SpareGraph(Graph):
    def __init__(self, *args):
        super(SpareGraph, self).__init__(*args)
        self.g = [[] for _ in xrange(self.vertexs)]

    def has_edge(self, v, w):
        return w in self.g[v]

    def add_edge(self, v, w):
        if v == w or self.has_edge(v, w):
            return
        self.g[v].append(w)
        if not self.is_directed:
            self.g[w].append(v)
        self.edges += 1


class SparseWeightGraph(Graph):
    def __init__(self, *args):
        super(SparseWeightGraph, self).__init__(*args)
        self.g = [[] for _ in xrange(self.vertexs)]

    def has_edge(self, v, w):
        for x in self.g[v]:
            if g[v][x].other(x) == w:
                return True
        return False

    def add_edge(self, v, w, wt):
        if v == w:
            return
        self.g[v].append(Edge(v, w, wt))
        if not self.is_directed:
            self.g[w].append(Edge(w, v, wt))
        self.edges += 1
