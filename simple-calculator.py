#author: BubaPy

#This part prints the chosing menu on the start

print("Add - 1")
print("Subtract - 2")
print("Multiply - 3")
print("Divide - 4")
chos = int(input("Please press 1 - 4 to begin! "))

#This part is for Addition

if chos == 1:
    add1 = float(input("Enter the first number to add: "))
    add2 = float(input("Enter the second number to add: "))
    print("Your total is: ", add1 + add2)

#This part is for subtraction

if chos == 2:
    sub1 = float(input("Enter the first number to subtract: "))
    sub2 = float(input("Enter the second number to subtract: "))
    print("Your subtraction is: ", sub1 - sub2)

#This part is for multiplication

if chos == 3:
    mul1 = float(input("Enter the first number to multiply: "))
    mul2 = float(input("Enter the second number to multiply: "))
    print("Your multiplication is: ", mul1 * mul2)

#This part is for dividation

if chos == 4:
    div1 = float(input("Enter the first number to divide: "))
    div2 = float(input("Enter the second number to divide: "))
    print("Your dividation is: ", div1 / div2)