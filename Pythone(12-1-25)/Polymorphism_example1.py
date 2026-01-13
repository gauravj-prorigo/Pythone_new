class Animal():
    
    def sound(self):
        print("Each Animal have diff sound")
        
class Dog(Animal):
    
    def sound(self):
        print("Dog sound Bawww Baww")    
        
class Cat(Animal):
    
    def sound(self):
        print("Car sound is Mauuu")           
        
        
C = Cat()
C.sound()
D = Dog()
D.sound()        