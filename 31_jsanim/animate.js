var c = document.getElementById("slate");//Get canvas
var dotButton = "buttonCircle";//Get dotButton
var stopButton = ;

var wipeCanvas = () => {
  console.log("wiping canvas...")
  ctx.clearRect(0,0,c.clientWidth,c.clientHeight)
  console.log("ET VIOLA.  eh?")
}

var ctx = ;
ctx.fillstyle = ;
var requestID;

var clear = (e) => {
};
var radius = 0;
var growing = true;

var drawDot = () =>{

};

var stopIt = () => {
  console.log("stopIt invoked")
  console.log(requstID);
};

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);
