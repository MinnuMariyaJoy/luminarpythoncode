#method is more important than class
class Swift:
    def start(self):
        print("swift car start method")
    def accelerate(self):
        print("swift car accelerate")
    def brk(self):
        print("swift car brk")

class Innova:
    def start(self):
        print("innova car start method")
    def accelerate(self):
        print("innova car accelerate")
    def brk(self):
        print("innova car brk")

class Person:
    def drive(self,car):
        car.start()
        car.accelerate()
        car.brk()

sw=Swift()
inno=Innova()
p=Person()
p.drive(sw)
