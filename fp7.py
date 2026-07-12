def factorial(a):
    fact=1

    for i in range(a,0,-1):
        fact*=i
    return fact

    
num=int(input("Enter the value of number:"))

print(factorial(num))
    
