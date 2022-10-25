// const planets = ["Earth", "Neptune", "Jupiter"];

// for i
// for of

//when you need to use the index
for (let i=0; i<planets.length; i++){
    console.log(`The #${i+1} planet is ${planets[i]}`);
}

// when I don't need to an index
for (const chocolate of planets){
    console.log(`The planet is ${chocolate}`);
}


//Add the planets to the page
const planets = ["Earth", "Neptune", "Jupiter"];

function addPlanet () {
    const sectionElement = document.querySelector("section");
    for(const item of planets){
        const divPlanet = document.createElement("div");
        divPlanet.classList.add("planet");
        sectionElement.appendChild(divPlanet);
    }
}

addPlanet();

//Add the planets to the page and passing an inline style depending
// on an array of colors
const planetsTwo = ["Earth", "Neptune", "Jupiter"];
const colors = ["blue", "red", "yellow"];

function addPlanetTwo () {
    const sectionElement = document.querySelector("section");
    for(let i = 0; i<planetsTwo.length; i++){
        const divPlanet = document.createElement("div");
        divPlanet.classList.add("planet");
        divPlanet.style.backgroundColor = colors[i];
        sectionElement.appendChild(divPlanet);
    }
}

addPlanetTwo();

//Add the planets to the page and passing an inline style depending
// on an array of objects
// we use the color property
const planetsThree = [
    {
        name: "Earth",
        color:"blue",
        moons: 5,
    },
    {
        name: "Neptune",
        color:"red",
        moons: 2,
    },
    {
        name: "Jupiter",
        color:"yellow",
        moons: 1,
    }
];

function addPlanetThree () {
    const sectionElement = document.querySelector("section");
    for(const item of planetsThree){
        const divPlanet = document.createElement("div");
        divPlanet.classList.add("planet");
        divPlanet.style.backgroundColor=item["color"];
        sectionElement.appendChild(divPlanet);

        //create the moons
        const numberMoons = item["moons"];
        // loop depending on the nb on moons, create a div per moon
        // add a class of moon in each div

    }
}

addPlanetThree();

// -----------------------
// const planets = [
//     {
//         name: "Earth",
//         color:"blue",
//     },
//     {
//         name: "Neptune",
//         color:"red",
//     },
//     {
//         name: "Jupiter",
//         color:"yellow",
//     }
// ];

// console.log(planets[0].color); //find the color of the first planet

//-----------------------------
// REVIEW ON FOR OF with array
// const colors = ["blue", "red", "yellow"];

// for (const a of colors){

// }
// //1st loop
// a = "blue"
// a = "red"

//---------------------------------
// REVIEW ON FOR OF with array of objects
// const colors = [{name:"John"},{name:"Tom"},{name:"Jane"}];

// for (const a of colors){
//     console.log(a);
// }

// 1st loop
// a = {name:"John"}
// a.name
// a["name"]

// 2nd loop
// a = {name:"Tom"}

// -------------------------------
// Square bracket notation with objects
const family = {
    john: "dad",
    lea: "daughter",
}


console.log(family.john);
console.log(family["john"]);

const username = prompt('whats your name');
// username="john"

//dot notation doesnt work with variable
console.log(family.username); //undefined
console.log(family[username]); //family["john"]
