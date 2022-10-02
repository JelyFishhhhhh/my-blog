function includeHTML(i=0) {
    let include_list = document.getElementsByTagName("ih");
    if (i >= include_list.length) {
        return
    }
    let element = include_list[i];
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 404) {element.innerHTML = "Page not found.";}
            else {element.innerHTML = this.responseText;}
            element.ready = true;
        }
    }
    xhttp.open("GET", `/templates/${element.id}.html`, true);
    xhttp.send();
    setTimeout(includeHTML, 0, i+1)
}