//WORK WITH METHODS AND PROPERTIES

const pet = "cat";
const answerUser = prompt("What is your favorite animal"); // CAT, caT

// check if the value of the variable pet, is equal to the value of the variable userAnswer
// make sure that the answer of the user is lowercase
// METHOD toLowerCase()
console.log(pet === answerUser.toLowerCase()); //true


const email = "john@gmail.com";
// METHOD includes()
const isEmailGood = email.includes('@'); //true

//FIND THE LETTER BASED ON POSITION
const sentence = "hello";
// variable[position of letter]
const firstLetter = sentence[0]; //h
const letterFour = sentence[4]; //o

//FIND THE POSITION BASED ON THE LETTER
const positionOfH = sentence.indexOf("h") //position 0

//LENGTH OF THE WORD
const lengthWord =  sentence.length;

//FIND THE LAST LETTER BASED ON THE LENGTH OF THE STRING
// // to be equal to the lastletter of the word
const positionLastLetter = sentence[sentence.length-1]
                            // sentence[5-1]
                            // sentence[4] --> last letter
const positionLastLetter2 = sentence[lengthWord-1];

// // ---- ARRAYS

// SYNTAX
// array : [item,item,item]

// const all = ["Adidas", 2, true, "Nike"];


const shoe1 = "ADIDAS";
const shoe2 = "Nike";

//array - list
const allShoes = ["Adidas", "Nike", "Puma"];

//RETRIEVE AN ITEM FROM THE ARRAY
console.log(allShoes[1]) //"Nike"
console.log(allShoes[1][2]); //"k" in word Nike

// LENGTH OF THE ARRAY - HOW MANY ITEMS IN THE ARRAY
console.log(allShoes.length); //3

// INDEX OF THE ITEM NIKE
console.log(allShoes.indexOf("Nike")); //1

// FIND THE LAST ITEM IN THE ARRAY DEPENDING ON THE LENGTH
console.log(allShoes[allShoes.length-1]); //last item in the array

// WITH NESTED ARRAYS

const shoes = [["AdidasBlue","AdidasRed"], "Nike", "Puma"];
// console.log(shoes[0])
//     // (2) ['AdidasBlue', 'AdidasRed']
console.log(shoes[0][1]); //'AdidasRed'



const colors = ["blue","red","yellow"];
// find the element at the specific index and modify it
// red is at position 1

// CHANGE THE ELEMENT AT THE POSITION 1 - FROM RED TO PINK
colors[1] = "pink";

colors.push("green") // add at the end of the array
colors.pop() // delete at the end of the array


// SPLICE METHOD
// array.splice(begining of the index, how many we want to delete, what do add)

// Add the color white after the color red
colors.splice(2,0,"white");

// Add green at the position 1, and delete 2 items from position 1
colors.splice(1,2,"green");

// delete the first element of the array
colors.splice(0,1);