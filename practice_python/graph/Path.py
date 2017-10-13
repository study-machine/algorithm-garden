from Graph import *


class Path(object):
    def __init__(self, graph, s):
        self._graph = graph
        self._s = s
        n = graph.vertexs
        self._visited = [False for _ in xrange(n)]
        self._from = [-1 for _ in xrange(n)]

        self.dfs(s)

    def dfs(self, v):
        pass

    def has_path(self, w):
        return self._visited[w]

    def path(self, w):
        stack = []
        p = w
        while p != -1:
            stack.insert(0, p)
            p = self._from[p]
        return iter(stack)

    def show_path(self, w):
        if not self.has_path(w):
            print 'no path'
            return
        it = self.path(w)
        while 1:
            try:
                print it.next(),
            except StopIteration:
                print 'ok'
                return
            print '->',


class SparsePath(Path):
    def __init__(self, *args):
        super(SparsePath, self).__init__(*args)

    def dfs(self, v):
        self._visited[v] = True
        for i in self._graph.adj_iter(v):
            if not self._visited[i]:
                self._visited[i] = True
                self._from[i] = v
                self.dfs(i)


class DensePath(Path):
    def __init__(self, *args):
        super(DensePath, self).__init__(*args)

    def dfs(self, v):
        self._visited[v] = True
        for i, b in self._graph.adj_iter(v):
            if b and not self._visited[i]:
                self._visited[i] = True
                self._from[i] = v
                self.dfs(i)


class SparseShortestPath(Path):
    def __init__(self, *args):
        super(SparseShortestPath, self).__init__(*args)
        self._ord = [False for _ in xrange(self._graph.vertexs)]

        self.bfs(self._s)

    def bfs(self, v):
        q = []
        q.insert(0, v)
        self._visited[v] = True
        self._ord[v] = 0
        while q:
            v = q.pop()
            for i in self._graph.adj_iter(v):
                if not self._visited[i]:
                    q.insert(0, i)
                    self._visited[i] = True
                    self._from[i] = v
                    self._ord[i] = self._ord[v] + 1


class DenseShortestPath(Path):
    def __init__(self, *args):
        super(DenseShortestPath, self).__init__(*args)
        self._ord = [False for _ in xrange(self._graph.vertexs)]

        self.bfs(self._s)

    def bfs(self, v):
        q = []
        q.insert(0, v)
        self._visited[v] = True
        self._ord[v] = 0
        while q:
            v = q.pop()
            for i, b in self._graph.adj_iter(v):
                if b and not self._visited[i]:
                    q.insert(0, i)
                    self._visited[i] = True
                    self._from[i] = v
                    self._ord[i] = self._ord[v] + 1


class WeightedPath(Path):
    def __init__(self, *args):
        super(WeightedPath, self).__init__(*args)

    def dfs(self, v):
        self._visited[v] = True
        for e in self._graph.adj_iter(v):
            i = e.v2
            if not self._visited[i]:
                self._visited[i] = True
                self._from[i] = v
                self.dfs(i)


class WeightedShortestPath(Path):
    def __init__(self, *args):
        super(WeightedShortestPath, self).__init__(*args)
        self._ord = [False for _ in xrange(self._graph.vertexs)]

        self.bfs(self._s)

    def bfs(self, v):
        q = []
        q.insert(0, v)
        self._visited[v] = True
        self._ord[v] = 0
        while q:
            v = q.pop()
            for e in self._graph.adj_iter(v):
                i = e.v2
                if not self._visited[i]:
                    q.insert(0, i)
                    self._visited[i] = True
                    self._from[i] = v
                    self._ord[i] = self._ord[v] + 1
