var type_inx=0;
var slogan="Talk is cheap. Show the code.";
var speed = 35;
document.getElementById('type').innerHTML="";
function typer(){
    document.getElementById('type').innerHTML += slogan.charAt(type_inx)
    type_inx++;
    setTimeout(typer, speed);
}

typer();