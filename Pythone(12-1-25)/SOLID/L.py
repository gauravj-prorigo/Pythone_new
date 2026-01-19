# class Bird:
#     def fly(self):
#         print("All birds can fly")
        
#     def eat(self):
#         print("Bird eat ")    
        
# class sparrow(Bird):
#     def fly(self):
#         print("sparrow can fly but not much high") 
        
# class penguin(Bird):
#     def fly(self):
#         print("can't fly")        
        
# class App():
#     def __init__(self,feature):
#         self.feature =  feature
#         pass                  
    

# A = App(sparrow()) 
# A.feature.eat()
# A.feature.fly()   

# A1 = App(penguin())
# A1.feature.fly()



class Bird:
    def eat(self):
        print("Bird eat ") 
        
class Flyingbird(Bird):
         def fly(self):
            print("All birds can fly")      
        
class sparrow(Flyingbird):
    def fly(self):
        print("sparrow can fly but not much high") 

        
class penguin(Bird):
    def swim(self):
        print("penguin can swim")        
   
        
class App():
    def __init__(self,feature):
        self.feature =  feature
        pass                  
    

A = App(sparrow()) 
A.feature.eat()  