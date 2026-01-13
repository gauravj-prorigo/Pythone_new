
def add(a,b):
    print("The addition is :",a+b)
def sub(a,b):
    print("The subtraction is :",a-b)
def multi(a,b):
    print("The multiplication is :",a*b)
def div(a,b):
    print("The division is :",a/b)  
    
 
print("Hello from Arithimatic.py")
print("Enter the two values")
a = int(input("Enter the number :"))
b = int(input("Enter the number :"))
ch = int(input("Enter the choice 1 for addition , 2 for sub , 3 for multi , 4 for div"))
 
if ch == 1:
    add(a,b)
elif ch == 2:
    sub(a,b)
elif ch == 3:
    multi(a,b)
elif ch == 4:
    div(a,b)        
else:
    print("Invalid choice")