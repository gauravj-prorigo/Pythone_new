class payment:
    def pay(self):
        print("lots of way of pay")
        
class Upi(payment):
    def pay(self):
        print("UPI payment method")  
        
class Card(payment):
    def pay(self):
        print("Card payment method") 
        
        
class Cash(payment):
    def pay(self):
        print("Cash payment method")    
        
        
        
U = Upi()
U.pay()
Ca = Card()
Ca.pay()
C = Cash()
C.pay()                           