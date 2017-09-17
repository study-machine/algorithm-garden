/**
 * Created by wxy on 17-9-16.
 */
const Color = {
    RED: 'rgba(200,50,50,0.9)',
    BLACK: 'rgba(0,0,0,0.9)'
}

class Stage {
    constructor() {
        this.canvas = document.querySelector('#myCanvas');
        this.canvas.width = document.body.clientWidth;
        this.canvas.height = 3000;
        this.ctx = this.canvas.getContext('2d');
    }

    drawBall(x, y, size) {
        size = size > 10 ? size : 10
        this.ctx.beginPath()
        this.ctx.fillStyle = Color.RED;
        this.ctx.arc(x, y, size, 0, 2 * Math.PI);
        this.ctx.fill()
        this.ctx.closePath()
    }

    drawText(x, y, text, fixX = 0, fixY = 0, fontSize = 20) {
        this.ctx.font = fontSize + "px Monospace";
        this.ctx.fillStyle = Color.BLACK;
        this.ctx.fillText(text.toString(), x - fixX, y - fixY)
    }

    drawLine(starX, starY, endX, endY) {
        this.ctx.beginPath()
        this.ctx.strokeStyle = Color.RED;
        this.ctx.moveTo(starX, starY);
        this.ctx.lineTo(endX, endY);
        this.ctx.closePath()
        this.ctx.stroke();
    }

    clearCanvas() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    }
}
var stage = new Stage()

