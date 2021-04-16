class Person:
    def m1(self,name):
        self.name=name
class Address(Person):
    def m2(self,adrs):
        self.adrs=adrs
        print("Name: ",self.name)
        print("Address : ",self.adrs)
class Mobile(Address):
    def m3(self,mob):
        self.mob=mob
        print("Mobile: ",self.mob)
class Age:
    def m4(self,ageof):
        self.ageof=ageof
class Weight:
    def m5(self,wght):
        self.wght=wght
class Health(Age,Weight):
    def m6(self):
        print("Weght: ", self.wght)
        print("Age: ", self.ageof)
        print("End")


obj=Mobile()
obj.m1("Minnu")
obj.m2("xyzzzzzzzzzzzz")
obj.m3(9548754674)
obj2=Health()
obj2.m4(25)
obj2.m5(50)
obj2.m6()