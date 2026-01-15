class Book:
    def __init__(self,name,author,date):
        self.name = name
        self.author = author
        self.data= date
        
    def display(self):
        print(f"Name of the book is {self.name} and author of the book is \n{self.author} and publish in {self.data}")
        
b1 = Book("Gaurav","Saurav",1927)
b1.display()
