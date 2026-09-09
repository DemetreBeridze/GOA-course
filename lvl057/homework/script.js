// 2)შექმენი ცვლადი ⁠userAge⁠ let-ის გამოყენებით, მიანიჭე რიცხვითი მნიშვნელობა, შემდეგ გაზარდე 
// ეს მონაცემი 1-ით ინკრემენტ ოპერატორით და გამოიტანე კონსოლში.

let age = 17
age ++
console.log(age)

// 3)შექმენი ორი ცვლადი: ⁠firstName⁠ და ⁠lastName⁠. გამოიყენე Template Literals და დაბეჭდე სრული წინადადება: 
// "გამარჯობა, ჩემი სახელია [firstName] [lastName]".

let firstName = "Demetre"
let lastName = "Beridze"

console.log(`Hello, my name is ${firstName} my lastname is ${lastName}`)


// 4)შექმენი ცვლადები ⁠currentYear⁠ და ⁠birthYear⁠. გამოითვალე ასაკი ამ ორ მონაცემს შორის სხვაობით,
//  შეინახე ახალ ცვლადში ⁠calculatedAge⁠ და დაბეჭდე შედეგი.

let currentYear = 2026;
let birthYear = 2009;
let calculateAge = currentYear - birthYear

console.log(calculateAge)


// 5)შექმენი სტრინგი ⁠text = "     learning javascript         "⁠ გამოიყენე შესაბამისი მეთოდი გარე 
// სივრცეების მოსაცილებლად , გადაიყვანე ტექსტი დიდ ასოებში და გამოიტანე მისი საბოლოო სახე.

let text = "     learning javascript         "
console.log(text.trim().toLowerCase())


// 6)შექმენი ცვლადი ⁠score = 50⁠. შემოკლებული მათემატიკური ოპერატორების (⁠+=⁠, ⁠*=⁠, ⁠-=⁠)
//  გამოყენებით ცვლადს დაუმატე 25, გაამრავლე 2-ზე, გამოაკელი 10 და ბოლოს გამოიტანე მიღებული ⁠score⁠.

let core = 50;
core +=25;
core *= 2;
core -= 10;

let score = core 
console.log(score)



// 7)შექმენი ცვლადი ⁠itemPrice = 19.99⁠ და შეამოწმე მისი ტიპი ⁠typeof⁠ ოპერატორით.
// დაბეჭდე კონსოლში ტექსტი: "itemPrice-ის ტიპია: [ტიპი]".

let itemPricw = 19.99;
console.log(`itemPrice ის ტიპია ${typeof itemPricw}`)


// 8)გამოიყენე ⁠Math.random()⁠ და ⁠Math.floor()⁠ მეთოდები, რათა დააგენერირო შემთხვევითი 
// მთელი რიცხვი 1-დან 10-მდე, შეინახო ცვლადში ⁠randomNumber⁠ და დაბეჭდო.

console.log(Math.floor(Math.random() * 10))


// 9)შექმენი ცვლადი ⁠city⁠ მნიშვნელობის მინიჭების გარეშე . შემდეგ შექმენი ცვლადი ⁠emptyValue⁠ და მიანიჭე ⁠null⁠.
//   დაბეჭდე ორივე მათგანი და გაიგე მათი ტიპები ⁠typeof⁠-ით.

let city;
let emptyValue = null;
console.log(typeof city);
console.log(typeof emptyValue)


// 10) შექმენი ცვლადი ⁠favoriteColor⁠ const-ის გამოყენებით, მიანიჭე საყვარელი ფერი სტრინგის სახით და 
// დაბეჭდე კონსოლში მისი სიგრძე ⁠.length⁠ თვისებით

let favColor = "blue"
console.log(favColor.length)



// 11)შექმენი ათწილადი ⁠pi = 3.14159⁠. გამოიყენე ⁠Math.round()⁠ და ⁠Math.floor()⁠ მეთოდები და
//  დაბეჭდე ორივე შედეგი ცალ-ცალკე, რომ გამოჩნდეს განსხვავება დამრგვალების პრინციპებს შორის.

let pi = 3.14;
console.log(Math.floor(pi))
console.log(Math.ceil(pi))


// 12)შექმენი ცვლადი ⁠testNumber = 42.5⁠ და ⁠Number.isInteger()⁠ მეთოდით შეამოწმე, არის თუ არა 
// ეს მონაცემი მთელი რიცხვი. დაბეჭდე მიღებული ლოგიკური მნიშვნელობა (Boolean) კონსოლში.

let Number = 42.5;
console.log(Number.isInteger)
