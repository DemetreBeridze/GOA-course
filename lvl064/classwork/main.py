# Multi-level inheritance

# შექმენით კლასი Gadgets, რომელსაც ეყოლება შვილი კლასი Phone-ი. 
# აიღეთ Phone კლასი, დაუმატეთ რამდენიმე თვისება და ერთი მეთოდი, რომელიც გამოიტანს: 'Calling'-ს.
#  და მშობელ კლასად გადაეცით Ios და Android კლასებს
class Gadgets:
    def __init__(self, brand , year):
        self.brand = brand
        self.year = year

        def gadget_info(self):
            return f"brand: {self.brand}, year: {self.year}"


class Phone(Gadgets):
    def __init__(self, brand , year, model):
        super().__init__(brand, year)
        self.model = model

        def calling(self):
            return "Calling..."

class Ios(Phone):
    def __init__(self, brand, year, model, ios_version):
        super().__init__(brand, year, model)
        self.ios_version = ios_version

class Android(Phone):
    def __init__(self, brand, year, model, android_version):
        super().__init__(brand, year, model)
        self.android_version = android_version

iphone= Ios(brand="iphone",year=2025,model="iphone 17", ios_version=17)
print(iphone.brand)
print(iphone.model)
print(iphone.year)
print(iphone.ios_version)

# Multiple Level Inheritence

# შექმენით კლასი VacuumCleaner, რომელსაც ექნება Vacuum მეთოდი.
# ასევე, შექმენით Robot კლასი, რომელსაც ექნება DetectObstacle მეთოდი.

# საბოლოოდ, შექმენით RobotVacuum კლასი, რომელიც მიიღებს VacuumCleaner და Robot -ის მეთოდებს მემკვიდრეობით.

# class VacuumCleaner:
#     def __init__(self):
#         pass

#     def Vacuum(self):
#         return "cleaning"

# class Robbot:
#     def __init__(self):
#         pass