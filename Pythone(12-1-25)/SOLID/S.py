class product:
    def __init__(self,proname,price):
        self.proname = proname
        self.price = price
        
class Cart():
    items = []  
    sum = 0
    def add(self,product):
        pass
        Cart.items.append({"ProductName":product.proname,"ProductPrice":product.price})
             
    def calculate(self):
        for x in Cart.items:
            Cart.sum  += x["ProductPrice"]
        return Cart.sum    
            

class Invoice:
    def __init__(self,cart):
         print("Invoice of", cart.sum)

class SaveDB:
    def __init__(self,c):
         print("Save to DB" ,c.items)


p1 = product("Iphone",5000)
p2 = product("Samsung",2000)
p3 = product("oppo",1000)
C = Cart()
C.add(p1)
C.add(p2)
C.add(p3)
print(C.calculate())
I = Invoice(C)
DB = SaveDB(C)




    