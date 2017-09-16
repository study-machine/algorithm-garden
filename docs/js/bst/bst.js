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
        if (this.count) {
            var node = this.root
            while (node.left)
                node = node.left;
            return node
        }
    }

    maximum() {
        if (this.count) {
            var node = this.root
            while (node.right)
                node = node.right;
            return node
        }
    }

    removeMin(node) {
        this.root = this.__removeMin(this.root)
    }

    __removeMin(node) {
        if (!node)
            return
        if (!node.left) {
            this.count--
            return node.right

        }
        node.left = this.removeMin(node.left)
        return node
    }

    remove(k) {

    }

    __remove(node, k) {

    }


}
