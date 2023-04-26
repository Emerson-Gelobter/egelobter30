var c = document.getElementById("playground");
var dotButton = document.getElementById("circle");
var dvdButton = document.getElementById("dvd");
var stopButton = document.getElementById("stop");

var ctx = c.getContext("2d");

ctx.fillStyle = "red";

var requestID;

var radius = 0;
var growing = true;
var animating = false;

var drawDot = (e) => {
    if (e.type == "click" && animating) {
        return
    }
    animating = true;
    clear();

    ctx.beginPath();
    ctx.arc(c.width / 2, c.height / 2, radius, 0, Math.PI * 2);
    ctx.fillStyle = "red";
    ctx.fill();

    if (growing == true){
        radius += 1;
    }
    else {
        radius -= 1;
    }
    if (radius > c. width / 2){
        growing = false;
    }
    if (radius == 0){
        growing = true;
    }
    requestID = window.requestAnimationFrame(drawDot);
}

var stopIt = function() {
    window.cancelAnimationFrame(requestID);
    animating = false;
}

var clear = funtion(e){
  e.preventDefault();
  ctx.clearRect(0,0,500,500);
};

var dvdLogoSetup = function(){
  window.cancelAnimationFrame(requestID);
  var rectWidth = 100;
  var rectHeight = 50;
  var rectX = Math.floor(Math.random(c.width));
  var rectY = Math.floor(Math.random(c.height));

  var xVel = 2;
  var yVel = 2;
  var logo = new Image();
  logo.src = "logo_dvd.jpg"
  var dvdLogo = function(){
    ctx.clearRect(0, 0, c.width, c.height);
    //ctx.fillRect(rectX, rectY, rectWidth, rectHeight);
    ctx.drawImage(logo, rectX, rectY, rectWidth, rectHeight);
    if(rectX >= c.width || rectX<=0){
      xVel *= -1 ;

    }
    if(rectY >=c.height || rectY<=0){
      yVel *= -1 ;
    }
    rectX = rectX + xVel;
    rectY = rectY + yVel;
    requestID = window.requestAnimationFrame(dvdLogoSetup());

  };
  dvdLogo();

};

var stopIt = function() {
    window.cancelAnimationFrame(requestID);

};


dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);
dvdButton.addEventListener("click", dvdLogoSetup);
