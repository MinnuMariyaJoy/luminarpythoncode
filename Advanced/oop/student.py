class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printvalue(self):
        print("Name :",self.name)
        print("Age :",self.age)
    def __str__(self):
        return self.name
f=open("student","r")
for line in f :
    data=line.split(",")
    name=data[0]
    age=data[1]
    obj=Student(name,age)
    print(obj)
    obj.printvalue()
