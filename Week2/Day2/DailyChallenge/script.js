
"Daily challenge"

let sentence="The food is not bad here!Let's come back.";

let wordNot= sentence.search('not'); // result 12
let wordBad= sentence.search('bad'); // result 16

// so 'not bad' is from 12 to 18.
// bad is after good, as 18 is after 12.

let newSentence=sentence.replace("not bad", "good");

console.log(newSentence);
//result: 'The food is good here!Let's come back.'