// 1) ახსენით რა არის ES6 და EcmaScript კომენტარების სახით
// ES6 -  არის javaScript - ის ერთ- ერთი განახლება რომელიც გამოვიდა 2015 წელს. ის არის js -  ის ყველაზე დიდი განახლება
// EcmaScript - არის js-ის განახლებები

// 2) შექმენი ცვლადი name რომელიც იქნება falsy - ს ტოლი და nickname 
// რომელსაც მნიშნველობა არ ექნება მინიჭებული, შემდეგ if - else - ის
//  გამოყენებით შეამოწმე, თუ name იქნება truthy, nickname გახდეს nameს ტოლი, სხვა შემთხვევაში "stranger"

let name = "";
let nichname;

if (name){
    name = nichname
} else{
    console.log("straingeer")
}


// 3) შექმენი ცვლადი day = 5; Switch - ის გამოყენებით:
// თუ day იქნება 1 - ის ტოლი --> Monday
// თუ day იქნება 2 - ის ტოლი --> Tuesday
// და ასე შემდეგ
let day = "day2";

switch (day){
    case "day1":
        console.log("Monday");
        break;
    case "day2":
        console.log("Tueasday")
}