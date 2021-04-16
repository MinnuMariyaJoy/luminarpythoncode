#5. What is method overriding give an example using Books class?

#Over riding is when the child class obeject over ride parent class object.

class Book1:
    def fav(self,peom):
        self.peom=peom
        print("favorite book is ",self.peom)
class Book2:
    def fav(self,novels):
        self.novels=novels
        print("favorite book is ",self.novels)
obj=Book2()
obj.fav("Revolution 2020")
