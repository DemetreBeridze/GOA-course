# 2) რას ეწოდება Tuple unpacking? მოიყვანეთ მინიმუმ 3 მაგალითი 
# (Asterisk ოპერატორის გამოყენებით და გამოყენების გარეშეც)
# Tuple unpacking - ewodeba toouplebis dashlas cvladebad

touple = (11 , 9 , 10)
neymar , suarez , messi = touple
print(neymar)
# -----------
touple_2=(1, 2, 3, 4, 5, 6)
num1 , num2, *num3 =touple_2
print(num3)
# ---------------
# 3) კომენტარის სახით ჩამოწერეთ რომელი მეთოდების/ფუნქციების გამოყენებაა შესაძლებელი Tuple-ებზე.
# 1 - count
# 2 - max() , min()
# 3 - control flow
# 4 - unpacking
# 5 - asteriks

# 4) კომენტარის სახით ჩამოწერეთ რომელი მეთოდების/ფუნქციების გამოყენება არ არის ხელმისაწვდომი Tuple-ებზე.
# yvela im operatos gamoyeneba romelic Touplpebis shecvlas moitxovs. (mag: .append , .indexsingit shecvla ...)


# 5) შექმენით Tuple სახელწოდებით info, სადაც შეინახავთ თქვენს მონაცემებს (სახელი, ასაკი, მისამართი ა.შ).
#  მასში შეინახეთ 4 მონაცემი და მოახდინეთ თაფლის unpacking: თითოეულ მონაცემს შესაბამისი ცვლადის სახელი 
# შეისაბამეთ (name, age, etc..)
info = ("Demetre" , "Beridze" , 16 , "Tbilisi" )
name , lastname , age , city = info
print(name)

# 6) შექმენით Tuple, რომელშიც შეინახავთ მთელ და წილად რიცხვებს. Tuple_ის პირველ ელემენტს 
# დაარქვით num1, დანარჩენი ელემენტები კი rest ცვლადში შეინახეთ Asterisk ოპერატორის გამოყენებით.
touple_3 = (3 , 3.22 , 1.11 , 7.345)
num_1 , *rest = touple_3
print(rest)

# 7) დაწერეთ თქვენი ვარაუდი: რას გამოიტანს ეს კოდი?
fruits = ('Apple', 'Pomegranate', 'Cherry', 'Strawberry', 'Blueberry')
*fruit1, fruit2, fruit3 = fruits 
# errors




