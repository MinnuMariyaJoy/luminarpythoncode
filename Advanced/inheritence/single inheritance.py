class School:
    schoolname="choice"
    def m1(self,place):
        self.place=place
        print("School name ",School.schoolname)
        print(self.place)
class Student(School):
    def m2(self,student_name):
        self.student_name=student_name
        print(self.student_name,"is student at ",School.schoolname,"at ",self.place)
obj=Student()
obj.m1('trpntra')
obj.m2('minnu')
