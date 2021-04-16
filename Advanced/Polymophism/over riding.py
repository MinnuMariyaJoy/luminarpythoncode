class Parent:
    def properties(self):
        print("10 l , 2 cars")
    def marry(self):
        print("with ram")

class Child(Parent):
    def marry(self):
        print("with arun ")

c=Child()
c.marry()

#child class method will over ride parent class
#this is not averloading since there is no arguments