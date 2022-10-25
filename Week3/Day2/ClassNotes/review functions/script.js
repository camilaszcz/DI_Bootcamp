const username = "Tom"; //global variable
// use const to declare the variable
// because you dont want to change the variable

// everything declared in the global scope is accessible in the local scope
function checkUsername (){
    if(username==="John"){
        console.log("hello");
    }
}

function addLastname (){
    const fullName = username + " Smith";
    console.log(fullName); // Tom Smith
}

// Other example
// what matters is where you invoke the function
// not where you create it


let bottles = 25; //change the variable

function increaseBottles (){
    bottles = bottles + 10;
}

function decreaseBottles (){
    bottles = bottles - 1; 
}

decreaseBottles() //24
increaseBottles() //24+10 -- 34

increaseBottles() //34+10 = 44
decreaseBottles() //44-1 = 43
decreaseBottles() //43-1 = 42


//OTHER EXAMPLE


function calculateHotel (){
    let hotelCost = 100;
    hotelCost *= 2;
    return hotelCost;
}

function calculateCar (){
    let carCost = 20;
    carCost -= 2;
    return carCost;
}

function calculateTotal () {
    // const total = hotelCost+carCost; //undefined
    const hotel = calculateHotel() //200
    const car = calculateCar() // 18
    const total = hotel + car; //200+18
    console.log(total);
}

calculateTotal()