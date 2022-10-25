// Create an input type text that takes/shows only letters. (ie. numbers and special characters won’t be accepted)

// Hint: use one of the following events to remove any character that is not a letter

// keyup event
// or keypress event
// or keydown event
// or input event

// Hint : Check out keycodes in Javascript or Regular Expressions

// keydown: It fires when any key is pressed down.
// keypress: It fires only when a key that produces a character value is pressed down. 
// For example, if you press the key a, this event will fire as the key a produces a character value of 97. 
//On the other hand, this event will not fire when you press the shift key as it doesn't produce a character value.
// keyup: It fires when any key is released.

document.getElementById("demo").addEventListener("keydown", myFunction);

// If the pressed keyboard button is "a" or "A" (using caps lock or shift), alert some text.

function myFunction() {
    const input =  document.getElementById("demo").value
    const x = input["CharacterData"];


    if( (x >= '97' && x <= '122') || (x >= '65' && x <= '90')){
        alert ("Keep typing!");
      }
    else input.replace(/[^a-zA-Z ]/g, ""){ 
        alert ("You pressed a 'not a letter key!");
      }

//event.code is not working. couldnt figure out how to restrict the value based on the keycode list
// also didnt work using Java Program to Check Alphabet using if else
// //In Java, the char variable stores the ASCII value of a character (number between 0 and 127) rather than the character itself.
// The ASCII value of lowercase alphabets are from 97 to 122. And, the ASCII value of uppercase alphabets are from 65 to 90. That is, alphabet a is stored as 97 and alphabet z is stored as 122. Similarly, alphabet A is stored as 65 and alphabet Z is stored as 90.
// Now, when we compare variable c between 'a' to 'z' and 'A' to 'Z', the variable is compared with the ASCII value of the alphabets 97 to 122 and 65 to 90 respectively.
// Since the ASCII value of * does not fall in between the ASCII value of alphabets. Hence, the program outputs * is not an alphabet.