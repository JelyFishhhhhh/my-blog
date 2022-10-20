var type_inx=0;
var slogan="Talk is cheap. Show the code.";
var speed = 35;
document.getElementById('type').innerHTML="";
function typer(){
    document.getElementById('type').innerHTML += slogan.charAt(type_inx)
    type_inx++;
    setTimeout(typer, speed);
}

// typer();

for (let i = 0; i < page_list.length; i++) {
    if (page_list[i].id == "type") {
        typer();
    }
}