# 2) შექმენით ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და
#  აბრუნებს ამ რიცხვების საშუალო მნიშვნელობას.


# def Arithmetic_mean() :
#     return sum(numbers) / len(numbers)

# numbers = [1, 2, 3 ,4 , 5, 6, 7, 8, 9, ]
# print(Arithmetic_mean())



#3)  შექმენით ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და
#  აბრუნებს ამ სიაში ლუწი რიცხვების რაოდენობას.


# def odd_numbers(number) :
#     count = 0
#     for num in numbers :
#         if num % 2 == 0 :
#             count += 1
#     return count

# numbers = [1, 2, 3 ,4 , 5, 6, 7, 8, 9, ]
# print(odd_numbers(numbers))


#4) შექმენით ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას
#  და აბრუნებს ამ სიაში კენტი რიცხვების რაოდენობას.

# def even_numbers(number) :
#     count = 0
#     for i in numbers :
#         if i % 2 != 0 :
#             count += 1
#     return count

# numbers = [1, 2, 3 ,4 , 5, 6, 7, 8, 9, ]
# print(even_numbers(numbers))



#5)  შექმენით ფუნქცია სახელწოდებით double_values რომელიც არგუმენტად მიიღებს სიას და
#  დააბრუნებს ახალ სიას, სადაც თითოეული ელემენტი გაორმაგებული იქნება.

# def double_values(number) :
#     result = []
#     for i in numbers :
#         result.append(i * 2)
#     return result

# numbers = [1, 2, 3 ,4 , 5, 6, 7, 8, 9, ]
# print(double_values(numbers))


#6) შექმენით ფუნქცია და გადაეცით არგუმენტად სია. ფუნქციამ უნდა დააბრუნოს ახალი სია, 
# რომლის თითოეული ელემენტიც უნდა იყოს კვადრატში აყვანილი.

# def double_values(number) :
#     result = []
#     for i in numbers :
#         result.append(i * i)
#     return result

# numbers = [1, 2, 3 ,4 , 5, 6, 7, 8, 9,]
# print(double_values(numbers))



#7) შექმენით ფუნქცია სახელწოდებით sum, რომელსაც არგუმენტად გადაეცემა 3 რიცხვი და ფუნქციის 
# მიზანი იქნება, რომ ამ სამი რიცხვის ჯამი დააბრუნოს.


# def sum(x, y, z) :
#     return x + y + z
# print(sum(13 , 7 , 4))


#8) შექმენით ფუნქცია სახელწოდებით substract, რომელსაც არგუმენტად ორ რიცხვს. ფუნქციამ 
# პასუხად უნდა დააბრუნოს ამ რიცხვების სხვაობა.

# def substract (a ,b ,) :
#     return a - b
# print(substract(12 , 7))



#9)  შექმენით ფუნქცია სახელწოდებით multiply, რომელსაც არგუმენტად ორ რიცხვს. ფუნქციამ პასუხად
#  უნდა დააბრუნოს ამ რიცხვების ნამრავლი.


# def multiply (a ,b ,) :
#     return a * b
# print(multiply(12 , 7))

# 10)  შექმენით ფუნქცია check_age, რომელიც არგუმენტად მიიღებს მომხმარებლის ასაკს.
# თუ მომხმარებლის ასაკი მეტი ან ტოლი იქნება 18-ზე, ტერმინალში დაიბეჭდოს "Access Granted",
#  წინააღმდეგ შემთხვევაში – "Access Denied".


# def check_age (age) :
#     if age >= 18 :
#         print("access granted")
#     else :
#         print("Access Denied")

# print(check_age(int(input("enter your age: "))))




#15) შექმენით ფუნქცია - Arithmetic_mean, რომელიც პარამეტრად მიიღებს სიას. ფუნქციამ სიაში არსებული
#  ელემენტების საშუალო არითმეტიკული უნდა დააბრუნოს. (ფუნქცია გათვლილი უნდა იყოს ნებისმიერი
#  რაოდენობის შემცველ სიაზე)


# def Arithmetic_mean (numbers) :
#     if len(numbers) == 0 :
#         print("unable")
#     return sum(numbers) / len(numbers)

# number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(Arithmetic_mean(number))



#17)  შექმენით ფუნქცია, რომელიც პარამეტრად მიიღებს სიას და დააბრუნებს ახალ სიას, სადაც მხოლოდ უნიკალური 
# ელემენტები იქნება — ანუ თქვენი დავალებაა სია გაფილტროთ duplicate ელემენტებისგან.


# def non_duplicate (numbers) :
#     list = []
#     for i in numbers :
#         if i not in list :
#             list.append(i)
#     return list

# numbers = [ 1, 1 ,2 , 3,3, 44 ,44, 56, 55, 55 ]
# print(non_duplicate(numbers))








# 18) შექმენით manual sum ფუნქცია Python-ში. (manual ნიშნავს გარკვეული ფუნქციის/მეთოდის საკუთარი ხელით შექმნას.)
# ეს ფუნქცია უნდა მუშაობდეს სიებზე, კონკრეტულად: მან უნდა დააბრუნოს სიის ყველა ელემენტის ჯამი.


# def sum (numbers) :
#     total = 0
#     for i  in numbers :
#         total += i
#     return total

# number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(sum(number))



