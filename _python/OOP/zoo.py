

class Animal:
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness= happiness
    
    def feed (self):
        self.health += 10
        self.happiness += 10
        return self
    
    def display_info(self):
        print(f"{self.name}: age:{self.age} health:{self.health} happiness:{self.happiness}")
        return self


class Lion(Animal):
    def __init__(self, name, age=7, health=10, happiness=15):
        super().__init__(name, age, health, happiness)
        self.feature = "predator"
        self.sound = "Roar"

    def display_info(self):
        super().display_info()
        print(f"Animal's feature: {self.feature}, sound: {self.sound}")
        return self

    def feed (self):
        self.health += 20
        self.happiness += 15
        return self

class Dog(Animal):
    def __init__(self, name, age=5, health=5, happiness=10):
        super().__init__(name, age, health, happiness)
        self.feature = "pet"
        self.sound = "bark"

    def display_info(self):
        super().display_info()
        print(f"Animal's feature: {self.feature}, sound: {self.sound}")
        return self

    def feed (self):
        self.health += 15    
        self.happiness += 15
        return self


class Gazelle(Animal):
    def __init__(self, name, age, health, happiness):
        super().__init__(name, age, health, happiness)
        self.feature = "vegetarian animal"
        self.sound = "honk"

    def display_info(self):
        super().display_info()
        print(f"Animal's feature: {self.feature}, sound: {self.sound}")
        return self


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, name, age):
        self.animals.append(Lion(name,age))
    def add_dog(self, name):
        self.animals.append(Dog(name))
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        print(self.animals)
        for animal in self.animals:
            animal.display_info()

zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala",15)
zoo1.add_lion("Simba",10)
zoo1.add_dog("popi")
zoo1.add_dog("sepestian")
zoo1.print_all_info()
# #predator, Roar
# lion = Lion("lion",10,0,0)
# #pet,bark
# Dog = Dog("Dog", 7,5,20)
# #vegetarian animal,honk
# Gazelle = Gazelle("Gazelle",11,10,30)

# lion.feed().display_info()
# Dog.feed().display_info()
# Gazelle.feed().display_info()
