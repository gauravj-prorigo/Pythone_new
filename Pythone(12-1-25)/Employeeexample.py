class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
    def nam(self):
        print(f"name of employee is {self.name}")    
        
    def pagar(self):
        print(f"salary is {self.salary}")    
        
        
class Manager(Employee):
    
    def manageteame(self):
        print("Lots of work we have to do team")        
        
 
m1 = Manager("gaurav",100000)  

m1.nam()
m1.pagar()
m1.manageteame()     