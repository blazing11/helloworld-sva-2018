function setup() {
  createCanvas(800, 400);
  background(0);
  noStroke();
  fill(0, 255, 0);  
}

var ballX = 400;
var ballY = 100;

var ballXV = -4;
var ballYV = 1;

var rectX_1 = 10;
var rectY_1 = 10;

var rectX_2 = 770;
var rectY_2 = 10;

var lives_1 = 5;
var lives_2 = 5;

function draw() {
  clear();
  background(0);  
  setText_p1();
  setText_p2();
    
  bounceCheck();
  increment();
  scoreCheck(); 


  if (keyIsDown(UP_ARROW)) {
    rectY_2 -= 5;
  }

  if (keyIsDown(DOWN_ARROW)) {
    rectY_2 += 5;
  }

  if (keyIsDown(87)){
    rectY_1 -= 5;
  }
  
  if (keyIsDown(83)){
    rectY_1 +=5;
  }
  
  fill(255);
  ball(ballX, ballY);
  rect(rectX_1, rectY_1, 20, 75);

  
  
  rect(rectX_2, rectY_2, 20, 75);
}

function increment() {  
  ballX += ballXV;  
  ballY += ballYV;
  
  
}

 

function ball(x, y) {
  
  ellipse(x, y, 20, 20);
}


function sliderBounce_1() {
  if(rectY_1 < ballY && rectY_1 + 95 > ballY) {
    ballXV = ballXV* -1;
    
  } 
   if(ballXV > 0){
    ballXV +=1;
  }else{
    ballXV -=1;
  }
  
  if(ballYV > 0){
    ballYV +=1;
  }else{
    ballYV -=1;
  }
}

function sliderBounce_2(){
  if(rectY_2 < ballY && rectY_2 + 95 > ballY ){
    ballXV = ballXV * -1;
    
    
  }
  
  if(ballXV > 0){
    ballXV +=1;
  }else{
    ballXV -=1;
  }
  
  if(ballYV > 0){
    ballYV +=1;
  }else{
    ballYV -=1;
  }
}
  
  
  
function wallBounce() {
  ballXV = ballXV * -1;
  
}

function bounceCheck() {
  if(ballY < 0 || ballY > 400) {
    ballYV = ballYV * -1;
  }
  
  if(ballX < 40 && ballXV < 0) {
    sliderBounce_1();
  }
  
  if(ballX > 760 && ballXV >0){
    sliderBounce_2();
  }
  
  
  
  if(ballX < 0) {
    ballX = 400;
    ballY = 100;
    lives_1 -= 1;
    ballXV = -4;
    ballYV = 1;
  }
    
  if(ballX > 800){
    ballX = 400;
    ballY = 100;
    lives_2 -= 1;
    ballXV = -4;
    ballYV = 1;
  }
}



function scoreCheck() {
  if(lives_1 == 0) {
  textAlign(CENTER);
  textSize(22);
  text("YOU WIN!!!", 700, 20);
  noLoop();
  }
  if(lives_2 == 0) {
  textAlign(CENTER);
  textSize(22);
  text("YOU WIN!!!", 100, 20);
  noLoop();
  }

}

function setText_p1() {
  textAlign(CENTER);
  textSize(22);
  text(lives_1, 10, 20);
}

function setText_p2() {
  textAlign(CENTER);
  textSize(22);
  text(lives_2, 790, 20);
}
