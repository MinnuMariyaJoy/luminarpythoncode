class Person:
    def setVal(self,name,age):   #passing attributes
        self.age=age               #slef.age will accept as attribute within class
        self.name=name

    def printValue(self):
        print("name",self.name)
        print("age",self.age)
obj=Person()
obj.setVal("ram",23)
obj.printValue()
