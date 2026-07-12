def greatest_of_two(a,b):
    if(a>b):
        print(a,"is the greatest value.")
    elif(a<b):
        print(b,"is the greatest value.")
    elif(a==b):
        print("Both value are equal.")
    else:
        print(" Invalid input")

num1=int(input("Enter the value of number1 value:"))
num2=int(input('Enter the value of number2 value:'))
greatest_of_two(num1,num2)