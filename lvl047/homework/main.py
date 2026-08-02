# მოცემული დავალებები შეასრულეთ Lambda-ს გამოყენებით.
# 2) დაწერეთ ფუნქცია, რომელიც მიიღებს მომხმარებლის სახელს. გვარსა და ასაკს. 
# ფუნქციამ დააბრუნოს მომხმარებლის მონაცემები f სტრინგის გამოყენებით.

user_info = lambda name, surname, age: f"სახელი: {name}, გვარი: {surname}, ასაკი: {age}"

# მაგალითი:
print(user_info("დემეტრე", "ბერიძე", 16))

# 3) დაწერეთ ფუნქცია, რომელიც გამოითვლის რიცხვების სიის საშუალო არითმეტიკულს.

average = lambda lst: sum(lst) / len(lst) if lst else 0

# მაგალითი:
print(average([10, 20, 30, 40]))  # შედეგი: 25.0

# 4) დაწერეთ ფუნქცია, რომელსაც გადაეცემა სტრინგი. პასუხად დააბრუნეთ არის თუ არა იგი პალინდრომი. (მოიძიეთ თუ რას ნიშნავს Palindrome).

is_palindrome = lambda s: s.lower() == s.lower()[::-1]

# მაგალითი:
print(is_palindrome("Radar"))  
print(is_palindrome("Hello"))  

# 5) დაწერეთ ფუნქცია, რომელიც აბრუნებს:
# • 'Positive' თუ რიცხვი დადებითია.
# • 'Negative' თუ რიცხვი უარყოფითი.
# • 'Zero' თუ რიცხვი ნულია. 
# გამოიყენეთ Ternary ოპერატორი.

check_number = lambda n: 'Positive' if n > 0 else ('Negative' if n < 0 else 'Zero')

# მაგალითი:
print(check_number(5))   
print(check_number(-3))  
print(check_number(0))   

# 6) დაწერეთ ფუნქცია, რომელიც არგუმენტად მიიღებს სიას. პასუხად დააბრუნოს სიის თითოეული რიცხვი გამრავლებული 2-ზე.

double_elements = lambda lst: [x * 2 for x in lst]

# მაგალითი:
print(double_elements([1, 2, 3, 4]))  

# 7) გამოიყენეთ List comprehension და Lambda მოცემული პროგრამის დასაწერად:
# დაწერეთ ფუნქცია, რომელსაც გადასცემთ სტრინგების სიას. ფუნქციამ უნდა დააბრუნოს მხოლოდ ისეთი სტრინგები, რომელთა სიგრძეც 5-ს აღემატება.

filter_long_strings = lambda lst: [s for s in lst if len(s) > 5]

# მაგალითი:
words = ["ვაშლი", "მსხალი", "ფორთოხალი", "ბანანი", "ატამი"]
print(filter_long_strings(words))  

# 8) გამოიყენეთ List comprehension და Lambda მოცემული პროგრამის დასაწერად:
# დაწერეთ ფუნქცია, რომელსაც გადასცემთ ინტეჯერების სიას. ფუნქციამ უნდა დააბრუნოს მხოლოდ ისეთი რიცხვები, რომლებიც უარყოფითია.

get_negatives = lambda lst: [x for x in lst if x < 0]

# მაგალითი:
numbers = [10, -5, 3, -12, 0, -1, 8]
print(get_negatives(numbers))  