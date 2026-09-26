# 1) შექმენით Cat კლასი, რომელსაც ექნება ატრიუტები: Breed და Color. მას ასევე დაუმატეთ make_sound მეთოდი, 
# რომელიც გამოძახებისას დაბეჭდავს 'Meow'ს. შექმენით მინიმუმ ორი ინსტანცია და 
# ყველა ატრიბუტი/მეთოდი გამოიძახეთ ტერმინალში.

class Cat:
    def __init__(self, Breed, Color):
        self.Breed = Breed
        self.Color = Color

    def make_sound(self):
        print("mew")

cat1 = Cat("British", "Black")
cat2 = Cat("Scotish", "White")

print(f"Cat1 - Breed : {cat1.Breed} , color : {cat1.Color}")
print(f"Cat2 - Breed : {cat2.Breed} , color : {cat2.Color}")

# 2) შექმენით კლასი iphone, რომელსაც ექნება ატრიუტები: model, price და color.
#  მას ასევე დაუმატეთ pay მეთოდი, რომელიც გამოძახებისას დაბეჭდავს 
# 'Succesfully paid {price} dollars to buy {model}' price და მოდელის მაგივრად
#  ჩასვით ატრიბუტები საჭირო სინტაქსით. შექმენით მინიმუმ ორი ინსტანცია 
# და ყველა ატრიბუტი/მეთოდი გამოიძახეთ ტერმინალში.

class Iphone:
    def __init__(self, model, price, color):
        self.model = model
        self.price = price
        self.color = color

    def pay(self):
        print(f"Succesfully paid {self.price} dollars to buy {self.model}")

iphone1 = Iphone(17, 1700, "black")
print(iphone1.pay())
