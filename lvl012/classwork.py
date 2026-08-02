number = int(input("write number: "))

if number < 0 :
    print("negative")
elif number > 0 :
    print("positive")
else :
    print("zero")



correct_password = "python123"

password = input("Enter password: ")

while password != correct_password:
    print("Wrong password, try again")
    password = input("Enter password: ")

if password == correct_password:
    print("Access granted")



fruits=["banana" , "apple" , "orange" , "mango" , "cherry"]

print=(fruits[1]) #meore wevri
print=(fruits[2]) # mesame wevri
print=(fruits[4]) #mexute wevri