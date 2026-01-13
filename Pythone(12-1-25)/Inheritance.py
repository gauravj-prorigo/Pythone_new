# class Book:
#     def __init__(self,name,author,year):
#         self.name =name
#         self.author = author
#         self.year = year
        
# class Info(Book):
#     def display(self):
#         print(f"The book name is {self.name} and its written by {self.author} and publish in {self.year}")  
        
# book = Info("Gaurav","khan",1650)        
                  
# book.display()                  


class Account:
    Account_num = 123456
    blance = 50000
    
    def show_blance(self):
        print(f"Account number {Account.Account_num} has blance {Account.blance}")
        
        
class SavingsAccount(Account):
    pass

check = SavingsAccount()
check.show_blance()        