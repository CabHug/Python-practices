#Programa inicial para administrar una libreria

class Library:
    def __init__(self):
        self.inventary = []

    def getInvet(self):
        if self.inventary:
            for i in self.inventary:
                print(i.name)
        else:
            print("We don't have invenraty yet :c")

    def setInvent(self, name):
        self.inventary.append(name)

class Book:
    def __init__(self, name):
        self.name = name
        self.number = 0

    def addBook(self, n):
        self.number += n

    def sustBook(self, n):
        if self.number >= n:
            self.number -= n
            print(f"Book setted! current number {self.number}")
        else:
            print(f"Not enought books, current number {self.number}")


libro1 = Book("libro1")
libro1.addBook(5)

libro2 = Book("libro2")
libro2.addBook(2)

Hugo_library = Library()
Hugo_library.setInvent(libro1)
Hugo_library.setInvent(libro2)

Hugo_library.getInvet()
    