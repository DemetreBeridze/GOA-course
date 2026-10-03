# 1) შექმენით Person კლასი (name, age).
# შემდეგ შექმენით Student კლასი, რომელიც ამატებს grade-ს და super()-ით ინიციალიზაციას აკეთებს.
    

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

student1 = Student("Demetre", 17, "A")
print(student1.name)
print(student1.age)
print(student1.grade)


# 2) შექმენით Shape კლასი area() მეთოდით რომელიც დააბრუნებს საწყისად 0-ს (return 0).
# შემდეგ შექმენით Rectangle კლასი (width, height), რომელიც super()-ს გამოიყენებს და მოახდენს 
# area() მეთოდის override-ს.

class Shape:
    def __init__(self):
        pass

    def Area(self):
        return 0

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def Area(self):
        return self.width * self.height

shape = Rectangle(5,10)
print(shape.Area())
