/**
 * Created by wxy on 17-9-16.
 */
const RootX = canvas.width / 2;
const RootY = 50;
const PosOffset = canvas.width / 5;
const BallSize = 20 + canvas.width / 100

class BallNode extends Node {
    constructor(k, v, parent, level, direction) {
        super(k, v, parent, level, direction)
        this.x = RootX;
        this.y = RootY;
        if (direction !== 0) {
            this.x = parent.x + (PosOffset * direction) / level + 1;
            this.y = RootY * (level + 1);
        }
        if (parent) {
            // linkBall(parent.x, parent.y, this.x, this.y)
        }
        // drawBall(this.x, this.y, k, level)
    }
}
class BallBST extends BST {
    __insert(node, k, v, parent = null, direction = 0) {
        if (!node) {
            this.count++;
            var parentLevel = this.__nodeLevel(parent);
            return new BallNode(k, v, parent, parentLevel + 1, direction)
        }
        if (k === node.k)
            node.v = v;
        if (k < node.k)
            node.left = this.__insert(node.left, k, v, node, -1);
        if (k > node.k)
            node.right = this.__insert(node.right, k, v, node, 1);
        return node
    }


    __inOrder(node) {
        if (!node)
            return;

        this.__inOrder(node.left);
        this.__drawBall(node)
        this.__linkBall(node)
        this.__inOrder(node.right);
    }

    __drawBall(node) {
        var x = node.x
        var y = node.y
        var fix = node.level
        var text = node.k.toString()
        ctx.beginPath()
        ctx.fillStyle = "rgba(200, 60, 60, 1)";
        ctx.arc(x, y, BallSize - fix * 2, 0, 2 * Math.PI)
        ctx.fill()
        ctx.closePath()
        ctx.fillStyle = "#000";

        ctx.fillText(text.toString(), x - 10, y)
    }

    __linkBall(node) {
        if (!node.parent)
            return;
        var p = node.parent;
        var direction = 0;
        if (p.left && p.left === node)
            direction = -1;
        else if (p.right && p.right === node)
            direction = 1;
        node.x = p.x + (PosOffset * direction) / node.level + 1;
        node.y = RootY * (node.level + 1);

        ctx.beginPath()
        ctx.strokeStyle = "rgba(200, 0, 0, 0.3)";
        ctx.moveTo(p.x, p.y);
        ctx.lineTo(node.x, node.y);
        ctx.closePath()
        ctx.stroke();
    }
}


// function drawBall(x, y, k, fix) {
//     ctx.beginPath()
//     ctx.fillStyle = "rgba(200, 60, 60, 1)";
//     ctx.arc(x, y, BallSize - fix * 2, 0, 2 * Math.PI)
//     ctx.fill()
//     ctx.closePath()
//     ctx.fillStyle = "#000";
//
//     ctx.fillText(k.toString(), x - 10, y)
// }
// function linkBall(startX, startY, endX, endY) {
//     ctx.beginPath()
//     ctx.strokeStyle = "rgba(200, 0, 0, 0.3)";
//     ctx.moveTo(startX, startY);
//     ctx.lineTo(endX, endY);
//     ctx.closePath()
//     ctx.stroke();
// }

