# -*- coding: utf-8 -*-
# @Time    : 17-10-12 下午3:08
# @Author  : wxy
# @File    : Path.py


class Path(object):
    def __init__(self, g, s):
        self.graph = g
        self.s = s
        n = g.vertexs
        self.visited = [False for _ in xrange(n)]
        self._from = [-1 for _ in xrange(n)]

    def has_path(self, v):
        return self.visited[v]

    def path_to(self, v):
        s = []
        while v != -1:
            s.insert(0, v)
            v = self._from[v]
        return s

    def show_path(self, v):
        if not self.has_path(v):
            return 'no path'
        s = self.path_to(v)
        return '->'.join(map(lambda x: str(x), s))


class DFSPath(Path):
    def __init__(self, *args):
        super(DFSPath, self).__init__(*args)

        self.dfs(self.s)

    def dfs(self, v):
        self.visited[v] = True
        for w in self.graph.g[v]:
            if not self.visited[w]:
                self._from[w] = v
                self.dfs(w)


class ShortestPath(Path):
    def __init__(self, *args):
        super(ShortestPath, self).__init__(*args)
        self.ord = [0 for _ in xrange(self.graph.vertexs)]

        self.bfs(self.s)

    def bfs(self, s):
        q = [s]
        self.visited[s] = True
        while q:
            v = q.pop()
            for w in self.graph.g[v]:
                if not self.visited[w]:
                    self.visited[w] = True
                    self._from[w] = v
                    self.ord[w] = self.ord[v] + 1
                    q.insert(0, w)


class ShortestWeightPath(ShortestPath):
    def __init__(self, *args):
        super(ShortestWeightPath, self).__init__(*args)

    def bfs(self, s):
        q = [s]
        self.visited[s] = True
        while q:
            v = q.pop()
            for e in self.graph.g[v]:
                w = e.other(v)
                if not self.visited[w]:
                    self.visited[w] = True
                    self._from[w] = v
                    self.ord[w] = self.ord[v] + 1
                    q.insert(0, w)


class Dijkstra(object):
    def __init__(self, graph, s):
        self.graph = graph
        self.s = s
        n = graph.vertexs
        self.marked = [False for _ in xrange(n)]
        self.dist_to = [0 for _ in xrange(n)]
        self._from = [-1 for _ in xrange(n)]

