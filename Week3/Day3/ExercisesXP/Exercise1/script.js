// Part I
    
//     In your Javascript file, using setTimeout, call a function after 2 seconds.
//     The function will alert “Hello World”.

//Answer:

// function greeting(){
//     alert("Hello World");
//   }
//   setTimeout(greeting, 2000);

//result: alert appears after 2 seconds

//     Part II
    
//     In your Javascript file, using setTimeout, call a function after 2 seconds.
//     The function will add a new paragraph <p>Hello World</p> to the <div id="container">.

//Answer:

// const node = document.createElement("container");
// const textnode = document.createTextNode("Hello World");

// document.addEventListener("appendChild", greeting);
// document.getElementById("container").appendChild(node);

// function greeting(){
//     node.appendChild(textnode);
//   }
  
// setTimeout(greeting, 2000);

//Result: adds hellow world, but how to define it as paragraph?

    
//     Part III
    
//     In your Javascript file, using setInterval, call a function every 2 seconds.
//     The function will add a new paragraph <p>Hello World</p> to the <div id="container">.

//     The interval will be cleared (ie. clearInterval), when the user will click on the button.
//     Instead of clicking on the button, the interval will be cleared (ie. clearInterval) as soon as there will be 5 paragraphs 
//     inside the <div id="container">.

//Answer, got stuck:
    

const node = document.createElement("container");
const textnode = document.createTextNode("Hello World");


setInterval(greeting, 2000);

function greeting(){
    node.appendChild(textnode);
  }
  

  // setInterval(function to call, delay)

// setInterval(sayHi, 1000); //I want to call the sayHi function EVERY second

// function sayHi(){
//     console.log("hello");
// }

// // --------------------
// // clearInterval(index of the interval)
// // -------------------

// const timerOne = setInterval(addDiv, 1000);//global variable
// //decalred in the global scope
// // I create an interval, that calls the function addDiv everysecond
// let counter = 0;

// //add the div, 10 times
// function addDiv (){
//     counter++;
//     if(counter <= 3) {
//         const section = document.getElementById("wrapper")
//         const myDiv = document.createElement("div");
//         myDiv.textContent = "hello";
//         myDiv.classList.add("banner");
//         section.appendChild(myDiv);
//     } else {
//         clearInterval(timerOne) //clearInterval(1)
//         console.log(timerOne);
//     }
// }

// // const intervalOne = setInterval(sayHi, 1000); //id 1
// // const intervalAgain = setInterval(sayHi, 1000); // 2

// // function sayHi (){
// //     console.log("hello");
// // }

// // setInterval() //1
// // setInterval() //2
// // setInterval()
// // setInterval()





// //Using clearInterval() to stop :
// //clearInterval(myInterval, 10000);


let divContainer = document.getElementById("container");
let newP = document.createElement("p");
let textP = document.createTextNode("hello world")

function helloP () {
    newP.appendChild(textP);
    divContainer.appendChild(newP);
}
setTimeout(helloP, 2000);
let myInterval = setInterval (addP2, 2000);
function addP2 () {
    let newP2 = document.createElement("p");
    let textP2 = document.createTextNode("hello world p2");
    newP2.appendChild(textP2);
    divContainer.appendChild(newP2);
}

let btn = document.getElementById("clear");
btn.addEventListener("click", clear);

function clear() {
    clearInterval(myInterval);
}