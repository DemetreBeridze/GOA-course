# 2) შექმენით კლასი Person, რომელსაც ექნება თვისებები name და age. შექმენით მეთოდი introduce(), 
# რომელიც დაბეჭდავს:
#  "Hello, my name is {name} and I am {age} years old"

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")

person1 = Person("Giorgi", 25)
person1.introduce()

# 3) შექმენით კლასი Rectangle, რომელსაც ექნება თვისებები width და height.  
# ასევე შექმენით მეთოდები area() და perimeter() რომლებიც გამოითვლის მართკუთხედის პერიმეტრსა და ფართობს.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print(self.width * self.height)

    def perimeter(self):
        print(2 * (self.width + self.height))

rect1 = Rectangle(5, 10)
rect1.area()
rect1.perimeter()

# 4) შექმენით კლასი Product და დაამატეთ თვისებები price და quantity. დაამატეთ მეთოდი:
# total_value() → price × quantity

# ასევე კლასის გამოყენებით შექმენით პროდუქტების სია და:
# • იპოვეთ ყველაზე ძვირი პროდუქტი
# • იპოვეთ ყველაზე იაფი პროდუქტი



# 5) შექმენით Dog კლასი, რომელსაც ექნება ატრიუტები: Breed, age და Color. 
# მას დაუმატეთ make_sound მეთოდი, რომელიც გამოძახებისას დაბეჭდავს შესაბამის ხმას. 
# ასევე დაუმატეთ bark() მეთოდი, რომელიც გამოიტანს: '{age} years old {breed} is barking'.
#  შექმენით მინიმუმ ორი ინსტანცია და ყველა ატრიბუტი/მეთოდი გამოიძახეთ ტერმინალში.

class Dog:
    def __init__(self, breed, age, color):
        self.breed = breed
        self.age = age
        self.color = color

    def make_sound(self):
        print("Woof woof")

    def bark(self):
        print(f"{self.age} years old {self.breed} is barking")

dog1 = Dog("Labrador", 3, "black")
dog2 = Dog("Golden Retriever", 5, "yellow")

print(dog1.breed)
print(dog1.age)
print(dog1.color)
dog1.make_sound()
dog1.bark()

print(dog2.breed)
print(dog2.age)
print(dog2.color)
dog2.make_sound()
dog2.bark()