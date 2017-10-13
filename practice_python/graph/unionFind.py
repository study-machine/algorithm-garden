class UnionFind(object):
    def __init__(self, n):
        self.count = n
        self.parent = [i for i in xrange(n)]
        self.rank = [0 for i in xrange(n)]

    def find(self, p):
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def union_element(self, p1, p2):
        p1_root = self.find(p1)
        p2_root = self.find(p2)

        if p1_root == p2_root:
            return
        if self.rank[p1_root]   < self.rank[p2_root]  :
            self.parent[p1_root] = p2_root
        elif self.rank[p1_root]   > self.rank[p2_root]  :
            self.parent[p2_root] = p1_root
        else:
            self.parent[p1_root] = p2_root
            self.rank[p2_root] += 1

    def is_connected(self, p1, p2):
        return self.find(p1) == self.find(p2)


