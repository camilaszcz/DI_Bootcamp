
//1. Add the lastname Smith to the object
//2. Change the price of the pear, so it will contain the Taxes. 17%
//3. Ask the user for the fruit he wants between Apple, Banana and Pear. Make sure that your code accept all type of strings, for example "Banana" or "banana" or "BaNaNA"
//4. Console.log the price for the specific fruit the user wants
const userCart = {
	username : "John",
	password: 1234,
	isUserSignedIn : true,
	cart : {
		apple : 2,
		banana : 1,
		pear : 5,
	},
	prices : {
		apple : 0.5,
		banana : 0.8646466363,
		pear : 0.2
	}
};

userCart["lastName"]='Smith';
userCart['prices']['pear']*=0.17;


let selectedFruit =prompt("Choose between Apple, Banana and Pear")
selectedFruit = selectedFruit.toLowerCase()

if (selectedFruit=="apple"){
console.log(userCart['prices']['apple'])};

if (selectedFruit=="banana"){
console.log(userCart['prices']['banana'])};

if (selectedFruit=="pear"){
console.log(userCart['prices']['pear'])};