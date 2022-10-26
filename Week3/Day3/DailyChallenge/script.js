// // Create an input type text that takes/shows only letters. (ie. numbers and special characters won’t be accepted)

// // Hint: use one of the following events to remove any character that is not a letter

// // keypress: It fires only when a key that produces a character value is pressed down. 
// // For example, if you press the key a, this event will fire as the key a produces a character value of 97. 
// //On the other hand, this event will not fire when you press the shift key as it doesn't produce a character value.

// let UserText = document.getElementById("input").addEventListener("keypress", myFunction);

//<input type="text" onkeypress='return event.charCode >= 48 && event.charCode <= 57'></input>

// function myFunction() {
//     const x = UserText.TextNode.char


//     if( (x >= '97' && x <= '122') || (x >= '65' && x <= '90')){
//       }
//     else{
//          (x.replace(/[^a-zA-Z ]/g, ""))
//       }
//     }
// //In Java, the char variable stores the ASCII value of a character (number between 0 and 127) rather than the character itself.
// The ASCII value of lowercase alphabets are from 97 to 122. And, the ASCII value of uppercase alphabets are from 65 to 90. That is, alphabet a is stored as 97 and alphabet z is stored as 122. Similarly, alphabet A is stored as 65 and alphabet Z is stored as 90.
// Now, when we compare variable c between 'a' to 'z' and 'A' to 'Z', the variable is compared with the ASCII value of the alphabets 97 to 122 and 65 to 90 respectively.
// Since the ASCII value of * does not fall in between the ASCII value of alphabets. Hence, the program outputs * is not an alphabet.

let inputtxt = document.getElementById("input")
let inputFunction= inputtxt.addEventListener("keypress", allLetter);

function allLetter()
  {
   const letters = /^[A-Za-z]+$/;
   if(inputtxt.value===letters)
     {
      return true;
     }
   else
     {
     inputtxt.value.replace("inputtxt", "x");
     alert ('Please input alphabet characters only');
     }
  }

  // is giving me the alert regardless of type and not replacing if it is not a letter.