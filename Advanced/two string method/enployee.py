class Employee:
    companyname="luminar"
    def setvalue(self,id,name,age,salry):
        self.id=id
        self.name=name
        self.age=age
        self.salry=salry
    def printvalue(self):
        print("id = ",self.id)
        print("name= ",self.name)
        print("age= ",self.age)
    def __str__(self):
        return str(self.id)
empl1=Employee()
empl1.setvalue(1089,"rahul",26,20000)
print(empl1)
empl2=Employee()
empl2.setvalue(1190,"Arun",28,25000)
print(empl2)
