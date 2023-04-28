// demo 1
// JS event propagation

var tds = document.getElementsByTagName('td');

var clicky = function(e) {
  alert( this.innerHTML );//makes an alert
};

for (var x=0; x < tds.length; x++) {//iterates through table
  tds[x].addEventListener('click', clicky);
}
