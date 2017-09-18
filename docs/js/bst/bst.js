/**
 * Created by wxy on 17-9-16.
 */
class Node {
    constructor(k, v, parent, level) {
        this.k = k;
        this.v = v;

        this.parent = parent;
        this.level = level;

        this.left = null;
        this.right = null;
    }

}
class BST {
    constructor() {
        this.root = null;
        this.count = 0;
    }


    nodeLevel(k) {
        var node = this.search(k)
        return this.__nodeLevel(node)
    }

    __nodeLevel(node) {
        if (!node)
            return -1;
        var l = 0;
        while (node.parent) {
            l++;
            node = node.parent;
        }
        return l
    }

    insert(k, v) {
        this.root = this.__insert(this.root, k, v)
    }

    __insert(node, k, v, parent = null) {
        if (!node) {
            this.count++;
            var parentLevel = this.__nodeLevel(parent);
            return new Node(k, v, parent, parentLevel + 1)
        }
        if (k === node.k)
            node.v = v;
        if (k < node.k)
            node.left = this.__insert(node.left, k, v, node);
        if (k > node.k)
            node.right = this.__insert(node.right, k, v, node);
        return node
    }

    search(k) {
        return this.__search(this.root, k);
    }

    __search(node, k) {
        if (!node)
            return null;
        if (k === node.k)
            return node;
        else if (k < node.k)
            return this.__search(node.left, k);
        else
            return this.__search(node.right, k);
    }

    preOrder() {
        this.__preOrder(this.root);
    }

    __preOrder(node) {
        if (!node)
            return;
        log(node.k, node.v, node.level);
        this.__preOrder(node.left);
        this.__preOrder(node.right);
    }

    inOrder() {
        this.__inOrder(this.root);
    }

    __inOrder(node) {
        if (!node)
            return;
        log(node.k, node.v, node.level);
        this.__inOrder(node.left);
        log(node.k, node.v, node.level);
        this.__inOrder(node.right);
    }

    levelOrder() {
        var l = [];
        l.push(this.root);
        while (l.length > 0) {
            var node = l.shift();
            log(node.k, node.v, node.level);
            if (node.left) l.push(node.left);
            if (node.right) l.push(node.right);
        }
    }

    minimum() {
        return this.__minimum(this.root).k
    }

    __minimum(node) {
        while (node.left)
            node = node.left;
        return node
    }

    maximum() {
        if (this.count) {
            var node = this.root
            while (node.right)
                node = node.right;
            return node
        }
    }

    removeMin() {
        this.root = this.__removeMin(this.root)
    }

    __removeMin(node) {
        // debugger
        if (!node)
            return
        if (!node.left) {
            this.count--
            // 同时修改parent
            if (node.right)
                node.right.parent = node.parent;
            return node.right

        }
        node.left = this.__removeMin(node.left)
        return node
    }

    removeMax() {
        this.root = this.__removeMax(this.root)
    }

    __removeMax(node) {
        if (!node)
            return
        if (!node.right) {
            this.count--
            // 同时修改parent
            if (node.left)
                node.left.parent = node.parent;
            return node.left

        }
        node.right = this.__removeMax(node.right)
        return node
    }

    remove(k) {
        if (!this.count)
            return;
        this.root = this.__remove(this.root, k)
        if (this.root)
            this.root.level = 0
    }

    __remove(node, k) {
        if (!node)
            return;
        if (k < node.k) {
            node.left = this.__remove(node.left, k);
            return node
        }
        if (k > node.k) {
            node.right = this.__remove(node.right, k);
            return node
        }

        if (k === node.k) {
            if (!node.left) {
                this.count--;
                if (node.right)
                    node.right.parent = node.parent;
                return node.right
            }
            else if (!node.right) {
                this.count--;
                if (node.left)
                    node.left.parent = node.parent;
                return node.left
            }
            else {//左右都有节点
                // debugger
                // successor取代node，父亲和孩子都要修改
                var successor = this.__minimum(node.right)

                successor.right = this.__removeMin(node.right)
                successor.left = node.left

                successor.parent = node.parent;

                if (successor.left)
                    successor.left.parent = successor;
                if (successor.right)
                    successor.right.parent = successor;
                successor.level = this.__nodeLevel(successor)

                return successor
            }
        }

    }


}
