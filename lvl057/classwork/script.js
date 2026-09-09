// 1) შექმენით ორი სხვადასხვა ცვლადი let-ის გამოყენებით: word1, word2.
// ორივეში შეინახეთ სხვადასხვა სტრინგი და გამოიტანეთ კონსოლში. გამოიყენეთ შესაბამისი მეთოდები,
//  რომ გადაიყვანოთ პირველი სტრინგი დიდ ასოებად, ხოლო მეორე პატარა ასოებად და შეინახეთ ისინი
//  ახალ ცვლადებში (შემდეგ ისევ გამოიტანეთ კონსოლში).

let word1 = "HeLlow"
let word2 = "WorLd"
console.log(word1.toUpperCase())
console.log(word2.toLowerCase())


// 2) გამოიყენეთ დღეს ნასწავლი მეთოდი, რომ ამ სტრინგს მოაშოროთ ცარიელი სფეისები:
// const variable = '     Group 71      '
const variable = '     Group 71      '
console.log(variable.trim())

// 3) კომენტარის სახით ახსენით რას აკეთებს - Math.random() და Math.floor()
// Math.random() - 0dan 1mde random ricxvs gamoitans terminals
// Math.floor() - nebismier ricxv, wilads daamgvalebs dablisken (2.59764 ~ 2 )



// 4) დააგენერირეთ რენდომ რიცხვი 0-დან 96-მდე და გამოიტანეთ კონსოლში. ეს რიცხვი აუცილებლად უნდა იყოს მთელი.
console.log(Math.floor(Math.random() * 96))