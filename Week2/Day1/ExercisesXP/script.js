"Exercise 1"

const favoriteFood = "pizza";
const favoriteMeal = "dinner";

const sentence = `I eat ${favoriteFood} at every ${favoriteMeal}`;

console.log(sentence);

"Exercise 2"

const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
const myWatchedSeriesLength = 3;
const myWatchedSeriesSentence = `I watched ${myWatchedSeriesLength}:${myWatchedSeries}`;

console.log(myWatchedSeriesSentence);

myWatchedSeries[2]="friends";
myWatchedSeries.push("Seinfeld");
myWatchedSeries.splice(0,0, "The Office");
myWatchedSeries.splice(1,1);

const letterthree = myWatchedSeries[1];
const letterthree1 = letterthree[2];

console.log(letterthree1);

console.log(myWatchedSeries);

"Exercise 3"

const celsius= 30;
const farenheit = celsius/5*9+32;
const temperature= `The temperature ${celsius} in celsius is ${farenheit} in farenheit`;

console.log(temperature);


"Exercise 4"

let c;
let a = 34;
let b = 21;

console.log(a+b) //first expression
// Prediction: 55 as both are numbers
// Actual:55

a = 2;

console.log(a+b) //second expression
// Prediction: 23 as a was redefined
// Actual:23

//What will be the outcome of a + b in the first expression ?55
//What will be the outcome of a + b in the second expression ?23
//What is the value of c? undefined

console.log(3 + 4 + '5');
// Prediction:75 as 3 and 4 are numbers and 5 is a string
// Actual:75

//Exercise 5

typeof("potato")
// Prediction: Vegetable
// Actual: String

typeof(15)
// Prediction:number
// Actual:number

typeof(5.5)
// Prediction:number
// Actual:number

typeof(NaN)
// Prediction: didn't know
// Actual:number

typeof("hello")
// Prediction:string
// Actual:string

typeof(true)
// Prediction:boolean
// Actual:boolean

typeof(1 != 2)
// Prediction:boolean
// Actual:boolean

"hamburger" + "s"
// Prediction:hamburgers
// Actual:hamburgers

"hamburgers" - "s"
// Prediction:hamburgers
// Actual:NaN

//`13`
// Prediction:13
// Actual:13

"1" - "3"
// Prediction:-2
// Actual:-2

"johnny" + 5
// Prediction:johnny5
// Actual:johnny5

"johnny" - 5
// Prediction:johnny
// Actual:NaN

99 * "hello"
// Prediction:99hello
// Actual:NaN

1 != 1
// Prediction:false
// Actual:false

1 == "1"
// Prediction:true
// Actual:true

1 === "1"
// Prediction:false
// Actual:false


//Exercise 6

5 + "34"
// Prediction:534
// Actual:

5 - "4"
// Prediction:1
// Actual:1

10 % 5
// Prediction:5/10
// Actual:0

5 % 10
// Prediction:10/5
// Actual:5

"Java" + "Script"
// Prediction:JavaScript
// Actual:JavaScript

" " + " "
// Prediction:  " "
// Actual:" "

" " + 0
// Prediction:0
// Actual:  0 

true + true
// Prediction:2
// Actual:2

true + false
// Prediction:1
// Actual:1

false + true
// Prediction:1
// Actual:1

false - true
// Prediction:-1
// Actual:-1

!true
// Prediction:false
// Actual:false

3 - 4
// Prediction:-1
// Actual:-1

"Bob" - "bill"
// Prediction:didn't know
// Actual:NaN











