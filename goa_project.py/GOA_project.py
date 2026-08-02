#start
print("Welcome looser! 😂🤣")
print("Wanna become CHAD?😎")
answer = input('Yes/No: ')
while answer != "Yes" and answer != "No":
    print("pick Yes or No")
    answer = (input("Yes or No: "))
if answer == "No" :
    print("Then Be a Looser!")
    exit()
else :
    print("Then join GOA!")

print("GOA Academy is the spot where you don’t just learn code 💻, you level up your chad vibes 🏋️‍♂️🥊.")
print('Coding + MMA + fitness = the ultimate combo to leave loosers behind and become a real boss 😎.')
print('If you wanna make your daily grind actually FUN, GOA’s where it’s at 💥.')

#first Choice
print("")
print("Are you willing to join GOA?")
answer = input("Yes or No: ")

while answer != "Yes" and answer != "No":
    print("pick Yes or No: ")
    answer = input("Yes or No: ")
if answer == "No":
    print("Then get lost!")
    exit()
else :
    print("Then register!")
    print("")

#register
email = (input("Write yout email: "))
password = (input("Write password : "))
password1 = (input("Repeat password : "))
while password1 != password :
    print("Password is incorrect ") 
    password1 = (input("Repeat password : "))

#second Choice
print('Successfully registered!')
print("")
choise = input("Goa teaches both: \n1-MMA  \n2-programming \nwhich one will you pick? (1 or 2):  ")
while choise != "1" and choise != "2" :
    print("Pick 1 or 2")
    choise = input("1 or 2 : ")
if choise == "1" :
    print("you have joined MMA course. ")
    print("Here you will learn wrestling,boxing and judo. ")
    print("")
    exit()
else :
    print("")
    print("Here you will learn:  \n1-Web development  \n2-Graphic design  \n3-Game development.")

#third choise
choise = input('Which one are you going to pick?(1 , 2 or 3): ')
while choise != "1" and choise !="2" and choise != "3" :
    print("Pick 1 , 2 or 3")
    choise = input('Which one are you going to pick?(1 , 2 or 3): ')
if choise == "2" :
    print("")
    print("Graphic design is the art of creating visual content to communicate ideas.")
    print("It uses images, colors, and text to make designs like logos, posters, and websites")
    exit()
elif choise == "3" :
    print("")
    print("Game development is the process of creating video games. It involves designing gameplay,")
    print("graphics, and code to build interactive and entertaining experiences.")
    exit()
else :
    print("")
    print("Here's all the info you need CHAD!😎")
    print("Web development is the process of creating websites and web applications.")
    print("It involves front-end development, which handles what users see and interact with using HTML, CSS,")
    print('and JavaScript, and back-end development, which manages servers, databases, and application logic.')
    print("Good web development ensures websites are fast, secure, user-friendly,accessible and functionality.")
    print("")

#fourth choise
print ("Information about courses: ")
print ("1-once a week (speed 1) - 195₾")
print ("2-twice a week (speed 2) - 295₾")
print ("3-Three times a week (speed 3) - 395₾")
plan = (input("Choose which one you prefer: "))
print("")
while plan != "1" and plan != "2" and plan != "3" :
    print("Pick 1 , 2 or 3")
    plan = (input("Choose which one you prefer: "))

if plan == "1":
#1-once a week (speed 1)
    print("Chose your Group:")
    print('1. Group 13 - Monday (18:00-20:00)')
    print('2. Group 23 - Thursday (17:00-19:00)')
    print('3. Group 65 - Saturday (15:00-17:00)')
    plan = (input("Chose your Group (1, 2 or 3): "))
    while plan != "1" and plan != "2" and plan != "3" :
        print("Pick 1 , 2 or 3")
        plan = (input("Chose your Group (1, 2 or 3): "))
    else:
        print("")
        print("Now you are CHAD!😎")
        print("Attened lesons on  Discord.")
#2-twice a week (speed 2)
elif plan == "2":
    print("Chose your Group:")
    print('1. Group 45 - Monday,Friday (14:00-16:00)')
    print('2. Group 78 - Thursday,Sunday (16:00-18:00)')
    print('3. Group 96 - Monday,Thursday (21:00-23:00)')
    plan = (input("Chose your Group (1, 2 or 3): "))
    while plan != "1" and plan != "2" and plan != "3" :
        print("Pick 1 , 2 or 3")
        plan = (input("Chose your Group (1, 2 or 3): "))
    else:
        print("")
        print("Now you are CHAD!😎")
        print("Attened lesons on  Discord.")
else:
    print("Chose your Group:")
    print('1. Group 1 - Monday,Wednesday,Friday (18:00-20:00)')
    print('2. Group 89 - Wednesday,Friday,Sunday (17:00-19:00)')
    print('3. Group 95 - Tuesday,Thursday,Saturday, (19:00-21:00)')
    plan = (input("Chose your Group (1, 2 or 3): "))
    while plan != "1" and plan != "2" and plan != "3" :
        print("Pick 1 , 2 or 3")
        plan = (input("Chose your Group (1, 2 or 3): "))
    else:
        print("")
        print("Now you are CHAD!😎")
        print("Attened lessons on  Discord.")
    










    