// Retrieve the form and console.log it.

    const.myForm = document.forms[0];
    console.log(myForm);
//     Retrieve the inputs by their id and console.log them.

    const myForm = document.forms[0].fname;
    console.log(myForm);
//     Retrieve the inputs by their name attribute and console.log them.

    const myForm = document.forms[0].elements.fname;
    console.log(myForm);

    
//     When the user submits the form (ie. submit event listener)
//     use event.preventDefault(), why ?
//     get the values of the input tags,
//     make sure that they are not empty,
//     create an li per input value,
//     then append them to a the <ul class="usersAnswer"></ul>, below the form.
//     The output should be :
    
//     <ul class="usersAnswer">
//         <li>first name of the user</li>
//         <li>last name of the user</li>
//     </ul>
    