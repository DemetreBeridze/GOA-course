// 1) დაწერეთ for loop-ი, რომელიც 10-დან 1-ის ჩათვლით დაითვლის რიცხვებს.

for(let i = 10 ; i>=1; i--){
    console.log(i)
}

// 2) დაწერეთ for loop-ი, რომელიც გადაუვლის თქვენი საყვარელი 
// ფილმების მასივს და გამოიტანს მის თითოეულ ელემენტს. (მასივში მინიმუმ 5 ელემენტი უნდა ინახებოდეს.)

const favMovies = ["Southpow", "Se7en", "Showshank redemption", "Endgame"]

for(let x=0; x<=favMovies.length; x++){
    console.log(favMovies[x])
}