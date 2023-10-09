print("Calculator")

number1 = float(input("Enter the first number : "))
number2 = float(input("Enter the Second number : "))
print("""
Press 1 for Addition
Press 2 for Subtraction
Press 3 for Multiplication
Press 4 for Division""")

choice = int(input("enter Your Choice 1-4: "))
if choice == 1:
    sum = number1+number2
    print("Then addition of two numbers is :",sum)
elif choice == 2:
    print("The Subtraction of two numbers is : ",number1-number2)
elif choice == 3:
    print("The Multiplication of two numbers is : ",number1*number2)
elif choice == 4:
    print("The Division of two numbers is : ",number1/number2)
else:
    print("Invalid Input")
