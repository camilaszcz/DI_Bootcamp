//Exercise 1

const people =['Greg', 'Mary', 'Devon', 'James'];
people.shift();
console.log(people);
// ['Mary', 'Devon', 'James']

people[2]='Jason';
// ['Mary', 'Devon', 'Jason']

people.push('Camila');
// ['Mary', 'Devon', 'Jason', 'Camila']

console.log(people.indexOf('Mary'));
//0

const newPeople  = people.slice(1,-1);
console.log('newPeople:', newPeople);
// ['Devon', 'Jason']

console.log(people.indexOf('Foo'));

const last = people[people.lenght -1];
console.log('last:', last);

console.log(people);

const people =['Greg', 'Mary', 'Devon', 'James'];
for (const friend of people) {
    console.log('This person is:', friend)
    if (friend === 'James') { break }
}

//Exercise2 + bonus

const colors = ['purple' , 'gold' , 'turquoise', 'emerald', 'fucsia']
const suffixes = ['st', 'nd', 'rd', 'th', 'th']
for (let i = 0;i<colors.lenght;i++){
    console.log(`My ${i+1}${suffixes[i]} choice is ${colors[i]}`)
}

//Exercise3

let number = null;
while(number != 10){
    const answer = prompt('Enter a number')
    number = Number{answer}
}

//Exercise4

