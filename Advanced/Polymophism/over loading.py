class Person:
    def show(self,num1):
        self.num1=num1
        print(self.num1)
class Student(Person):
    def show(self,num2,num3):
        self.num2=num2
        self.num3=num3
        print(self.num2,self.num3)
obj=Student()
obj.show(2)

#If given only one argument person show mwthod will work and 2 argument student show mwthod will work. This is overloading
#overloading is not supported , so no output
