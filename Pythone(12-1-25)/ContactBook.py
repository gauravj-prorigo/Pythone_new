x=[]
def book(name,age,marks):
   x.append({'Name':name,'age':age,'Marks':marks})
   display(x)
 
def display(x):
   print(x)
 
while range(5):  
 name = input("Enter the name :")
 age = int(input("Enter the age :"))
 marks = int(input("Enter the marks :"))
 book (name ,age,marks)