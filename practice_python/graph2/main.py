# -*- coding: utf-8 -*-
# @Time    : 17-10-12 下午2:56
# @Author  : wxy
# @File    : main.py
from random import random, randint
from Graph import *
from Component import *
from Path import *


def print_dec():
    print '=' * 20


def gen_graph(GraphClass, n, m):
    g = GraphClass(n)
    for i in xrange(m):
        g.add_edge(randint(0, n - 1), randint(0, n - 1))
    g.show()
    return g


def gen_wt_graph(GraphClass, n, m):
    g = GraphClass(n)
    for i in xrange(m):
        g.add_edge(randint(0, n - 1), randint(0, n - 1), round(random(), 2))
    g.show()
    return g


def get_component(g):
    c = Component(g)
    print 'components:'
    print c.ccount, c.id
    return c


def show_path(PathClass, g, s):
    p = PathClass(g, s)
    for i in xrange(g.vertexs):
        print i, p.show_path(i)
    return p


if __name__ == '__main__':
    g = gen_wt_graph(SparseWeightGraph,10,15)
    p2 = show_path(ShortestWeightPath, g, 0)

