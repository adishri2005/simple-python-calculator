#1.ADD
#2.SUBTRACT
#3.DIVIDE
#4.MULTIPLY

print(" ")
print("Welcome to the calculator")
print(" ")
print("Select an operation to perform:")
print(" ")
print("1.ADD")
print("2.SUBTRACT")
print("3.DIVIDE")
print("4.MULTIPLY")
print(" ")

OPERATION = input()

if OPERATION == "1":
 num1 = int(input("Enter Number 1: "))
 num2 = int(input("Enter Number 2: "))
 print("Total is " + str(int(num1) + int(num2)))
 print("Thank you for using the calculator :)")
 again_operation =input()

elif OPERATION == "2":
 num1 = int(input("Enter Number 1: "))
 num2 = int(input("Enter Number 2: "))
 print("Total is " + str(int(num1) - int(num2)))
 print("Thank you for using the calculator :)")
 again_operation =input()

elif OPERATION == "3":
 num1 = int(input("Enter Number 1: "))
 num2 = int(input("Enter Number 2: "))
 print("Total is " + str(int(num1) / int(num2)))
 print("Thank you for using the calculator :)")
 again_operation =input()

elif OPERATION == "4":
 num1 = int(input("Enter Number 1: "))
 num2 = int(input("Enter Number 2: "))
 print("Total is " + str(int(num1) * int(num2)))
 print("Thank you for using the calculator :)")
 again_operation =input()

else:
 print("Invalid Entry, Please Try Again")  
 print("Thank you for using the calculator :)")
