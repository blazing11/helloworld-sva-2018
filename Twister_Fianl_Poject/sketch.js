let serial; // variable to hold an instance of the serialport library
let portName = "/dev/cu.usbmodem143301"; // fill in your serial port name here
let inString;
let inData; // data from Arduino!
let youCansend = false;
let p1Check = false;
let p2Check = false;
let count = 0;
let usedSquare;
let lastColor;
let lastPlayer;
let youCanstrart = false;

let hand;
let mat;

let picA;
let picB;
let picC;
let picD;
let picE;
let picF;
let picG;
let picH;
let picI;

let leftH;
let rightH;
let leftF;
let rightF;

let losePic;

let gameStarted;
let gifLoad;
let img;

let t = 0;
let k = 0;
let startGif;
let gif_createImg;
let back;
let interval;
let interval_2;

let counter = 8;
// let spinner;

let limbs = new Array(); //put those elements into player1's array
limbs[0] = "leftHand";
limbs[1] = "rightHand";
limbs[2] = "leftFeet";
limbs[3] = "rightFeet";

let square = ["A", 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'];
// var square = ["A", 'B'];

let redArray = ["A", "E", "I"];
let yellowArray = ["B", "F", "G"];
let blueArray = ["C", "D", "H"];

let lastLimb;

let lastSquare;
let lastLimb2;

let p1Used = [];
let p2Used = [];
let totalUsed = p1Used.concat(p2Used)

function preload() {
  // load images
  img = loadImage('Twister_image/logo_2.jpg');
  picA = loadImage('Twister_image/aRed.png');
  picB = loadImage("Twister_image/bYellow.png");
  picC = loadImage("Twister_image/cBlue.png");
  picD = loadImage("Twister_image/dBlue.png");
  picE = loadImage("Twister_image/eRed.png");
  picF = loadImage("Twister_image/fYellow.png");
  picG = loadImage("Twister_image/gYellow.png");
  picH = loadImage("Twister_image/hBlue.png");
  picI = loadImage("Twister_image/iRed.png");
  back = loadImage('Twister_image/whiteback.jpg');

  leftH = loadImage("Twister_image/hand_L.png");
  rightH = loadImage("Twister_image/hand_R.png");
  leftF = loadImage("Twister_image/leg_L.png");
  rightF = loadImage("Twister_image/leg_R.png")

  losePic = loadImage("Twister_image/lose.png");

}

function setup() {
  createCanvas(500, 300); // make the canvas

  serial = new p5.SerialPort(); // make a new instance of the serialport library
  serial.on('data', serialEvent); // callback for when new data arrives

  serial.open(portName); // open a serial port

  serial = new p5.SerialPort(); // make a new instance of the serialport library
  serial.on('list', printList); // set a callback function for the serialport list event
  serial.on('connected', serverConnected); // callback for connecting to the server
  serial.on('open', portOpen); // callback for the port opening
  serial.on('data', serialEvent); // callback for when new data arrives
  serial.on('error', serialError); // callback for errors
  serial.on('close', portClose); // callback for the port closing

  serial.list(); // list the serial ports
  serial.open(portName); // open a serial port/ callback for the port closing
  // createCanvas(500, 300);
  // img = loadImage("logo_2.jpg");  // Load the image
  startButton = createButton('Start Game');
  startButton.position(212, 230);
  startButton.mousePressed(startGame);
  setInterval(timeIt,1000);
  gameStarted = false;

}

function draw() {
  // black background, white text:
  background(255);
  image(img, 0, 0);

  if (lastSquare == "A") {
    showA();
  }
  if (lastSquare == "B") {
    showB();
  }
  if (lastSquare == "C") {
    showC();
  }
  if (lastSquare == "D") {
    showD();
  }
  if (lastSquare == "E") {
    showE();
  }
  if (lastSquare == "F") {
    showF();
  }
  if (lastSquare == "G") {
    showG();
  }
  if (lastSquare == "H") {
    showH();
  }
  if (lastSquare == "I") {
    showI();
  }


  // console.log("count: ",count);
  if(count%2==1){
    if (lastLimb == "leftHand") {
      showleftHand();
    }
    if (lastLimb == "rightHand") {
      showrightHand();
    }
    if (lastLimb == "leftFeet") {
      showleftFeet();
    }
    if (lastLimb == "rightFeet") {
      showrightFeet();
    }
  }

  if(count%2==0){
    if (lastLimb2 == "leftHand") {
      showleftHand();

    }
    if (lastLimb2 == "rightHand") {
      showrightHand();

    }
    if (lastLimb2 == "leftFeet") {
      showleftFeet();

    }
    if (lastLimb2 == "rightFeet") {
      showrightFeet();

    }
  }

  if (inString == "lose") {
    loseSequence();
  }

  if (gameStarted == true) {

    startButton.hide();

    if (t < 520 && k == 0) {
      gif_createImg = createImg("Twister_image/twister.gif");
      gif_createImg.position(0, 0);
      k = k + 1;
    } else if (t >= 520 && k != 0) {
      gif_createImg.hide(gif_createImg);
      textSize(24);
      fill(0);
      text(str(lastPlayer), 220, 40);


      // setInterval(timeIt,1000);
      textSize(24);
      fill(0);
      text("You have "+ counter+" sec left", 180, 280);



    }

    t = t + 1;

  }

}


function serverConnected() {
  print('connected to server.');
}

function portOpen() {
  print('the serial port opened.')
}

function serialError(err) {
  print('Something went wrong with the serial port. ' + err);
}

function portClose() {
  print('The serial port closed.');
}

function serialEvent() {

  inString = serial.readLine();
}

function printList(portList) {

  for (var i = 0; i < portList.length; i++) {

    print(i + " " + portList[i]);
  }
}

function serverConnected() {
  print('connected to server.');
}

function portOpen() {
  print('the serial port opened.')
}


//Game logic function =======================================

function everySetting() {

  serial.write(usedSquare);

  setTimeout(startDet, 7550);



  // console.log("current player: ", lastPlayer);
  textSize(24);
  fill(0);
  text(str(lastPlayer), 250, 80);

  // console.log("color: ", lastColor);
  // console.log("usedSquare: ", usedSquare);
  // console.log("player1: ", p1Used);
  // console.log("player2: ", p2Used);
  // console.log("count: ", count);

}

function startDet() {
  serial.write(lastSquare);
  // console.log("Lest's detect: ", lastSquare);

}

function random_limbs() {

  lastLimb = limbs[Math.floor(Math.random() * limbs.length)];
  if (p1Used.includes(lastLimb)) {
    var i = p1Used.indexOf(lastLimb);
    usedSquare = p1Used[i = i + 1];
    if (usedSquare == 'A') {
      usedSquare = 'J';
    }
    if (usedSquare == 'B') {
      usedSquare = 'K';
    }
    if (usedSquare == 'C') {
      usedSquare = 'L';
    }
    if (usedSquare == 'D') {
      usedSquare = 'M';
    }
    if (usedSquare == 'E') {
      usedSquare = 'N';
    }
    if (usedSquare == 'F') {
      usedSquare = 'O';
    }
    if (usedSquare == 'G') {
      usedSquare = 'P';
    }
    if (usedSquare == 'H') {
      usedSquare = 'Q';
    }
    if (usedSquare == 'I') {
      usedSquare = 'R';
    }

    p1Used[p1Used.indexOf(lastLimb)] = null;

    p1Used[i] = null;
    p1Used.splice(p1Used.indexOf(null), 1);
    p1Used.splice(p1Used.indexOf(null), 1);
    return lastLimb;
    return usedSquare;

  } else {
    return lastLimb;
  }

}

function random_limbs2() {

  lastLimb2 = limbs[Math.floor(Math.random() * limbs.length)];
  if (p2Used.includes(lastLimb2)) {
    var z = p2Used.indexOf(lastLimb2);
    usedSquare = p2Used[z = z + 1];

    if (usedSquare == 'A') {
      usedSquare = 'J';
    }
    if (usedSquare == 'B') {
      usedSquare = 'K';
    }
    if (usedSquare == 'C') {
      usedSquare = 'L';
    }
    if (usedSquare == 'D') {
      usedSquare = 'M';
    }
    if (usedSquare == 'E') {
      usedSquare = 'N';
    }
    if (usedSquare == 'F') {
      usedSquare = 'O';
    }
    if (usedSquare == 'G') {
      usedSquare = 'P';
    }
    if (usedSquare == 'H') {
      usedSquare = 'Q';
    }
    if (usedSquare == 'I') {
      usedSquare = 'R';
    }
    p2Used[p2Used.indexOf(lastLimb2)] = null;

    p2Used[z] = null;
    p2Used.splice(p2Used.indexOf(null), 1);
    p2Used.splice(p2Used.indexOf(null), 1);

    return lastLimb2;
    return usedSquare;
  } else {
    return lastLimb2;
  }

}


function random_square() {

  lastSquare = square[Math.floor(Math.random() * square.length)];
  if (!p1Used.includes(lastSquare) && !p2Used.includes(lastSquare)) {

    return lastSquare;
  } else {
    random_square();

  }

}

function p1NewRound() {

  random_square();
  random_limbs();
  saveP1(lastLimb, lastSquare);

  return {
    "limb": lastLimb,
    "square": lastSquare
  };

}

function p2NewRound() {

  random_square();
  random_limbs2();
  saveP2(lastLimb2, lastSquare);

  return {
    "limb": lastLimb2,
    "square": lastSquare
  };

}

function playNextround() {

  if (count % 2 == 0) {

    p1NewRound();
    // test_color();

    lastPlayer = "player1";

  }
  if (count % 2 == 1) {
    p2NewRound();
    // test_color();

    lastPlayer = "player2";

  }

  count = count + 1;


  return lastPlayer;

}

function saveP1(lastLimb, lastSquare) {

  p1Used.splice(0, 0, lastLimb, lastSquare);
  return p1Used;
}

function saveP2(lastLimb2, lastSquare) {

  p2Used.splice(0, 0, lastLimb2, lastSquare);
  return p2Used;
}

function loseSequence() {
  background(255);
  image(losePic, 0, 0);

  noLoop();
}

function startGame() {
  // change gameStarted variable
  gameStarted = true;
  // start the interval
  interval = setInterval(playNextround, 8000);
  interval_2 = setInterval(everySetting, 8000);


}

function showA() {
  background(255);
  image(picA, 70, 50);
}

function showB() {
  background(255);
  image(picB, 70, 50);
}

function showC() {
  background(255);
  image(picC, 70, 50);
}

function showD() {
  background(255);
  image(picD, 70, 50);
}

function showE() {
  background(255);
  image(picE, 70, 50);
}

function showF() {
  background(255);
  image(picF, 70, 50);
}

function showG() {
  background(255);
  image(picG, 70, 50);
}

function showH() {
  background(255);
  image(picH, 70, 50);
}

function showI() {
  background(255);
  image(picI, 70, 50);
}

function showleftHand() {
  image(leftH, 270, 50);

}

function showrightHand() {
  image(rightH, 270, 50);
}

function showleftFeet() {
  image(leftF, 270, 50);
}


function showrightFeet() {
  image(rightF, 270, 50);
}

function showleftHand2() {
  image(leftH2, 270, 50);
}

function showrightHand2() {
  image(rightH2, 270, 50);
}

function showleftFeet2() {
  image(leftF2, 270, 50);
}

function showrightFeet2() {
  image(rightF2, 270, 50);
}

function timeIt(){
  counter--;
  if (counter == 0){
    counter = 8;
  }
}
