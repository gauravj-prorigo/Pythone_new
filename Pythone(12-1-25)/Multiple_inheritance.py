class Employee():
    
    def show_name(self,emp):
        print(f"Name of the Employee is {emp}")
        
class Department():
    
    def show_dep(self,dep):
        print(f"the dep name is {dep}") 
        
        
class ShowInfo(Employee,Department):
    pass

S = ShowInfo()

S.show_name("Gaurav")
S.show_dep("IT")              