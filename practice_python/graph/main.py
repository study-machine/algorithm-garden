from random import randint, random
from Graph import *
from Component import *
from Path import *
from lazy_prim import *
from prim import *
from kruscal import *
from Dijkstra import *


def gen_connection(n, m):
    return [(randint(0, n - 1), randint(0, n - 1)) for _ in xrange(m)]


def gen_weighted_connection(n, m):
    return [(randint(0, n - 1), randint(0, n - 1), round(random(), 2)) for _ in xrange(m)]


def create_graph(Graph, n, connection):
    g = Graph(n, False)
    for c in connection:
        g.add_edge(*c)
    g.print_graph()
    return g


def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


def test1():
    n = 20
    m = 40
    connection_1 = gen_connection(n, m)
    g1 = create_graph(SparseGraph, n, connection_1)
    g2 = create_graph(DenseGraph, n, connection_1)

    c1 = SparseComponent(g1)
    print c1.components

    c2 = DenseComponent(g2)
    print c2.components

    p1 = SparsePath(g1, 0)
    p1.show_path(5)

    p2 = DensePath(g2, 0)
    p2.show_path(5)

    sp1 = SparseShortestPath(g1, 0)
    sp1.show_path(5)

    sp2 = DenseShortestPath(g2, 0)
    sp2.show_path(5)


def test2():
    n = 20
    m = 40
    connection_2 = gen_weighted_connection(n, m)
    g3 = create_graph(SparseWeightedGraph, n, connection_2)
    g4 = create_graph(DenseWeightedGraph, n, connection_2)

    c3 = SparseWeightedComponent(g3)
    print c3.components

    c4 = DenseWeightedComponent(g4)
    print c4.components

    p3 = WeightedPath(g3, 0)
    p3.show_path(5)

    p4 = WeightedPath(g4, 0)
    p4.show_path(5)

    sp3 = WeightedShortestPath(g3, 0)
    sp3.show_path(5)

    sp4 = WeightedShortestPath(g4, 0)
    sp4.show_path(5)


def test3():
    n = 6
    m = 6
    connection_2 = gen_weighted_connection(n, m)
    g3 = create_graph(SparseWeightedGraph, n, connection_2)
    c3 = SparseWeightedComponent(g3)
    print 'components:', c3.components
    p3 = WeightedShortestPath(g3, 0)
    for i in xrange(1, n):
        p3.show_path(i)
    print '=' * 20

    lazy_prim = LazyPrim(g3)
    print 'mst:', lazy_prim.mst
    print 'mst weight:', lazy_prim.mst_weight

    prim = Prim(g3)
    print 'mst:', prim.mst
    print 'mst weight:', prim.mst_weight

    kruscal = Kruscal(g3)
    print 'mst:', kruscal.mst
    print 'mst weight:', kruscal.mst_weight


def test4():
    n = 10
    m = 20
    connection = gen_weighted_connection(n, m)
    g = create_graph(SparseWeightedGraph, n, connection)
    sp = WeightedShortestPath(g, 0)
    for i in xrange(n):
        sp.show_path(i)
    print "-" * 10
    dij = Dijkstra(g, 0)
    for i in xrange(n):
        print i, dij.shortest_dist_to(i),
        dij.show_path(i)


if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    test4()
