class Pets:
    global pet_list
    def __init__ (self, pet_list):
        self.pet_list = pet_list

    def isHungry(self):
        for x in self.pet_list:
            if (x.hungry):
                return x.hungry
    
    def whos_hungry(self):
        list_lapar=[]
        for x in self.pet_list:
            if (x.hungry):
                list_lapar.append(x.name)
        return list_lapar

class Animal:
    def __init__ (self,name,age):
        self.name = name
        self.age = age
        self.hungry = True

    def eat(self):
        self.hungry = False

class Cat(Animal):
    species = "Felis catus"
    def sound(self):
        return "Miaw"

class Dog(Animal):
    species = "Canis lupus familiaris"
    def sound(self):
        return "Guk Guk"

class Bird(Animal):
    species = "Aves"
    def sound(self):
        return "tweet"