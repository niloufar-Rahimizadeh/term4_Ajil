class Dog:
    tail_number = 1
    hand_foot_n = 4
    def __init__(self, breed, color, name, age):
        self.breed = breed
        self.color = color
        self.name = name
        self.age = age


my_dog = Dog("Husky", "black", "willie", 3) 

my_dog.tail_number = 2
my_dog.breed = "German"

print(my_dog.tail_number)
print(my_dog.breed)