from Graph import *


class Component(object):
    def __init__(self, graph):
        self._graph = graph
        n = graph.vertexs
        self._visited = [False for _ in xrange(n)]
        self._id = [False for _ in xrange(n)]
        self._c_count = 0

        for i in xrange(graph.vertexs):
            if not self._visited[i]:
                self.dfs(i)
                self._c_count += 1

    def dfs(self, v):
        pass

    def is_connected(self, v1, v2):
        return self._id[v1]==self._id[v2]

    @property
    def components(self):
        return self._c_count


class SparseComponent(Component):
    def __init__(self, *args):
        super(SparseComponent, self).__init__(*args)

    def dfs(self, v):
        self._visited[v] = True
        self._id[v] = self._c_count
        for i in self._graph.g[v]:
            if not self._visited[i]:
                self.dfs(i)


class DenseComponent(Component):
    def __init__(self, *args):
        super(DenseComponent, self).__init__(*args)

    def dfs(self, v):
        self._visited[v] = True
        self._id[v] = self._c_count
        for i, b in enumerate(self._graph.g[v]):
            if b and not self._visited[i]:
                self.dfs(i)


class SparseWeightedComponent(SparseComponent):
    def __init__(self, *args):
        super(SparseWeightedComponent, self).__init__(*args)

    def dfs(self, v):
        self._visited[v] = True
        self._id[v] = self._c_count
        for e in self._graph.g[v]:
            if not self._visited[e.v2]:
                self.dfs(e.v2)


class DenseWeightedComponent(DenseComponent):
    def __init__(self, *args):
        super(DenseWeightedComponent, self).__init__(*args)

    def dfs(self, v):
        self._visited[v] = True
        self._id[v] = self._c_count
        for e in self._graph.g[v]:
            if e and not self._visited[e.v2]:
                self.dfs(e.v2)

