//1st retrieve the button

const firstBtn = document.getElementById("btn");
// const firstBtn = document.querySelector("#btn");

//syntax
// element.addEventListener(event, function);
// call the function as soon as the event fired
// the function is called a callback function - called only after the event is fired

firstBtn.addEventListener("click", alertUser);
firstBtn.addEventListener("mouseover", alertUser);
firstBtn.addEventListener("mouseout", alertUserTwo);

function alertUser(){
    console.log("You clicked the button");
    document.body.style.backgroundColor = "lightblue";
}

function alertUserTwo(){
    document.body.style.backgroundColor = "pink";
}

// -------------------------------
// with a paragraph

const para = document.querySelector("p");

para.addEventListener("click", welcomeUser);

function welcomeUser() {
    alert("Heyyyy")
}

//Use Toggle
firstBtn.addEventListener("mouseover", alertUser);
firstBtn.addEventListener("mouseout", alertUser);

//callback function - called only after the event is fired
function alertUser(){
    firstBtn.classList.toggle("ocean");
}


//1 retrieve the two buttons

const firstBtn = document.getElementById("btnOne");
const secondBtn = document.getElementById("btnTwo");

firstBtn.addEventListener("click", changeToBlue);
secondBtn.addEventListener("click", changeToRed);

function changeToBlue(){
    document.body.style.backgroundColor="blue"
}

function changeToRed(){
    document.body.style.backgroundColor="red";
}

// ----------------------------
// change the color of the body depending on the textContent of the button
// with the event object

const firstBtn = document.getElementById("btnOne");
const secondBtn = document.getElementById("btnTwo");
firstBtn.addEventListener("click", changeColor);
secondBtn.addEventListener("click", changeColor);

function changeColor(event){
    console.log(event.target); //
    console.log(event.target.textContent);

    const color = event.target.textContent.toLowerCase();
    document.body.style.backgroundColor=color;
}