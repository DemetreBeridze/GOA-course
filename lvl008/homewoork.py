## > - metia
# < - naklebia
# >= - metian an toli
# <= - naklebia an toli
# == - mkacrad tolia
# != - artolia

print(5 > 10)
print(19 > 17)

print(14 < 13)
print(16 < 18)

print(16 <= 16)
print(34 <= 89)

print(54 >= 54)
print(32 >= 78)

print(34 == "34")
print(77 == 77)

print(34 != "34")
print(77 != 77)




# 5) დეტალურად ახსენით თუ რატომ გამოიტანს მოცემული კოდი False-ს ტერმინალში:

# num1 = "21"
# num2 = 21
# print(num1 == num2)

# radgan "==" amowmebs rogorc monacems aseve monacemis tips. radgan 21 aris int xolo "21" atis string tiis isini ertmanetis toli ver iqneba.


# 6) ცვლადში შეინახეთ თქვენი გვარი, შემდეგ კი მომხმარებელს
#  შემოატანინეთ მისი გვარი. დაადგინეთ თქვენი და მომხმარებლის გვარები ემთხვევა თუ არა ერთმანეთს.

my_surname = "Beridze"
users_surname = input("enter yout surname: ")
print(my_surname == users_surname)




# 7) რას გამოიტანს მოცემული კოდები?

# • False or True and True and False

# • True and False or False or True

# • True or True and False or True or False and True or False

print(False or True and True and False)
#       false or  true  and false - ghamoitans Falce


print(True and False or False or True)
#         falce or false or true- gamoitans True


print(True or True and False or True or False and True or False)
#         true or   falce      or true or falce    falce or falce- gamoitans True



# 8) დაწერეთ სახლის გაგრილების სისტემის პროგრამა.
# ვთქვათ, როდესაც სახლში ტემპერატურა 30 გრადუსს ასცდება - ავტომატურად უნდა ჩაირთოს გაგრილების სისტემა.
#  იმის გასაგებად თუ რა ტემპერატურაა სახლში, მომხმარებელს იგი შემოატანინეთ input() ფუნქციის მეშვეობით.
#  (გამოიყენეთ მხოლოდ ლოგიკური ოპერატორები)

temperature = float(input("შეიყვანეთ არსებული ტემპერატურა სახლში: "))
cooling_system = temperature > 30
print(cooling_system)









# HARD LVL:
# 9) დაწერეთ ოთახის გაგრილების სისტემის პროგრამა, but there’s a twist:

# ჩათვალეთ, რომ პროგრამა მხოლოდ იმ შემთხვევაში აღიქვამს ოთახის ტემპერატურას, თუ იგი 
# ფარენგეიტშია გადმოცემული. (სისტემა ჩაირთვება მაშინ, როდესაც ტემპერატურა 89.6 ფარენგეიტს ასცდება). 
# ერთადერთი გასათვალისწინებელი ფაქტი ის არის, რომ მომხმარებელს ოთახის ტემპერატურა გრადუსებში შემოაქვს. 

# ეცადეთ დაწეროთ პირობის მიხედვით ისეთი ოთახის გაგრილების სისტემის პროგრამა, რომელიც სწორად იმუშავებს 

temperature1 = float(input("შეიყვანეთ არსებული ტემპერატურა სახლში: "))
cooling_system1 = temperature *1.8 + 30  > 89.6
print(cooling_system1)










