// demo 2
// JS event propagation

var tds = document.getElementsByTagName('td');
var trs = document.getElementsByTagName('tr');
var table = document.getElementsByTagName('table')[0];

var clicky = function(e) {
  alert( this.innerHTML ); //creates browser alert
};

for (var x=0; x < tds.length; x++) { // iterates through table data
  tds[x].addEventListener('click', clicky);
}

for (x=0; x < trs.length; x++) { // iterates through table rows
  trs[x].addEventListener('click', clicky);
}

table.addEventListener('click', clicky);


// Q: When user clicks on a cell, in what order will the pop-ups appear?
// cell ==> row ==> table
