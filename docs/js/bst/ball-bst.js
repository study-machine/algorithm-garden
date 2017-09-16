/**
 * Created by wxy on 17-9-16.
 */
const RootX = stage.canvas.width / 2;
const RootY = 50;
const PosOffset = stage.canvas.width / 5;
const BallSize = 20 + stage.canvas.width / 100

class BallNode extends Node {
    // constructor(k, v, parent, level, direction) {
    //     super(k, v, parent, level, direction)
    //     // this.x = RootX;
    //     // this.y = RootY;
    //     // if (direction !== 0) {
    //     //     this.x = parent.x + (PosOffset * direction) / level + 1;
    //     //     this.y = RootY * (level + 1);
    //     // }
    // }
}
class BallBST extends BST {
    constructor(stage) {
        super();
        this.stage = stage
    }


    __insert(node, k, v, parent = null, direction = 0) {
        if (!node) {
            this.count++;
            var parentLevel = this.__nodeLevel(parent);
            return new BallNode(k, v, parent, parentLevel + 1, direction)
        }
        if (k === node.k)
            node.v = v;
        if (k < node.k)
            node.left = this.__insert(node.left, k, v, node,);
        if (k > node.k)
            node.right = this.__insert(node.right, k, v, node);
        return node
    }


    __preOrder(node) {
        // 这里必须用preOrder来update,layerOrder也可以，inOrder和postOrder都不行
        // 因为，递归下去再回来，父球没有定位xy，子球也没法定位
        if (!node)
            return;
        this.__updateXY(node)
        this.__drawBall(node)
        this.__linkBall(node)
        this.__preOrder(node.left);
        this.__preOrder(node.right);
    }


    __updateXY(node) {
        var p = node.parent
        if (!p) {
            node.x = RootX;
            node.y = RootY;
            return
        }
        var direction = 0;
        if (p.left && p.left === node)
            direction = -1;
        else if (p.right && p.right === node)
            direction = 1;

        node.x = p.x + (PosOffset * direction) / node.level + 1;
        node.y = RootY * (node.level + 1);
    }


    __drawBall(node) {
        var size = BallSize - node.level * 2
        this.stage.drawBall(node.x, node.y, size)
        this.stage.drawText(node.x, node.y, node.k, (8 - node.level))
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
        this.stage.drawLine(node.x, node.y, p.x, p.y)
    }

    removeMin() {
        this.root = this.__removeMin(self.root)
        this.inOrder()
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

