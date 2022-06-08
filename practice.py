class Animal():
    ACCELERATION = 9.8 #attribute
    
    def __init__(self, name, species, legs = 4):
        self.name = name
        self.species = species
        self.legs = legs
    
    # Generic Parent (animal) method -- No OverRide
    def make_sound(self):
        print('reeeeeee')
    
    # Creating a child class
class Dog(Animal): # putting the parent inside class dog
    SPEED = 15
    
    def printInfo(self):
        print(f"The dog runs at {SPEED} mph and accelerates towards the ground at {ACCELERATION} mps")
        
    # Creating a grandchild cass
class Mut(Dog):
    COLOR = "brown and tanish"
    
    # OverRide the Animal Class__init__ method by using the Dog class
    def __init__(self, name, species, eye_color, legs = 4):
        Dog.__init__(self, name, species, legs)  # pulling from dog() which is pulling from animal()
        self.eye_color = eye_color
        
    #overRide the make_sound method from the animal class
    def make_sound(self): #method
        print("ruff ruff ruff awoooo")




cat = Animal("Sassy", 'Himalayan cat')
print(cat.name)
dog = Dog('Shadow', 'Golden Retriever')
cat.make_sound()
dog.make_sound()
print(dog.ACCELERATION)
print(dog.SPEED)  #specificaly only for dog, not for any other animal like can't do cat.SPEED

mut = Mut('Eyo', 'chihuahua-terrier mix and maybe also beagle?', 'brown')
mut.make_sound()  # overRides the animal sound




class Mut(Dog):
    COLOR = "brown and tan"
    
    #overriding the Animal class __init__ with the super().__init__
    def __init__(self, name, species, eye_color, legs = 4):
        super().__init__(name, species, legs)
        # super will reference the class that the child class takes in
        self.eye_color = eye_color
    def make_sound(self):
        print('woof')

Czika = Mut('Czika', 'mini pinscher', 'black and tan')
Czika.make_sound()
print(Czika.SPEED)