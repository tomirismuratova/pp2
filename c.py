class Book:
    def __init__(self, author, name):
        self.author = author
        self.name = name
    def func(self):
        print(self.author, self.name)
a = Book("Jane Austin", "Flower")
a.func()