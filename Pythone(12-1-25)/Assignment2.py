class Book:
    def __init__(self,Name,author,year):
        self.Name = Name
        self.author = author
        self.year = year
    
    def display(self):
        print(f"The name of book is {self.Name}")
        print(f"Author is {self.author}")
        print(f"Year of publish is {self.year}")
    
class DigitalBook(Book):
    
    def __init__(self,Name,author,year,price):
        super().__init__(Name,author,year)
        self.price = price
        
    
    def display(self):
        super().display()
        print(f"And the price is {self.price}")
          
    
    
DB = DigitalBook("The last ride","Gaurav",1947,550)  
DB.display()    
    