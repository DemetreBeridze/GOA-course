# პირველი 5 დავალება codeware იყო
# 6) სტუდენტების ლექსიკონი (Dict)
# 1. Dict-ის შექმნა (სახელი: ნიშანი)
students = {
    "გიორგი": 45,
    "ანა": 85,
    "ნიკა": 92,
    "მარიამი": 48
}
# 2. ახალი სტუდენტის დამატება
students["დავითი"] = 78

# 3. არსებული სტუდენტის ნიშნის განახლება
students["გიორგი"] = 60

# 4. List Comprehension: დავტოვოთ მხოლოდ ის სტუდენტები (სახელები), 
# რომელთა ნიშანიც 50-ზე მეტია
passed_students = [name for name, grade in students.items() if grade > 50]

print("6) 50-ზე მეტი ქულის მქონე სტუდენტები:", passed_students)


# 7) რიცხვების კვადრატები და ლუწი რიცხვების ფილტრაცია

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. List Comprehension: რიცხვების კვადრატები
squares = [num ** 2 for num in numbers]

# 2. List Comprehension + if: კვადრატების სიიდან მხოლოდ ლუწი რიცხვები
even_squares = [sq for sq in squares if sq % 2 == 0]

print("7) კვადრატები:", squares)
print("7) მხოლოდ ლუწი კვადრატები:", even_squares)



# 8) სიტყვების სიგრძის მიხედვით გაფილტვრა

words = ["Python", "AI", "Development", "Code", "Learning", "Data"]

# List Comprehension + if: მხოლოდ ის სიტყვები, რომელთა სიგრძეც (len) > 4
long_words = [word for word in words if len(word) > 4]

print("8) სიტყვები 4-ზე მეტი ასოთი:", long_words)


# 9) პროდუქტების ფასების გაფილტვრა

products = {
    "ვაშლი": 1.5,
    "ყველი": 5.0,
    "პური": 0.8,
    "რძე": 3.5,
    "ყავა": 7.2
}

# List Comprehension + if: იმ პროდუქტების სახელები, რომელთა ფასიც > 3
expensive_products = [item for item, price in products.items() if price > 3]

print("9) 3 დოლარზე ძვირი პროდუქტები:", expensive_products)