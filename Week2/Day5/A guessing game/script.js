

    // //   In the function, start by asking the user if they would like to play the game (Hint: use the built-in confirm() function).

    function playTheGame(){
    const userPreference = confirm("Would you like to play a game?");

if (!userPreference){
    alert ('No problem, goodbye!')
    return
}
    const answer=prompt('Please enter a number');
    if (onlyNum(answer)){
        alert ('This is not a number. Try again')
    }


    console.log = ("Lets guess a number!");

    function guessNumber() {

    // generating a random integer from 1 to 10
    const random = Math.floor(Math.random() * 10) + 1;

    // take input from the user
    const guess = parseInt(prompt('Guess a number from 1 to 10: '));

    //   If the user didn’t enter a number
    
    while(guess){
        console.log('Sorry, not a number. Try again')
    }
    if (random < guess) {
        alert("You are too high!");
    }
    if (random > guess){
        alert("Your are too low!");
    }
    // take the input until the guess is correct
    while(number !== random) {
        number = parseInt(prompt('Guess a number from 1 to 10: '));
    }

    // check if the guess is correct
    if(number == random) {
        console.log('You guessed the correct number.');
    }
    

    function onlyNum(str){
        const regex = new RegExp (/^[0-9]*$/)
        return regex.text(str)
    }