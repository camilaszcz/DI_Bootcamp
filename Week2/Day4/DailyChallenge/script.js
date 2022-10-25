//Daily Challenge

const answer = prompt ('Type a few words separated by commas');
const words = answer.split(",");

console.log(words);


function getLengthOfLongestWord(){
    let row = 0;
    for (let i=0; i<numberOfStarsOnFirstRow; i++) {
        if (words[i].lenght>row){
            row=words[i].length;
        }
    }
    return row;
const lenghtOfLongestWord = getLengthOfLongestWord();
displayRows();
}

function displayRows(){
    const firstRow = createFirstRow();
    console.log(firstRow);
    for (const word of words){
        displayWord(word);
        }
    console.log(firstRow);
}

function displayWord(word){
    const spaces= getLengthOfLongestWord - word.length;
    const emptySpaces = " ".repeat(spaces);
    console.log(`*${word}${spaces}*`);
}

function getLengthOfLongestWord(){
    let lenghtOfLongestWord = 0;
    for (const word of words){
    const wordLength = word.length;
    if (wordLength>lenghtOfLongestWord){
        lenghtOfLongestWord = wordLength;
    }
}
return lenghtOfLongestWord;
}

function createFirstRow() {

    const numberOfStarsOnFirstRow = lenghtOfLongestWord + 4;


} 
