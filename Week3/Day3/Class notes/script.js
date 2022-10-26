//const SaleBanner = document.getElementsByClassName('banner')

// function sayHi(){
// display(SaleBanner)
// }

//this:
//setTimeout(makeBannerAppear, 5000);
//or this:

//function makeBannerAppear(() => {
// //SaleBanner.style.visibility = 'visible';
// // ------------------------
// // make the banner appear
// function startOne () {
//     setTimeout(makeBannerAppear, 10000);
// }

// //it will be called after 3 seconds
// function makeBannerAppear (){
//     //retrieve the div
//     const div = document.getElementById("hello"); //retrieve the div from the DOM
//     div.style.display = "block"; //change the style
// }

// startOne() //called when the page is executed


// // -----------------------------
// //add the banner to the page
// function start (){
//     setTimeout(createBanner, 3000);
// }

// function createBanner (){
//     const div = document.createElement("div");
//     div.textContent = "hello";
//     div.classList.add("banner");
//     document.body.appendChild(div);
// }

// start()

// Use the same code as before but create a countdown in the banner.

// ... "The sales end in 10sec ! "

// ... "The sales end in 9sec ! "


// function start (){
//     setTimeout(createBanner, 3000);
// }

// function createBanner (){
//     const div = document.createElement("div");
//     div.textContent = "hello";
//     div.classList.add("banner");
//     document.body.appendChild(div);
// }

// start()


// const countdown = document.getElementById('number');
// const counter = 10;
// const timer = setInterval(decreaseCounter, 1000);

// function decreaseCounter(){
//     if(counter >=0){
//         countdown.TextContent = counter;
//         counter--;
//     } else{ 
//         clearInterval(timer);
//         return;
//     }
// }
// <p> The download will begin in <span id="countdowntimer">10 </span> Seconds</p>

    var timeleft = 10;
    var downloadTimer = setInterval(function(){
    timeleft--;
    document.getElementById("number").textContent = timeleft;
    if(timeleft <= 0)
        clearInterval(downloadTimer);
    },1000);