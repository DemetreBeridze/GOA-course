// 2) შექმენი მასივი fruits რამდენიმე ხილის დასახელებით. დაბეჭდე კონსოლში ტექსტი: "მასივში არის X ელემენტი", 
// სადაც X არის მასივის სიგრძე.

let fruits = ["apple", "pineapple", "mango"];
console.log(`masivshi aris ${fruits.length} elemnti`);

// 3) შექმენი ცარიელი მასივი todoList. .push() მეთოდის გამოყენებით თანმიმდევრობით დაამატე 3 აქტივობა
// (მაგ. "learn", "workout", "rest"). დაბეჭდე საბოლოო მასივი.

let todoList =[];
todoList.push("learn", "workout", "rest")
console.log(todoList)

// 4) გაქვს მასივი numbers = [10, 20, 30, 40, 50]. წაშალე მასივიდან ბოლო ელემენტი
//  .pop()-ით, ხოლო წაშლილი მნიშვნელობა შეინახე ცალკე ცვლადში removedNumber და დაბეჭდე კონსოლში.

let numbers = [10, 20, 30, 40, 50];
let removeNum = numbers.pop();
console.log(numbers);
console.log(removeNum);


// 5) შექმენი მასივი colors = ["წითელი", "მწვანე", "ლურჯი", "ყვითელი", "იასამნისფერი"]. .at()
//  მეთოდის გამოყენებით დაბეჭდე:
// პირველი ელემენტი და ბოლო ელემენტი 

let colors = ["წითელი", "მწვანე", "ლურჯი", "ყვითელი", "იასამნისფერი"];
console.log(colors.at(0,));
console.log(colors.at(4));
console.log(colors(colors.length - 1));

// 6) გაქვს რიგის მასივი queue = ["გიორგი", "ანა", "ნიკა", "მარიამი"]. რადგან პირველი მომხმარებელი მოემსახურა,
//  ამოიღე ის მასივიდან .shift()-ით და დაბეჭდე განახლებული რიგი.

let queue = ["გიორგი", "ანა", "ნიკა", "მარიამი"];
queue.shift();
console.log(queue);

// 7) შექმენი ორი მასივი: frontEnd = ["HTML", "CSS", "JS"] და 
// backEnd = ["Node.js", "Python"]. შეაერთე ეს ორი მასივი .concat()-ის გამოყენებით ახალ fullStack
//  მასივში და დაბეჭდე.

let frontEnd = ["HTML", "CSS", "JS"];
let backEnd = ["Node.js", "Python"];
console.log(`${frontEnd}`.concat(backEnd))

// 8) გაქვს მასივი animals = ["Dog", "Cat", "Bear", "Wolf"].
// იპოვე და დაბეჭდე "Cat"-ის ინდექსი .indexOf()-ის საშუალებით.
// შეამოწმე, რას დააბრუნებს .indexOf("lion") და ახსენი რატომ მივიღეთ მსგავსი შედეგი.

let animals = ["Dog", "Cat", "Bear", "Wolf"];
console.log(animals.indexOf("Cat"))

// 9) გაქვს კვირის დღეების მასივი 
// days = ["ორშაბათი", "სამშაბათი", "ოთხშაბათი", "ხუთშაბათი", "პარასკევი", "შაბათი", "კვირა"].
//  .slice()-ის გამოყენებით ამოჭერი მხოლოდ სამუშაო დღეები (ორშაბათიდან პარასკევის ჩათვლით) 
// ახალ მასივში workDays.

let days = ["ორშაბათი", "სამშაბათი", "ოთხშაბათი", "ხუთშაბათი", "პარასკევი", "შაბათი", "კვირა"];
let workDays = days.slice(5, 7);
console.log(workDays)

// 10) შექმენი მასივი randomMovies = ["Inception", "Interstellar"]. 
// .unshift() მეთოდით სიის საწყისში (პირველ ადგილას) დაამატე ფილმი "The Dark Knight".

let randomMovies = ["Inception", "Interstellar"];
randomMovies.unshift("the dark knight");
console.log(randomMovies)

// 11) გაქვს მასივი scores = [50, 65, 78, 92, 45, 88, 99].
//  .slice() მეთოდის გამოყენებით ამოჭერი და ცალკე მასივში შეინახე ბოლო 3 ქულა.

let scores = [50, 65, 78, 92, 45, 88, 99];
let scores2 = scores.slice(5,7);
console.log(scores2)

// 12) შექმენი ცარიელი მასივი searchHistory.
// 1. დაამატე მასში 3 ლინკი .push()-ით: "google.com", "github.com", "youtube.com".
// 2. წაშალე ბოლო ეწვიეული საიტი .pop()-ით.
// 3. დაამატე ახალი საიტი "stackoverflow.com".
// 4. დაბეჭდე მასივის მიმდინარე სიგრძე (.length) და ბოლო ელემენტი (.at(-1)).

let searchHistory=[];
searchHistory.push("google.com", "github.com", "youtube.com");
searchHistory.pop();
searchHistory.push("stackoverflow.com");
console.log(searchHistory);
console.log(searchHistory.length);
console.log(searchHistory.slice(searchHistory.length - 1));

// 13) შექმენი მასივი shoppingList = ["bread", "milk", "cheese", "eg"].
// .indexOf()-ით იპოვე "cheese"-ის ინდექსი.

let shoppingList = ["bread", "milk", "cheese", "eg"];
console.log(shoppingList.indexOf("cheese"))

// 14) არ დაგეზაროთ და აუცილებლად უყურეთ თავიდან ჩანაწერს.