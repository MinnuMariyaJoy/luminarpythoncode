#6. Create objects of the following file and print the details of student with maximum mark?
# anu,1,bca,200 rahul,2,bba,177 vinod,3,bba,187 ajay,4,bca,198 maya,5, bba,195


class Students:
    def __init__(self,name,roll,course,marks):
        self.name=name
        self.roll=roll
        self.course=course
        self.marks=marks
    def printvalue(self):
        print("Name :",self.name)
        print("Roll no: ",self.roll)
        print("Course : ",self.course)
        print("Mark: ",self.marks)
f=open("max mark","r")
for line in f :
    data=line.split(",")
    name=data[0]
    roll=data[1]
    course=data[2]
    marks=int([data[3]])
    print(marks)
max=0

for i in marks:
    if (i>max):
        max=i
    else:
        pass

obj = Students(name, roll, course, marks)
obj.printvalue()









