function handleForm() {
    let link = document.getElementById('link');
    let zip = document.getElementById('zip');
    let button = document.getElementById('compileButton');


    if(link.value != "") {
        zip.disabled = true;
    } else {
        zip.disabled = false;
    }

    if(zip.files.length > 0) {
        link.disabled = true;
    } else {
        link.disabled = false;
    }

    if (link.value != "" || zip.files.length != 0) {
        button.disabled = false;
    } else {
        button.disabled = true;
    }
}