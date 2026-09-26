
#  1
# 1)შექმენი დეკორატორი, რომელიც ფუნქციის პასუხს 
# თავში და ბოლოში დაუმატებს '***'-ს.

def add_stars(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"***{result}***"
    return wrapper

@add_stars
def get_greeting():
    return "Hello World"

print("--- დავალება 1 ---")
print(get_greeting())  # დაბეჭდავს: ***Hello World***




# 2)შექმენი დეკორატორი, რომელიც ფუნქციის პასუხს 5-ს დაუმატებს.
# შექმენი სამი სხვა ფუნქცია, რომელიც სხვადასხვა ინტეჯერს დააბრუნებს 
# და სამივეს იგივე დეკორატორი გაუწერე.

def add_five(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + 5
    return wrapper

@add_five
def get_ten():
    return 10

@add_five
def get_twenty():
    return 20

@add_five
def get_negative():
    return -2

print("\n--- დავალება 2 ---")
print(get_ten())       # დაბეჭდავს: 15 (10 + 5)
print(get_twenty())    # დაბეჭდავს: 25 (20 + 5)
print(get_negative())  # დაბეჭდავს: 3  (-2 + 5)