class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printvalue(self):
        print("name: ",self.name)
        print("age : ",self.age)
class Student(Person):
    def __init__(self,roll,marks,name,age):
        super().__init__(name,age)
        self.roll=roll
        self.marks=marks
    def print(self):
        print(self.roll)
        print(self.marks)
cr=Student(36,100,"Minnu",25)
cr.printvalue()
cr.print()









