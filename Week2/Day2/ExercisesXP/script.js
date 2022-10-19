"Exercise1"

let x=100;
let y=25;

if (x>y){
    console.log('x is the biggest number');
}

"Exercise2"

const newDog='Chihuahua';
const length = newDog.length;


console.log(newDog.toLowerCase());
console.log(newDog.toUpperCase());

if (newDog =='Chihuahua'){
    console.log("I love Chihuahuas, it's my favorite dog breed");
} else {
    console.log("I dont care, I prefer cats");
}


"Exercise3"

const answer = prompt("Tell me a random number");

if (answer % 2==0){
    console.log("The number is even");
}
else{
    console.log("The number is odd");
}

"Exercise4"
const users = ["Lea123", "Helena45", "Camila&inha", "Tamar@000"];
console.log(users.length);

if (users.lenght===0){
    console.log(`no one is online`);
}
else if (users.lenght===1){
    console.log(`${users[0]} is online`);
}
else if (lenght===2){
    console.log(`${users[0]} and ${users[1]} are online`);
}
else if (lenght > 2){
    console.log(`${users[0]}, ${users[1]} and ${users.lenght-2} more are online`);
}
