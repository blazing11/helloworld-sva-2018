var hand;

function preload() {
  hand = loadImage ('leg_R.png');
}

function setup() {
  createCanvas(500, 300);
}

function draw() {
  background(255);
  image(hand, 270, 50);
  
}