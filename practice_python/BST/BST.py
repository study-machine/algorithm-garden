from random import randint


class Node(object):
    def __init__(self, k, left=None, right=None):
        self.k = k
        self.left = left
        self.right = right

    def __repr__(self):
        return '{},(l:{},r:{})'.format(self.k, self.left, self.right)
        # left = 'l:' + str(self.left.k) if self.left else ''
        # right = 'r:' + str(self.right.k) if self.right else ''
        # return '{},({},{})'.format(self.k, left, right)


def do_something(node):
    print node


class BST(object):
    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, k):
        self.root = self.__insert(self.root, k)

    def __insert(self, node, k):
        if not node:
            self.count += 1
            return Node(k)
        if k == node.k:
            return node
        elif k < node.k:
            node.left = self.__insert(node.left, k)
        else:
            node.right = self.__insert(node.right, k)
        return node

    def pre_order(self):
        self.__pre_order(self.root)

    def __pre_order(self, node):
        if not node:
            return
        do_something(node)
        if node.left:
            self.__pre_order(node.left)
        if node.right:
            self.__pre_order(node.right)

    def post_order(self):
        self.__post_order(self.root)

    def __post_order(self, node):
        if not node:
            return
        if node.left:
            self.__post_order(node.left)
        if node.right:
            self.__post_order(node.right)
        do_something(node)

    def in_order(self):
        print 'inOrder'
        self.__in_order(self.root)

    def __in_order(self, node):
        if not node:
            return
        if node.left:
            self.__in_order(node.left)
        do_something(node)
        if node.right:
            self.__in_order(node.right)

    def level_order(self):
        q = []
        node = self.root
        q.append(node)
        while q:
            node = q.pop(0)
            do_something(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def minimum(self):
        if not self.root:
            return
        return self.__minimum(self.root)

    def __minimum(self, node):
        if not node.left:
            return node
        else:
            return self.__minimum(node.left)

    def remove_min(self):
        self.root = self.__remove_min(self.root)

    def __remove_min(self,node):
        if not node:
            return
        if not node.left:
            self.count-=1
            return node.right

        node.left = self.__remove_min(node.left)
        return node
    def contain(self, k):
        node = self.root
        while node:
            if k == node.k:
                return True
            elif k < node.k:
                node = node.left
            else:
                node = node.right
        return False

    def remove(self, k):
        if self.contain(k):
            self.root = self.__remove(self.root, k)

    def __remove(self, node, k):
        if not node:
            return
        if k < node.k:
            node.left = self.__remove(node.left,k)
            return node
        elif k > node.k:
            node.right = self.__remove(node.right,k)
            return node
        else:
            if not node.left:
                 return node.right
            elif not node.right:
                return node.left
            else:
                print 'test'
                successor = Node(self.__minimum(node.right).k)
                node.right = self.__remove_min(node.right)
                successor.left = node.left
                successor.right = node.right
                return successor

class BST2(object):
    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, k):
        if not self.root:
            self.root = Node(k)
            return

        node = self.root
        while 1:
            if k == node.k:
                return
            elif k < node.k:
                if node.left:
                    node = node.left
                else:
                    node.left = Node(k)
                    return
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = Node(k)
                    return

    def in_order(self):
        stack = []
        node = self.root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            if stack:
                node = stack.pop()
                do_something(node)
                node = node.right

    def pre_order(self):
        stack = []
        node = self.root
        while node or stack:
            while node:
                do_something(node)
                stack.append(node)
                node = node.left
            if stack:
                node = stack.pop()
                node = node.right

    def level_order(self):
        q = []
        node = self.root
        q.append(node)
        while q:
            node = q.pop(0)
            do_something(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def contain(self, k):
        node = self.root
        while node:
            if k == node.k:
                return True
            elif k < node.k:
                node = node.left
            else:
                node = node.right
        return False

    def minimum(self):
        return self.__minimum(self.root)

    def __minimum(self,node):
        if not node:
            return
        while node:
            if not node.left:
                node = node.left
            else:
                return node

    def find_father(self,k):
        father = None
        node = self.root
        while node:
            if k == node.k:
                return father
            else:
                father = node
                if k < node.k:
                    node = node.left
                else:
                    node = node.right
        return False



    def remove_min(self):
        self.__remove_min(self.root)

    def __remove_min(self,node):
        if not node:
            return
        while node.left:
            if not node.left.left:
                node.left = node.left.right
                return
            else:
                node = node.left




def test():
    bst = BST()
    bst2 = BST2()
    n = 10
    arr = [randint(0, n - 1) for _ in xrange(n)]
    for i in arr:
        i = randint(0,99)
        bst.insert(i)
        bst2.insert(i)

    # bst.level_order()
    bst2.level_order()
    print '=' * 10

    # bst.in_order()
    # print '=' * 10
    # bst2.in_order()
    # print '*' * 10

    # bst.remove(bst.root.k)
    # bst.level_order()
    print bst2.find_father(bst.minimum().k).k

    # bst2.level_order()


if __name__ == '__main__':
    test()
