// 1) შექმენით კონსტანტა სადაც შეინახავთ 10 - 100 ჩათვლით რიცხვს, თქვენი დავალებაა,
//  რომ შეამოწმოთ მოსწავლის ქულა და შესაბამისად გამოიტანოთ შეფასება, მაგალითად, 
// თუ მოსწავლის ქულა მეტია ან ტოლი 90 მაშინ გამოიტანეთ მნიშვნელობა 'A' 

const point1 = 66 ;

if (90  < point1 && point1 < 100){
    console.log("A+")
} else if (80 < point1 && point1 < 90){
    console.log("A")
} else if (70 < point1 && point1 < 80){
    console.log("B+")
} else if (60 < point1 && point1 < 70){
    console.log("B")
} else {
    console.log("you failed!!!")
}



// 2) მეორე დავალების გაკეთება სცადეთ ამჯერად switch - ის გამოყენებით, მოიძიეთ
//  ინფორმაცია და კომენტარების სახით ახსენით მისი დანიშნულება

let point = 88;

switch (true){
    case (90  < point && point < 100):
        console.log("A+")
        break;
    case (80  < point && point < 90):
        console.log("A")
        break;
    case (70  < point && point < 80):
        console.log("B+")
        break;
    case (60  < point && point < 70):
        console.log("B")
        break;
    default:
        console.log("you failed")
}

// 3) შექმენით ორი კონსტანტა სადაც შეინახავთ სახელს და ასაკს, თქვენი დავალებაა, რომ შეამოწმოთ
//  უდრის თუ არა მომხმარებლის სახელი თქვენს სახელს და უდრის თუ არა მომხმარებლის ასაკი თქვენს ასაკს,
//  თუ მოცემული პირობა არის true, გამოიტანეთ ტექსტი 'We have the same name or age' სხვა შემთხვევაში
//  კი გამოიტანეთ ტექსტი "We don't have the same name and age", ამისათვის გამოიყენეთ logical operator 

const name = "Demetre";
const age = 17;

const userNmae = "Giorgi";
const userAge = 16;

if (name === userNmae && age === userAge){
    console.log("we have same ag eand also same name")
} else {
    console.log("we dont have same age and same name")
}


// 4) შექმენით ორი კონსტანტა, პირველი age რომელშიც შეინახავთ ასაკს, მეორე hasTicket -
//  რომელშიც შეინახავთ boolean მნიშვნელობას, თქვენი დავალებაა, რომ შეამოწმოთ იმ შემთხვევაში
//  თუ მომხმარებლის ასაკი მეტია 15 - ზე და hasTicket - ის მნიშვნელობა არის true,
//  მაშინ გამოიტანეთ ტექსტი 'You can go in, and watch a movie' სხვა შემთხვევაში "You can't go in",
//  გამოიყენეთ logical, comparation operator - ები

const age1 = 17;
const hasTicket = true;

if (age1 > 15 && hasTicket){
    console.log("you can enter and watch movie")
}


// 5) შექმენით კონსტანტა temperature სადაც შეინახავთ ტემპერატურას, თქვენი დავალებაა ternary operator-ის
//  გამოყენებით შეამოწმოთ თუ ტემპერატურა მეტია ან ტოლია 20 - ის მაშინ გამოიტანოთ 'It is warm',
//  სხვა შემთხვევაში კი გამოიტანეთ 'It is cold'

const temperature = 25;

if (temperature >= 20){
    console.log("its hot here")
}
