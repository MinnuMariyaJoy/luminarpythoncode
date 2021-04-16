#07/04/2021

# class Book:
#     def __init__(self,pages):
#         self.pages=pages
#
#     def __add__(self, other):
#         return self.pages+other.pages
#
# b1=Book(100)
# b2=Book(200)
# print(b1+b2)



#one more book object
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return Book(self.pages + other.pages) #object will get printed
    def __sub__(self, other):
        return "overloading substraction"

    def __str__(self):            #for coverting object printing
        return(str(self.pages))




b1 = Book(100)
b2 = Book(200)
b3=Book(100)
print(b1-b2)
print(b1 + b2 +b3)