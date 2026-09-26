
#  1
# შექმენი ფუნქცია sum_numbers(*args), რომელიც მიიღებს 
# (რამდენიც გინდა) რიცხვს და დააბრუნებს მათ ჯამს.

def sum_numbers(*args):
    return sum(args)


print(sum_numbers(5, 10, 15))



#  2
# ყველაზე დიდი რიცხვი
# შექმენი ფუნქცია largest_number(*args), რომელიც დააბრუნებს 
# გადაცემულ რიცხვებს შორის ყველაზე დიდს.

def largest_number(*args):
    return max(args)

print("\n--- დავალება 2 ---")
print(largest_number(3, 8, 1, 20, 5))



# 3
# შექმენი ფუნქცია count_even(*args), რომელიც დათვლის 
# რამდენი ლუწი რიცხვია გადაცემულ არგუმენტებში.

def count_even(*args):
    count = 0
    for num in args:
        if num % 2 == 0:
            count += 1
    return count

print("\n--- დავალება 3 ---")
print(count_even(2, 7, 10, 15, 18))



#  4
# საშუალო არითმეტიკული
# შექმენი ფუნქცია average(*args), რომელიც დააბრუნებს 
# ყველა რიცხვის საშუალოს.

def average(*args):
    if not args:
        return 0
    return sum(args) / len(args)

print("\n--- დავალება 4 ---")
print(average(10, 20, 30))



#  5
# შექმენი ფუნქცია რომელსაც გადასცემ ორ რეგულარულ არგუმენტს 
# მაგ: name ,age და დანარჩენია არგუმენტები შეინახე *args ში 
# და გამოიტანე ყველა მათგანი

def display_person_info(name, age, *args):
    print(f"სახელი: {name}")
    print(f"ასაკი: {age}")
    print("დამატებითი არგუმენტები (*args):")
    for arg in args:
        print(arg)

print("\n--- დავალება 5 ---")
display_person_info("გიორგი", 22, "სტუდენტი", "თბილისი", "Python developer")



#  6
# შექმენი ფუნქცია print_info(**kwargs), რომელიც დაბეჭდავს 
# ველა გადაცემულ key: value წყვილს.

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("\n--- დავალება 6 ---")
print_info(name="Goga", age=20, city="Tbilisi")


#  7
# შექმენი ფუნქცია print_values(**kwargs), რომელიც მხოლოდ 
# მნიშვნელობებს დაბეჭდავს.

def print_values(**kwargs):
    for value in kwargs.values():
        print(value)

print("\n--- დავალება 7 ---")
print_values(name="Goga", age=20, city="Tbilisi")



#  8
# გასაღებების რაოდენობა
# შექმენი ფუნქცია count_keys(**kwargs), რომელიც დააბრუნებს 
# რამდენი გასაღები (key) გადაეცა.

def count_keys(**kwargs):
    return len(kwargs)

print("\n--- დავალება 8 ---")
print(count_keys(a=1, b=2, c=3, d=4))



#  9
# შექმენი ფუნქცია სადაც გააერთანებ როგორც regular არგუიმენტებს 
# ასევე *args **kwargs , გამოძახების დროს გადაეცი შესაბამისი არგუმენტები, 
# კომენტარის სახით ახსენით თუ რომელი არგუმენტი რომელ პარამეტრშ შეიანხება და რატომ

def process_data(main_id, status, *args, **kwargs):
    print(f"main_id: {main_id}")
    print(f"status: {status}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")



print("\n--- დავალება 9 ---")
process_data(101, "active", "item1", "item2", user="Nika", role="admin")



#  10
# შექმენი ფუნქცია sum_numbers(**kwargs), რომელიც მხოლოდ იმ 
# მნიშვნელობებს შეკრებს, რომლებიც რიცხვებია.

def sum_numbers_kwargs(**kwargs):
    total = 0
    for value in kwargs.values():
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            total += value
    return total

print("\n--- დავალება 10 ---")
print(sum_numbers_kwargs(a=10, b="ტექსტი", c=20.5, d=True, e=5))



#  11
# შექმენი დეკორატორი, რომელიც ფუნქციის შესრულებამდე დაბეჭდავს 
# "Starting...", ხოლო დასრულების შემდეგ "Finished!".

def start_finish_decorator(func):
    def wrapper(*args, **kwargs):
        print("Starting...")
        result = func(*args, **kwargs)
        print("Finished!")
        return result
    return wrapper

@start_finish_decorator
def do_something():
    print("ფუნქცია სრულდება...")

print("\n--- დავალება 11 ---")
do_something()



# 12
# შექმენი დეკორატორი, რომელიც ნებისმიერი ფუნქციის შესრულებამდე დაბეჭდავს: Welcome!
# შემდეგ კი გაუშვებს ფუნქციას.

def welcome_decorator(func):
    def wrapper(*args, **kwargs):
        print("Welcome!")
        return func(*args, **kwargs)
    return wrapper

@welcome_decorator
def greet(name):
    print(f"გამარჯობა, {name}!")

print("\n--- დავალება 12 ---")
greet("გიორგი")


# 13
# შექმენი დეკორატორი, რომელიც ფუნქციის შესრულებამდე და 
# შესრულების შემდეგ დაბეჭდავს:
#
def line_decorator(func):
    def wrapper(*args, **kwargs):
        print("--------------------")
        result = func(*args, **kwargs)
        print("--------------------")
        return result
    return wrapper

@line_decorator
def show_message():
    print("ეს არის მთავარი ტექსტი")

print("\n--- დავალება 13 ---")
show_message()