import time
# დაწერე დეკორატორი @say_hello, რომელიც ფუნქციის გამოძახებამდე 
# დაიბეჭდავს ტექსტს "ფუნქცია იწყებს მუშაობას...", ხოლო 
# ფუნქციის დასრულების შემდეგ დაიბეჭდავს "ფუნქციამ დაასრულა მუშაობა!".

def say_hello(func):
    def wrapper(*args, **kwargs):
        print("ფუნქცია იწყებს მუშაობას...")
        result = func(*args, **kwargs)
        print("ფუნქციამ დაასრულა მუშაობა!")
        return result
    return wrapper

@say_hello
def process_data():
    print("მონაცემები მუშავდება...")

print("--- დავალება 2 ---")
process_data()



# დაწერე დეკორატორი @timer, რომელიც ზომავს და ბეჭდავს, 
# რამდენი წამი დასჭირდა ფუნქციის შესრულებას (time მოდულის გამოყენებით).
# დეკორატორმა უნდა შეძლოს ნებისმიერი ფუნქციის შეფუთვა 
# და ორიგინალი ფუნქციის შედეგის დაბრუნება.

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()          # დაწყების დრო
        result = func(*args, **kwargs)    # ორიგინალი ფუნქციის გაშვება
        end_time = time.time()            # დასრულების დრო
        execution_time = end_time - start_time
        print(f"ფუნქციის შესრულებას დასჭირდა: {execution_time:.4f} წამი")
        return result                     # ორიგინალი შედეგის დაბრუნება
    return wrapper

@timer
def slow_function(seconds):
    time.sleep(seconds)                   # დროებითი პაუზა ტესტირებისთვის
    return f"პროცესი დასრულდა {seconds} წამში"

print("\n--- დავალება 3 ---")
output = slow_function(1.5)
print(f"დაბრუნებული შედეგი: {output}")



# შექმენი დეკორატორი, რომელიც ფუნქციის შესრულებამდე 
# დაბეჭდავს "Starting...", ხოლო დასრულების შემდეგ "Finished!".

def start_finish_decorator(func):
    def wrapper(*args, **kwargs):
        print("Starting...")
        result = func(*args, **kwargs)
        print("Finished!")
        return result
    return wrapper

@start_finish_decorator
def run_task():
    print("დავალება სრულდება...")

print("\n--- Level 51 (11) ---")
run_task()



# შექმენი დეკორატორი, რომელიც ნებისმიერი ფუნქციის შესრულებამდე 
# დაბეჭდავს: Welcome! შემდეგ კი გაუშვებს ფუნქციას.

def welcome_decorator(func):
    def wrapper(*args, **kwargs):
        print("Welcome!")
        return func(*args, **kwargs)
    return wrapper

@welcome_decorator
def greet_user(name):
    print(f"მოგესალმებით, {name}!")

print("\n--- Level 51 (12) ---")
greet_user("გიორგი")



#   13
# შექმენი დეკორატორი, რომელიც ფუნქციის შესრულებამდე 
# და შესრულების შემდეგ დაბეჭდავს: 

def line_decorator(func):
    def wrapper(*args, **kwargs):
        print("--------------------")
        result = func(*args, **kwargs)
        print("--------------------")
        return result
    return wrapper

@line_decorator
def display_message():
    print("ეს არის ტექსტი ხაზებს შორის")

print("\n--- Level 51 (13) ---")
display_message()