from operator import *
print("\t----Simple Calculator----")
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operation = input("Enter the operation you want to do (+,-,*,/): ")
    operations = {'+':add,'-':sub,'*':mul,'/':truediv}
    print(f"{num1} {operation} {num2} = {operations[operation](num1,num2)}")
except Exception as e:
    print("Invalid input")
