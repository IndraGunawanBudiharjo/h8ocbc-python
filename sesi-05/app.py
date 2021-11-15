class Dog(): # class name PascalCase

    species = 'Canis Familiaris'

    def __init__(self, name, age, breed): # setiap method wajib ada self
        self.name = name
        self.age = age
        self.breed = breed
    
    def __str__(self):
        return f'{self.name} is {self.age} years old'

    # def description(self):
    #     return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        return f'{self.name} says {sound}'    

miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")

print(miles.name)
print(miles.species)
# miles.species = 'anjing' # ganti hanya pada instance nya
# Dog.species = 'anjing' # ganti di class
print(buddy.species)
print(miles)
print(miles.speak('Woof Woof'))

# # parent
# class Mom():
#     def __init__(self, name, hair_color):
#         self.name = name
#         self.hair_color = hair_color

#     def get_hair_color(self):
#         return self.hair_color

# # child
# class Children(Mom):
#     def __init__(self, name, new_hair_color, age):
#         super().__init__(name, new_hair_color)
#         self.age = age

# mom = Mom('ani', 'cokelat')
# print(f"{mom.name}'s hair color is {mom.hair_color}")
# first_daughter = Children('ita', 'ungu', 20) 
# print(f"{first_daughter.name}'s hair color is {first_daughter.hair_color}, and age is {first_daughter.age}")

