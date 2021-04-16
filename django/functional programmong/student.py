class Student:
    def __init__(self,rollno,name,course,total):
        self.roolno=rollno
        self.name=name
        self.course=course
        self.total=total
    def __str__(self):
        return self.name
s1=Student(12,"anna","BBA",120)
s2=Student(14,"anee","BBA",10)
s3=Student(12,"athul","BBA",130)
print(s1)

studentlist=[]
studentlist.append(s1)
studentlist.append(s2)
studentlist.append(s3)

studenttotal=list(map(lambda stud:stud.total,studentlist))
print(studenttotal)