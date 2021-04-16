class Student:
    def __init__(self,name,roll,course,marks):
        self.name=name
        self.roll=roll
        self.course=course
        self.marks=marks
    def printvalue(self):
        print("Name: ",self.name)
        print("Roll no : ",self.roll)
        print("Course : ",self.course)
        print("Marks : ",self.marks)
f=open("mark","r")
for line in f :
    data=line.split(",")
    name=data[0]
    roll=data[1]
    course=data[2]
    marks=int(data[3])
    obj=Student(name,roll,course,marks)
    if(marks>190):
        obj.printvalue()

