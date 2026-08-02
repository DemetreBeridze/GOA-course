# 1) შექმენი dict შენს შესახებ რომლის ელემენტებია name: surname: და age: აქედან
#  კი გამოიტანეთ ტერმინალში ყველა ელემენტი

dict1 = {
    "name" : "demetre",
    "lastname" : "beridze",
    "age" : 16,
}
print(dict1.keys)


# 2) გადმოგეცემათ სია numbers = [1, 2, 3, 4, 5] გამოიტანეთ ტერმინალში ახალი სია სადაც numbers-ს გააორმაგებთ
numbers = [1, 2, 3, 4, 5]
duplicate_nums = [num*2 for num in numbers]
print(duplicate_nums)

# 3) გადმოგეცემათ სია numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] გამოიტანეთ მხოლოდ და მხოლოდ კენტი
#  რიცხვები ამ სიიდან ტერმინალში

numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in numbers1:
    if i % 2 != 0:
        print(i)