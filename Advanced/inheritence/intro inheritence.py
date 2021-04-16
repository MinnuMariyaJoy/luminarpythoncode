#Single inheritance

class Parent:
    parent_name='arun'
    def m1(self,age):             #parent class, base class,super class
        self.age=age
        print("my name is ",Parent.parent_name)
        print(self.age)

class Child(Parent):      #derived class or child class
    def m2(self):
        print("parent name is ",Parent.parent_name)
        print(self.age)


c=Child()
c.m1(20)
c.m2()


