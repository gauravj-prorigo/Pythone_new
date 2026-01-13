from abc import ABC,abstractmethod

class baseclass(ABC):
    def __init__(self,model):
        self.model = model
        print("base class init method")
        
    @abstractmethod
    def start(self):
        pass
    
    def display():
        print("Hi i calling from baseclass")
        
class Bike(baseclass):
    
    def __init__(self,model,company):
        super().__init__(model)
        self.company = company
        print("bike class init method")
        print(f"Bike name is {self.model} and company is {self.company}")
        
    def start(self):
        print("Start with kick")
        
class car(baseclass):
    def start(self):
        print("Start with key")
               
class auto(baseclass):
    def start(self):
        print("Start with button")               
        
        
B = Bike("Kawasaki","ninja")  
B.start()
C = car("sonet") 
C.start()
A = auto("Bajaj")  
A.start()          