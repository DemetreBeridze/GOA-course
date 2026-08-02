# 3) დაწერეთ პროგრამა, რომელიც ამოწმებს input-ით შემოყვანილი რიცხვი ლუწია თუ კენტი.
# 4) დაწერეთ პროგრამა, რომელიც ამოწმებს ტემპერატურას:
# თუ > 30 -> "It's Hot"
# თუ 15-30 -> "It's Warm"
# თუ < 15 -> "It's Cold"
# 5) მოხმარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ:
# • "Positive even" dadebiti luwi
# • "Positive odd" dadebiti kenti
# • "Negative" uaryofiti
# 6) დაწერეთ პროგრამა რომელიც 0-დან მომხმარებლის შემოტანილ რიცხვამდე დაბეჭდავს:
# 'Even' ან 'Odd'-ს
# 7) მომხმარებელს შემოატანინეთ 10 რიცხვი. დაითვალეთ: რამდენია დადებითი, რამდენი უარყოფითი და ნული.
# 8) მოცემულია სია:
# fruits = ["apple", "banana", "orange", "grape"]
# შეცვალეთ "banana" სიტყვა "kiwi"-ით და დაბეჭდეთ განახლებული სია.
# 9) მოცემულია სია:
# nums = [4, 8, 12, 16, 20]
# დაწერეთ პროგრამა, რომელიც:
# შეკრებს პირველ და ბოლო ელემენტს და დაბეჭდავს შედეგს.
# 10) შექმენით სია და დაპრინტე თითოეული წევრი.
# 11) შექმენით რიცხვების სია დაპრინტე მხოლოდ ლუწი რიცხვები. 
# 12) შექმენით რიცხვების სია და დაპრინტე მხოლოდ ლუწი რიცხვების ჯამი. 
# 13) შექმენით რიცხვების სია და დაპრინტეთ მხოლოდ ის რიცხვები რომელიც მეტია 6 ზე.
# 14) შექმენით ცვლადი სადაც შეინახავ ნებისმიერ სიტყვას და დაპრინტე თითოეული ასო. 
# 15) შექმენით სია და დაპრინტე პირველი სამი წევრი. 

#3 
# number = int(input("write number: "))

# if number % 2==0 :
#     print("es ricxvi luwia")
# else:
#     print("kentia")


#4
# Temperature = int(input("enter temperature: "))

# if Temperature > 30 :
#     print("its hot")
# elif 15 < Temperature < 30 :
#     print("It's Warm")
# else :
#     print("It's Cold")


#5
# num =int(input("write number: "))

# if num % 2 == 0 and num > 0 :
#     print("Positive even")
# elif num % 2 != 0 and num > 0 :
#     print("Positive odd")
# else : 
#     print("Negative")



#6
# num1 = int(input("enter number: "))

# for i in range (0 , num1 + 1) :
#     if i % 2 == 0 :
#         print(i, "Even")
#     else :
#         print(i, "odd")


#7 ???

#8
# fruits = ["apple", "banana", "orange", "grape"]
# fruits[1] = "kiwi"
# print(fruits)

#9
# nums = [4, 8, 12, 16, 20]
# Total = nums[1] + nums[-1]
# print(Total)

#10
# films = ["se7en", "interstelar" , "showshank redeprion" , "southpow" , "avatar" , "F1"]
# print(films[0])
# print(films[1])
# print(films[2])
# print(films[3])
# print(films[4])
# print(films[5])

#11
# nums1 = [3, 6, 7, 12, 34, 98, 103, 116, 21]

# for num in nums1 :
#     if num % 2 == 0 :
#         print(num)


#12
# nums2 = [3,7,8,13,16,19,22]


# even_sum = 0

# for i in nums2 :
#     if i % 2 ==0 :
#         even_sum += i
# print(even_sum)


#13

# nums3 = [3,7,8,13,16,19,22]

# even_sum = 0

# for i in nums3 :
#     if i > 6 :
#         even_sum += i
# print(even_sum)

# #14
# film = "interstellar"

# for i in film :
#     print(film)



#15

films = ["se7en", "interstelar" , "showshank redeprion" , "southpow" , "avatar" , "F1"]
print(films[0])
print(films[1])
print(films[2])










