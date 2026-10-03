# 2) ახსენით თუ რას ნიშნავს Class Inheritence.

# 3)  შექმენით Employee კლასი (name, salary).
# შემდეგ შექმენით Manager კლასი, რომელიც მშობელ კლასს დაუმატებს department კუთვნილებას და super()-ით იღებს დანარჩენ კუთვნილებებს.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Mnager(Employee):
    def __init__(self, name, salary, departament):
        super().__init__(name, salary)
        self.departament = departament




# 4) შექმენი User კლასი (username, email).
# შექმენი Admin კლასი, რომელიც ამატებს role-ს და super()-ით იძახებს მშობლის კონსტრუქტორს.

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class Admin(User):
    def __init__(self, username, email, role):
        super().__init__(username, email)
        self.role = role

# 5) შექმენი Book კლასი (title, author).
# შემდეგ EBook კლასი (file_size), რომელიც super()-ით იძახებს მშობლის კონსტრუქტორს და ამატებს ნებისმიერ ახალ ატრიბუტს.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Ebook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

# 6) შექმენით მშობელი კლასი Vehicle. მიეცით მას თვისებები: brand, year, color, horsePower. მშობელ კლასში დაამატეთ drive() მეთოდი, რომელიც დაბეჭდავს '{color} {brand} is going'. ასევე შექმენით stop() მეთოდი, რომელიც დაბეჭდავს '{color} {brand} is stopping'. 



class Vehicle:
    def __init__(self, brand, year, color, horse_power):
        self.brand = brand
        self.year = year
        self.color = color
        self.horse_power = horse_power


    def drive(self):
        return f"{self.color} {self.brand} is going"

    def stop(self):
        return f'{self.color} {self.brand} is stopping'

vehicle = Vehicle("TESLA", 2023, "white", "250")

print(vehicle.brand);
print(vehicle.stop());
print(vehicle.stop)

class Car(Vehicle):
    def __init__(self, brand, year, color, horse_power, car, bike):
        super().__init__(brand, year, color, horse_power)
        self.car = car
        self.bike = bike