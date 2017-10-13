# -*- coding: utf-8 -*-
# @Time    : 17-10-12 下午4:41
# @Author  : wxy
# @File    : Heap.py
from utils import *


def parent(k):
    return (k - 1) / 2


class MinHeap(object):
    def __init__(self, n):
        self.data = [None for _ in xrange(n)]
        self.count = 0

    def insert(self, item):
        self.data[self.count] = item
        self.count += 1
        self.__shift_up(self.count - 1)

    def __shift_up(self, k):
        while parent(k) >= 0 and self.data[k] < self.data[parent(k)]:
            swap(self.data, k, parent(k))
            k = parent(k)

    def extract_min(self):
        ret = self.data[0]
        swap(self.data, 0, self.count - 1)
        self.count -= 1
        self.__shift_down(0)
        return ret

    def __shift_down(self, k):
        while k * 2 + 1 < self.count:
            j = k * 2 + 1
            if j + 1 < self.count and self.data[j + 1] < self.data[j]:
                j += 1
            if self.data[k] < self.data[j]:
                break
            swap(self.data, k, j)
            k = j


def __shift_down(arr, k, n):
    while k * 2 + 1 < n:
        j = k * 2 + 1
        if j + 1 < n and arr[j + 1] < arr[j]:
            j += 1
        if arr[k] < arr[j]:
            break
        swap(arr, k, j)
        k = j


def heap_sort(cls, arr):
    n = len(arr)


if __name__ == '__main__':
    from random import randint

    n = 10
    mh = MinHeap(n)
    for i in xrange(n):
        mh.insert(randint(0, n * 10))
    print mh.data

    for i in xrange(n):
        print mh.extract_min()
