class Shape:
    
    def shape(self):
        print("shape is simple")
        
class Cirle(Shape):
    
    def circle(self):
        print("Shape of circle is simple") 
        
class Squar(Shape):
    
    def squar(self):
        print("shape of square is simple")    
        
        
C = Cirle()
C.circle()
C.shape()  
S = Squar()
S.squar()
S.shape()      
                       