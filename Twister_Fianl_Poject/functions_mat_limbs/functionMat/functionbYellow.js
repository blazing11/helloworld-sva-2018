var mat;

function preload() {
  mat = loadImage ('bYellow.png');
}

function setup() {
  createCanvas(500, 300);
}

function draw() {
  background(255);
  image(mat, 70, 50);
  
}