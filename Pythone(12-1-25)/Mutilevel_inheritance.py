class Manger:
    def __init__(self,name):
        self.name = name
    
    def show_name(self):
        print(f"The name of Manger {self.name}")    
        
        
class Employee(Manger):
    
    def __init__(self,name,id):
        super().__init__(name)  
        self.id = id
    def show_id(self):
        print(f"id is {self.id}")    
        
        
class Person(Employee):
    def __init__(self, name, id,role):
         super().__init__(name, id) 
         self.role = role   
    def show_role(self):
         print(f"his assitance role is {self.role}") 
         
         
p = Person("Gaurav",30,"intern")  

p.show_name()
p.show_id()
p.show_role()                       