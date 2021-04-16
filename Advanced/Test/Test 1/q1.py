class Vehicle:
    def m1(self,registration,cost,mileage):
        self.registration=registration
        self.cost=cost
        self.mileage=mileage
    def m2(self):
        print("Registration: ",self.registration)
        print("Cost: ",self.cost)
        print("mileage: ",self.mileage)

class Bus(Vehicle):
    bname='Bus'
    def m3(self):
        print("Vehicle name : ", Bus.bname)

obj=Bus()
obj.m3()
obj.m1("KL AE 0890",1000000,"50km/ltr")
obj.m2()