# 1) მომხმარებელს შეაყვანინეთ ორი რიცხვი
# • და სცადეთ მათი გაყოფა
# • დაიჭირეთ:
# • ValueError
# • ZeroDivisionError
# თითოეული Exception-ის შემთხვევაში განსხვავებული შეტყობინება დაბეჭდეთ


try:
    num1 = float(input("enter first number"))
    num2 = float(input("enter second nuber"))
    result = num1 / num2
    print("RESULT : " + result)
except ValueError:
    print("error: invidal inpur")
except ZeroDivisionError:
    print("error : cannot devide bu zero")


# try: 
#     user_input = float(input("enter number"))
#     if user_input =
# except ValueError:
#     print("please enter numberonly")