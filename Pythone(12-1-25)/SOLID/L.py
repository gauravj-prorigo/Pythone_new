from abc import ABC,abstractmethod
class Account:
    accounts = []
    def __init__(self,accountType,blance):
        self.accountType = accountType
        self.blance = blance
        
     
    def add_Account(self):
            Account.accounts.append({"AccountType":self.accountType,"Blance":self.blance})
        
      
class Bank(ABC):
    @abstractmethod
    def withdraw(self,ref,amount):
           pass
    @abstractmethod        
    def deposite(self,ref,amount): 
         pass   
         

class Current_Account(Bank):
      
      def withdraw(self,ref,amount):
            ref.accounts["blance"] -=  amount
            
      def deposite(self,ref,amount): 
         ref.accounts["blance"] +=  amount    
         
         
class Saving_Account(Bank):
      
      def withdraw(self,ref,amount):
            ref.accounts["blance"] -=  amount
            
      def deposite(self,ref,amount): 
         ref.accounts["blance"] +=  amount 
         
         
class FixDepo_Account(Bank):
      
      def withdraw(self,ref,amount):
           print("Not allowed")
            
      def deposite(self,ref,amount): 
         ref.accounts["blance"] +=  amount          
                            
                            
                            
Ac1 = Account("Saving",5000)
Ac2 = Account("Current",6000) 

sav1 = Saving_Account()
                           