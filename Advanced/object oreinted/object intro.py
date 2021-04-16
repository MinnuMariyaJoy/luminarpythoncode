#class:design pattern  Eg:plan for a house, tv
#object:real number   eg : sumsung, lg
#references :name that refers to memory location of an object (remote)


class Person:   #class      #cap should be given to the first letter
    def walk(self):   #self appeard becase it is a method inside class
        print("Person is walking")
    def run(self):     #methods
        print("person is running")
    def jumping(self):
        print("person is jumping")

obj=Person()    #this is the reference, use this refernce for calling methods
obj.walk()
obj.run()
obj.jumping()

ab=Person()  #another object, we can create any number of object
ab.walk()
