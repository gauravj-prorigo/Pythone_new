from abc import ABC ,abstractmethod

class payment(ABC):
    @abstractmethod
    def pay(self):
        pass
      
class onlinepayment(payment,ABC):
    @abstractmethod
    def refund(self):
         pass   
     
class onlinepay(onlinepayment):
    def pay(self):
        print("online payment")

    def refund(self):
        print("refund avalible")  

class cash(payment):
    def pay(self):
        print("paying by cash")


p1 = onlinepay()
p1.pay()
p1.refund()

p2 = cash()
p2.pay()
