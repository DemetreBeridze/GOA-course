# mistakes in programming
# 1 - bugs (logical error) - მცირე შეცდომა კოდში რომელიც არ იწვევს პროგრამის შეჩერებას
# 2 - Exceptions (NameError, SyntaxError, IndexError, TypeError, ValueError) - ისეთი შეცდომები რომლებიც იწვევეს პროგრამის შეჩერებას

# ZeroDivisionError - ასწორებს შეცდომას, როდესაც რიცხვს 0ზე ვყოფთ
# მაგალითად :
result = 10 / 0
print(result)

# --------------4----------------
try:
    # მომხმარებელს შემოაქვს ორი რიცხვი
    num1 = float(input("შემოიტანეთ პირველი რიცხვი: "))
    num2 = float(input("შემოიტანეთ მეორე რიცხვი: "))
    # გაყოფა
    result = num1 / num2
    print(f" შედეგი: {result}")
except ZeroDivisionError:
    # თუ მეორე რიცხვი 0-ია:
    print("Can’t divide a number by 0.")
except ValueError:
    # თუ მომხმარებელმა რიცხვები არ შემოიტანა:
    print("გთხოვთ, შემოიტანოთ მხოლოდ რიცხვები.")


# ----------------5----------------
# 1. ვქმნით მომხმარებლის მონაცემების ლექსიკონს (Dictionary)
user_profile = {
    "სახელი": "გიორგი",
    "გვარი": "ბერიძე",
    "ასაკი": 25,
    "ქალაქი": "თბილისი"
}
# 2. ვცდილობ ისეთი key-ის გამოტანას, რომელიც არ არსებობს
try:
    # "პროფესია" ჩვენს ლექსიკონში არ არის, ამიტომ ეს ხაზი შეცდომას გამოიწვევს
    user_profession = user_profile["პროფესია"]
    print(f"მომხმარებლის პროფესიაა: {user_profession}")

except KeyError:
    print("შეცდომა: მოთხოვნილი მონაცემი (Key) ლექსიკონში არ არსებობს!")


# ---------6----------------
# 1. ELSE ბლოკი
# დანიშნულება: სრულდება მხოლოდ იმ შემთხვევაში, თუ "try" ბლოკში არანაირი შეცდომა არ მოხდა.
# მას ვიყენებთ მაშინ, როცა გვინდა რაღაც კოდი გაეშვას მხოლოდ წარმატებული ოპერაციის შემდეგ.

try:
    number = int("100") # ტექსტი წარმატებით გადაიქცევა რიცხვად
except ValueError:
    print("ეს კოდი არ გაეშვება, რადგან შეცდომა არ მომხდარა.")
else:
    print("წარმატება! 'else' ბლოკი გაეშვა, რადგან 'try'-ში შეცდომა არ დაფიქსირებულა.")



# 2. FINALLY ბლოკი
# განსაზღვრავს კოდის ბლოკს, რომელიც გაეშვება ნებისმიერ შემთხვევაში
# , მიუხედავად იმისა, მოხდა თუ არა შეცდომა try ბლოკში, ან  except-ში.

try:
    result = 10 / 0 # აქ მოხდება ZeroDivisionError
except ZeroDivisionError:
    print(" ნულზე გაყოფა მოხდა!")
finally:
    print("'finally' ყოველთვის სრულდება, მიუხედავად შეცდომებისა.")


# 3. RAISE 
# დანიშნულება: გამოიყენება პროგრამისტის მიერ შეცდომის (Exception) ხელოვნურად და განზრახ გამოსაწვევად.
#  მისი საშუალებით შესაძლებელია პროგრამის მუშაობის იძულებითი შეჩერება 
# ა იმ შემთხვევაში, თუ დარღვევია კოდის ლოგიკური პირობა.
# (მაგალითად, თუ მომხმარებელი ასაკში მიუთითებს უარყოფით რიცხვს: -5).

age = -5

if age < 0:
    raise ValueError("ასაკი არ შეიძლება იყოს უარყოფითი რიცხვი!")


# ----------------8------------------
try:
    print("Trying...")
except Exception:
    print("Error encountered")
finally:
    print("Code cleanup is done")


# ------9-----------------
def check_password(password_string):
    try:
        # 1. ვამოწმებთ სიგრძეს
        if len(password_string) < 8:
            raise ValueError("Password too short")
        # 2. ვამოწმებთ შეიცავს თუ არა სფეისს 
        if " " in password_string:
            raise SyntaxError("Password cannot contain spaces")
        # თუ არცერთი პირობა არ დაირღვა
        return "Password accepted"
    except (ValueError, SyntaxError) as error:
        # აქ ვიჭერთ ჩვენს მიერ გამოწვეულ შეცდომებს    
        return str(error)

print(check_password("123"))        # დაიბეჭდება: Password too short
print(check_password("12345 678"))  # დაიბეჭდება: Password cannot contain spaces
print(check_password("my_secret_pass_123")) # დაიბეჭდება: Password accepted