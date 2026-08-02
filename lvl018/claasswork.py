def greet(name):
    return "Hello " + name

print(greet("Demetre"))


def jami(x, y):
    return x + y
print(jami(4 , 8))


def odd_or_even(num) :
    if num % 2 == 0:
        print("ecven")
    else:
        print("odd")
print(odd_or_even(3))
print(odd_or_even(12))



def xarisxi (a ,b):
    return a**b
print(xarisxi(3,3))



def string_length(text):
    return len(text)

print(string_length("Hello"))      # 5
print(string_length("bye"))  # 9





def inverted_word(word):
    return word[::-1]
print(inverted_word("interstellar"))



def numbers (numbers):
    return sum(numbers)


nums = [1, 2, 3, 4, 5]
print(numbers(nums))   




def adult_or_not (name, age):
    if age > 18 :
        print("thise person is adult")
    else:
        print("")