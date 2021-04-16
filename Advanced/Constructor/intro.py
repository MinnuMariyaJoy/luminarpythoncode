# constructor: to initialise instance variables
# it autimatically invoke when creating object

class Employee():
    companyname = "luminar"

    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def printValue(self):
        print("id", self.id)
        print("name", self.name)
        print("salary", self.salary)
        print("company name :", Employee.companyname)


obj = Employee(1089, "ram", 2300)
obj.printValue()
