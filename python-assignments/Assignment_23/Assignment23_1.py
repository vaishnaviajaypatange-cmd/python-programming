class Bookstore:
    NoOfBooks = 0

    def __init__(self,name,author):
        self.name = name
        self.author = author
        Bookstore.NoOfBooks += 1

    
    
    def Display(self):
        print(f"{self.name} by {self.author}.No of books : {self.NoOfBooks}")


obj1 = Bookstore("linux system programming","robert love")
obj1.Display()

obj2 = Bookstore("C Programming","Dennis Ritchie")
obj2.Display()