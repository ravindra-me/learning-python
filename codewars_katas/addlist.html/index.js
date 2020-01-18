var button=document.getElementById("enter");
var input= document.getElementById("userinput");
var ul= document.getElementById("ul");
function inputlength(){
    return input.value.length;
}
function creatListElement(){
    var li=document.createElement("li");
    li.appendChild(document.createTextNode(input.value));
    ul.appendChild(li);
    input.value="";

}
button.addListAfterClick() {
    if(inputlength() >0) {
        creatListElement();
    }    
}
button.addListAfterKeyPress(event){
    if(inputlength()>0 && event.KeyCode==13){
        creatListElement();
    }
}
button.addEventListener("click",addListAfterClick);
button.addEventListener("keypress", addListAfterKeyPress);