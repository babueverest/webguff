function button1Command(event) {
alert("button 1 command " + event);
}

function button2Command(event) {
alert("button 2 command" + event);
}

function initialize( ) {
var b1 = document.getElementById("signup");
var b2 = document.getElementById("signin");
b1.onclick = button1Command;
b2.onclick = button2Command;
}

