print("are you willing to join goa?")
answer = input("yes or no: ")
while answer != "yes" and answer != "no":
    print("pick yes or no")
    answer = input("yes or no: ")
if answer == "no":
    print("have a great day")
else :
    print("joined")

choice = input ("Goa teaches both MMA and programming, which one will you pick: ")
while choice != "programming" and choice!= "MMA":
    print ("pick MMA or programming")
    choice= input ("MMA or programming: ")
if choice =="MMA":
    print ("you have joined MMA")
    print ("here you will learn wrestling,boxing and judo ")
    exit()
elif choice == "programming":
    print ("here you will learn web development, graphic design and game development")

print ("which one are you going to pick?")
print ("graphic design course")
print ("web development course")
print("or")
print ("game development course")

choice1= input()
if choice1== "web development course":
    print ("youve successfuly joined web development course")
elif choice1== "game development course":
    print ("youve successfuly joined game development course")
elif choice1== "graphic design course":
    print ("youve successfuly joined graphic design course")
print ("pick your plan")
print ("once a week for $100")
print ("twice a week for $200")
plan= input()
while plan != "once a week" and plan!= "twice a week":
    print("options are only once a week and twice a week")
    plan = input()
if plan == "once a week" :
    print("you will have lessons only on friday")
elif plan == "twice a week":
    print ("lessons on monday and friday")  