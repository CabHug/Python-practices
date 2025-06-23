#Programa inicial para administrar una libreria

class Library:
    def __init__(self):
        self.inventary = []

    def getInvet(self):
        if self.inventary:
            print("We don't have invenraty yet :c")

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
    