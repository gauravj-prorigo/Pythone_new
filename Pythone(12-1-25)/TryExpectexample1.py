class baseclass:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def add(self):
        try:
            ans = self.a/self.b
            print(f"answer is {ans}") 
        
        except ZeroDivisionError as e:
               print(e)     
      
      


val = baseclass(10,2)
val.add() 