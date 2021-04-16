#3. Create a Book class with instance Library_name, book_name, author, pages?

class Book:
    def __init__(self,library_name,book_name,author,pages):
        self.library_name=library_name
        self.book_name=book_name
        self.author=author
        self.pages=pages
    def printvalue(self):
        print("Library name: ",self.library_name)
        print("Book Name: ","self.book_name")
        print("Author :",self.author)
        print("Pages: ",self.pages)
obj=Book("LMK","Promise","Nikitha ",150)
obj.printvalue()