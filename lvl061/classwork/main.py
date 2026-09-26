# შექმენით Cat კლასი ატრიბუტებით: breed და color.
# დაუმატეთ make_sound მეთოდი ('Meow').
# შექმენით მინიმუმ ორი ინსტანცია და გამოიძახეთ ყველა ატრიბუტი/მეთოდი.


class Cat:
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

    def make_sound(self):
        print("Meow")


# პირველი ინსტანცია 
cat1 = Cat("Siamese", "White")

# მეორე ინსტანცია (კატა 2)
cat2 = Cat("Persian", "Grey")



print("--- Cat 1 ---")
print(f"ჯიში (Breed): {cat1.breed}")
print(f"ფერი (Color): {cat1.color}")
print("ხმა (Sound):", end=" ")
cat1.make_sound()



print("--- Cat 2 ---")
print(f"ჯიში (Breed): {cat2.breed}")
print(f"ფერი (Color): {cat2.color}")
print("ხმა (Sound):", end=" ")
cat2.make_sound()