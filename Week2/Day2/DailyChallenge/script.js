
"Daily challenge"

let sentence="The food is not bad here!Let's come back.";

let wordNot= sentence.search('not'); // result 12
let wordBad= sentence.search('bad'); // result 16

// 'not bad' is from 12 to 18.
// bad is after good, as 18 is after 12.
//to make sure:

if (wordBad>wordNot){
    console.log('wordBad:'wordBad)
    console.log('wordNot:', wordNot)

    let part1 = sentence.slice(0, wordNot)
    let part2 = sentence.slice(wordBad+3)
    console.log(part1 + "good" + part2)
} else{
    console.log(sentence)
}
//result: 'The food is good here!Let's come back.'