from abc import ABC,abstractmethod
class Mobile(ABC):
    
    @abstractmethod
    def send(self):
        pass
    
    @abstractmethod
    def phone(self):
        pass
    
class Smartphone(Mobile):
    
    def phone(self):
        print("calling function") 
        
    def send(self):
        print("Message functionlity")        
        
    
    
        
        

call = Smartphone()
msg = Smartphone()

call.phone()               
msg.send()