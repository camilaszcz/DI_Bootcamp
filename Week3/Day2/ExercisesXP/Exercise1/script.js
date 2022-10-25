// Part I
    
//     In your Javascript file, using setTimeout, call a function after 2 seconds.
//     The function will alert “Hello World”.


//Answer:


// const Button = document.getElementById("clear");
// Button.addEventListener("click", greeting);

// function greeting(){
//     alert("Hello World");
//   }
  
//   setTimeout(greeting, 2000);


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
  
//setTimeout(greeting, 2000);


    
//     Part III
    
//     In your Javascript file, using setInterval, call a function every 2 seconds.
//     The function will add a new paragraph <p>Hello World</p> to the <div id="container">.

//     The interval will be cleared (ie. clearInterval), when the user will click on the button.
//     Instead of clicking on the button, the interval will be cleared (ie. clearInterval) as soon as there will be 5 paragraphs 
//     inside the <div id="container">.

//Answer, got stuck:
    
const node = document.createElement("container");
const textnode = document.createTextNode("Hello World");

document.addEventListener("appendChild", greeting);
document.getElementById("container").appendChild(node);

let timer = setInterval(greeting, 2000);

function greeting() {
    node.appendChild(textnode)
}

function clear() {
  clearInterval(timer);
}

//Using clearInterval() to stop :
//clearInterval(myInterval, 10000);


