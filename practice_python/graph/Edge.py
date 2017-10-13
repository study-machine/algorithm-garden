class Edge(object):
    def __init__(self, v1, v2, weight):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight

    def other(self, x):
        assert x == self.v1 or x == self.v2
        return self.v2 if x == self.v1 else self.v1

    def __eq__(self, other):
        assert isinstance(other, self.__class__)
        return self.weight == other.weight

    def __lt__(self, other):
        assert isinstance(other, self.__class__)
        return self.weight < other.weight

    def __gt__(self, other):
        assert isinstance(other, self.__class__)
        return self.weight > other.weight

    def __repr__(self):
        return '({}-{},wt:{})'.format(self.v1,self.v2, self.weight)
