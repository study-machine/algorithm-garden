# -*- coding: utf-8 -*-
# @Time    : 17-10-12 下午3:52
# @Author  : wxy
# @File    : Edge.py
from functools import total_ordering


@total_ordering
class Edge(object):
    def __init__(self, v1, v2, wt):
        self.v1 = v1
        self.v2 = v2
        self.wt = wt

    def other(self, v):
        assert v in [self.v1, self.v2]
        return self.v2 if v == self.v1 else self.v1

    def __repr__(self):
        return '({},{},{})'.format(self.v1, self.v2, self.wt)

    def __lt__(self, other):
        return self.wt < other.wt

    def __eq__(self, other):
        return self.wt == other.wt
