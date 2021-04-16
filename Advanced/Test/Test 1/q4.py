#4. Create an Animal class using constructor and build a child class for Dog?


class Animal:
    def __init__(self,animaltype,food):
        self.animaltype=animaltype
        self.food=food
    def printvalue(self):
        print("Animal type :", self.animaltype)
        print("Food: ", self.food)

class Dog:
    animalname="dog"
    def m1(self):
        print("Animal Name: ", Dog.animalname)

obj2=Dog()
obj2.m1()
obj1=Animal("carnovoras","meat")
obj1.printvalue()
