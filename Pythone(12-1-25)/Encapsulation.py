class Base:
    def __init__(self,name,age):
        self.__name = name
        self.__age =  age
        
    def get_name(self):
        return self.__name
    
    def set_name(self,nav):
        self.__name = nav
        
    def get_age(self):
            return self.__age
    
    def set_age(self,age):
        self.__age = age    
                
                
B = Base("Gaurav",22)    
print(B.get_name())   

B.set_name("Saurav")
print(B.get_name()) 

B1 = Base("Balaji",23)
print(B1.get_name())

B1.set_age(24)
print(B1.get_age())

