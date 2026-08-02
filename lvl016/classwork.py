
word = (input("write your word: "))

if word != word.upper :
    print("incorrect")
else:
    print("correct")


word1 = (input("write your word and one letter: "))
index = word.find("-1")

print(index)


fruits = ['apple', 'banana', 'peach', 'pineapple']

fruits.append('orange')
fruits.append('kiwi')
fruits.append('mango')

print(len(fruits))