def prime(x):
    if(x<2):
        return False
    else:
       for i in range(2 ,x, +1):
           if(x % i ==0):
               return False
    return True  
 
x = int(input("Enter number to check is it prime or not :"))
ans = prime(x)
if ans:
    print(f"{x} is a prime number")
else:
    print(f"{x} is not prime number")  