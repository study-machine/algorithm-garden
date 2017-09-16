/**
 * Created by wxy on 17-9-16.
 */

var canvas = document.querySelector('#myCanvas');
canvas.width = document.body.clientWidth;
canvas.height = 3000;
var ctx = canvas.getContext('2d');
ctx.fillStyle = '#abc';
ctx.fillStyle = "rgba(200, 0, 0, 0.5)";
ctx.font = "20px Monospace";





function clearCanvas(ctx, canvas) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}