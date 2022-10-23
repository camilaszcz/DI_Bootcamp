//Daily Challenge

const answer = prompt('Type a few words separated by commas');
const words = answer.split(",");

function getLengthOfLongestWord(){
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
    const spaces= lenghtOfLongestWord - word.length;
    const emptySpaces = " ".repeat(spaces);
    console.log(`*${word}${spaces}*`);

}

function getLengthOfLongestWord(){
    let lenghtOfLongestWord=0;
    for (const word of words){
    const wordLength = word.length;
    if (wordLength>lengthOfLongestWord){
        lengthOfLongestWord = wordLength;
    }
}
return lenghtOfLongestWord;
}

function createFirstRow() {

    const numberOfStarsOnFirstRow = lenghtOfLongestWord+4;

    let row = "";
    for (let i=0<numberOfStarsOnFirstRow; i++) {
        row=row+"*";
    }
    return row;
} 
