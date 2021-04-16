class Employee():
    companyname="luminar"
    def setVal(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary

    def printValue(self):
        print("id",self.id)
        print("name",self.name)
        print("salary",self.salary)
        print("company name :",Employee.companyname)
obj = Employee()
obj.setVal(1089,"ram",23000)
obj.printValue()

employe2=Employee()
employe2.setVal(1900,"anil",25000)
employe2.printValue()