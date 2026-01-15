class Bank:
    
    __blance = 14800
    
    def withdraw(self,amount):
        if(amount > Bank.__blance):
            print("insufficent blance")
            return    
        Bank.__blance  -= amount
        print(f"current balnce after deduction of {amount} is {Bank.__blance}")
        
    def deposite(self,amount):
        Bank.__blance  += amount
        print(f"Your account blance is {Bank.__blance}")    
          

Gaurav = Bank()
Gaurav.withdraw(8500)
Gaurav.deposite(14800)