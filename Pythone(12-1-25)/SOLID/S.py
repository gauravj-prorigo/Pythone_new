class product:
    def __init__(self,proname,price):
        self.proname = proname
        self.price = price
        
class Cart():  
    def __init__(self):
        self.items = []

    def add(self,product):
        self.items.append({"ProductName":product.proname,"ProductPrice":product.price})
             
    def calculate(self):
        total = 0
        for x in self.items:
            total  += x["ProductPrice"]
        return total    
            

class Invoice:
    def __init__(self,cart):
         print("Invoice of", cart.calculate())

class SaveDB:
    def __init__(self,c):
         print("Save to DB" ,c.items)


p1 = product("Iphone",5000)
p2 = product("Samsung",2000)
p3 = product("oppo",1000)

C1 = Cart()
C1.add(p1)
C1.add(p2)
C1.add(p3)
print(C1.calculate())

I = Invoice(C1)
DB = SaveDB(C1)







    