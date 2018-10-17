var serial;	// variable to hold an instance of the serialport library
var portName = "/dev/cu.usbserial-DN05135L";  // fill in your serial port name here
var inString;

var xspacing = 16;   // How far apart should each horizontal location be spaced
var w;              // Width of entire wave

var savedTime;
var totalTime = 10000;
var passedTime;
var calmSavedTime;
var calmTotalTime = 2*totalTime;
var calmPassedTime;
var something = 0;
var decrement = 0;
var getbigger = false;
var aNumber;
var theta = 0.0;  // Start angle at 0
var amplitude = 15.0;  // Height of wave
var period = 500.0;  // How many pixels before the wave repeats
var dx;  // Value for incrementing X, a function of period and xspacing
var yvalues= [];  // Using an array to store height values for the wave
var invar;


function setup() {
  createCanvas(640, 360);
  	
 serial = new p5.SerialPort();// make a new instance of the serialport library
 serial.on('list', printList); 		// set a callback function for the serialport list event
 serial.on('data', serialEvent);    // callback for when new data arrives
 
 // change the data rate to whatever you wish
 var options = { baudrate: 9600};
 serial.open(portName, options);
  w = width+16 ;
  dx = (TWO_PI / period) * xspacing; 
  //TWO_PI is a mathematical constant with the value 6.2831855. It is twice the ratio of the circumference of a circle to its diameter.
  for (var x = 0; x < w/xspacing ;x++) {
    yvalues[x] = aNumber
}
  //prvarArray(Serial.list());
  
  savedTime = millis();
  calmSavedTime = millis();
}



function draw() {
  background(0);
  calcWave();
  renderWave();
  
  calmPassedTime = millis() - calmSavedTime;
  
  if (calmPassedTime > calmTotalTime);{
    calmSavedTime = millis();
   //prvarln("calmSavedTime: " + calmSavedTime);
   //prvarln("totalTime: " + totalTime);
    decrement = map(calmPassedTime, 0, 2*totalTime, 0, 5);
    amplitude = amplitude - 25*decrement;
    amplitude = constrain(amplitude, 15, 80);
    //prvarln("amplitude normal: " + amplitude);
    period = 1000;
  }

  passedTime = millis() - savedTime;
  // Has five seconds passed?
  if (passedTime > totalTime) {// after 10 sec... reset wave
    savedTime = millis(); // Save the current time to restart the timer!
    
    getbigger = false;
  }

  if (getbigger== true) { // when a gesture is triggered do this....
    something = map(passedTime, 0, totalTime, 0, 5);
    amplitude = amplitude + something/5;
    amplitude = constrain(amplitude, 15, 80);
  //  prvarln("amplitude getting big: " + amplitude);
    period = 1000;
  }else{
   
    amplitude = amplitude - decrement/5;
    period = 500;
  
  }
  
  
  
  //prvarln(passedTime);
 

}


function serialEvent() {
  // read a string from the serial port:
  inString = serial.readLine();
  print( "we have data!: " + str(inString));

  // check to see that there’s actually a string there:
  if (inString.length >  0 ) {
  
    if ("LEFT"== str(inString)) {
      getbigger = true;
     
    }
    if ("RIGHT"== str(inString)) {
      getbigger = true;
      
    }
    if ("NONE"== str(inString)) {

      getbigger = false;
     
    }

  }
  
}
function calcWave() {
  // Increment theta (try different values for 'angular velocity' here y speed
  print (str(inString))
  theta += 0.02;
  if ("LEFT" == str(inString)) {
    theta += 0.03;
  }

  if ("RIGHT" == str(inString)) {
    theta -= 0.065;
  }

  if ("NONE" == str(inString)) {
    theta += 0.02;
  }
  // For every x value, calculate a y value with sine function
  var x = theta;
  for (var i = 0; i < yvalues.length; i++) {   //need to find out 
    yvalues[i] = sin(x)*amplitude;  // need to find out 
    x+=dx;
  }
}

function renderWave() {
  noStroke();
  fill(255);
  // A simple way to draw the wave with an ellipse at each location

  for (var z = 0; z <500; z= z+20) {

    for (var x = 0; x < yvalues.length; x++) {

      ellipse(x*xspacing, (height/2+z+(yvalues[x])), 8, 8);
    }
  }
}
function printList(portList) {
  // portList is an array of serial port names
  for (var i = 0; i < portList.length; i++) {
    // Display the list the console:
 	print(i + " " + portList[i]);
   }
}