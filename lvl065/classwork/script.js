// შექმენით ორი მასივი: languageA, languageB. სადაც 5-5 ელემენტს მოათავსებთ. თქვენი დავალებაა გამოიყენოთ forLoop-ი, რომ დაადგინოთ ამ ორ მასივს შორის არის თუ არა საერთო ელემენტები. თუ აღმოაჩენთ -
//  კონსოლში დალოგეთ 'found mutual language: {...}'


let languageA = ["english", "france", "spanish", "georgian"];
let languageB = ["english", "spanish"];
let sameLanguage = [];

for(i = 0; i < languageA.length; i++){
    for(j = 0; j < languageB.length; j++)
        if(languageA[i] === languageB[j]){
            sameLanguage.push(languageA[i])
        }
}
console.log(sameLanguage)

// -----------------------------------------------------

// 2) შექმენით fruits მასივი: ['apple', 'cherry', 'melon']
// დაწერეთ while loop-ის პროგრამა, math.random-ის საშუალებით currentFruit-ში ყოველ ჯერზე რენდომული მნიშვნელობა ჩაიწერება, სანამ 'cherry' მნიშვნელობა არ ჩაჯდება currentFruit-ში, იქამდე გააგრძელეთ ძებნა.

let fruits = ['apple', 'cherry', 'melon'];
let currentFruit;

while(currentFruit !== 'cherry'){
    currentFruit = fruits[Math.floor(Math.random() * 2)];
    console.log(currentFruit)
}