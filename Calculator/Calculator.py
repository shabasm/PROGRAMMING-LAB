num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
choice = int(input("Choose any option:"))
result = 0
if choice == 1:
    result = num1+num2
elif choice == 2:
    result = num1-num2
elif choice == 3:
    result = num1*num2
elif choice == 4:
    result = num1/num2
print("Result is ", float(result))
