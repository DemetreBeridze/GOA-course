#1
def print_user_info(name, *args):
    print(f"სახელი (name): {name}")
    
    print("*args-ის მნიშვნელობები:")
    for arg in args:
        print(arg)
        
    print(f"*args-ის მონაცემთა ტიპი: {type(args)}")


print_user_info("გიორგი", 25, "თბილისი", True, 99.5)

#2

def find_sum(*args):
    even_sum = 0
    for number in args:
        # ვამოწმებთ, არის თუ არა რიცხვი ლუწი
        if number % 2 == 0:
            even_sum += number
    return even_sum


result = find_sum(10, 15, 22, 33, 40, 7)
print(f"ლუწი რიცხვების ჯამი: {result}")

#3

def process_kwargs(**kwargs):
    # პარამეტრის ტიპი
    print(f"**kwargs-ის მონაცემთა ტიპი: {type(kwargs)}")
    
    # თვითონ პარამეტრი (ლექსიკონი / dictionary)
    print(f"თვითონ kwargs: {kwargs}")
    
    # თითოეული მნიშვნელობა
    print("kwargs-ის მნიშვნელობები:")
    for value in kwargs.values():
        print(value)


process_kwargs(person1="ანა", person2="ნიკა", person3="მარიამი", person4="დავითი")

#4

def combined_function(regular, *args, **kwargs):
    print(f"ჩვეულებრივი არგუმენტი (regular): {regular}")
    print(f"დამატებითი არგუმენტები (*args): {args}")
    print(f"Keyword არგუმენტები (**kwargs): {kwargs}")

combined_function("მთავარი ტექსტი", 1, 2, 3, role="admin", active=True)