from abc import ABC,abstractmethod

class product:
    def __init__(self,proname,price):
        self.proname = proname
        self.price = price
        
class Cart():

    def __init__(self):
        self.items = []

    def add(self,product):
        pass
        self.items.append({"ProductName":product.proname,"ProductPrice":product.price})
             
    def calculate(self):
        total = 0
        for x in self.items:
            total  += x["ProductPrice"]
        return total    
            

class Invoice:
    def __init__(self,cart):
         print("Invoice of", cart.calculate())

class SaveDB(ABC):     
    @abstractmethod
    def saveDB(self,c):
        pass     
         
class SqlDB(SaveDB):      
     def saveDB(self,c):
        print("Save into sql DB",c.items)
        
class mongoDB(SaveDB):          
     def saveDB(self,c):
        print("Save into Mongo DB",c.items)
        
class oracalDB(SaveDB):         
     def saveDB(self,c):
        print("Save into oracal DB",c.items)                


p1 = product("Iphone",5000)
p2 = product("Samsung",2000)
p3 = product("oppo",1000)

C = Cart()

C.add(p1)
C.add(p2)
C.add(p3)
print(C.calculate())

I = Invoice(C)

sql = SqlDB()
sql.saveDB(C)

mongo = mongoDB()
mongo.saveDB(C)





    