from abc import ABC ,abstractmethod

class onlinepayment(ABC):
    @abstractmethod
    def refund(self):
         pass
class payment(ABC):
    @abstractmethod
    def pay(self):
        pass
    
class onlinepay(payment,onlinepayment):
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
