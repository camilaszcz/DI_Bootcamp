//Exercise1

const fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
fruits.shift(); 
fruits.sort();
fruits.push("Kiwi");
fruits.splice(0,1);
fruits.reverse();
//result (3) ['Kiwi', 'Oranges', 'Blueberries']

//Exercise2

const moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(moreFruits[1]);//result (3) ['Apples', Array(1), 'Blueberries']
console.log(moreFruits[1][1]);//result ['Oranges']

