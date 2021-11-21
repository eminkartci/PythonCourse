
# QUESTION 1
# ## Take the inputs
# number1 = float(input("Enter the first number: "))
# number2 = float(input("Enter the second number: "))

# operationName = input("Enter the operation: ")

# ## Do the operation
# if operationName == "sum":
#     result = number1 + number2
# elif operationName == "sub":
#     result = number1 - number2
# elif operationName == "mul":
#     result = number1 * number2
# elif operationName == "div":
#     result = number1 / number2

# ## Print the result
# print(f"Result: {result}")

# QUESTION 2

# for i in range(10,1,-1):
#     print(i**2,end=" ")

# QUESTION 3

for satir in range(4): # [0 1 2 3]
    # space
    for space in range(satir): # []
        print(" ",end="")
    # sayi
    for sayi in range(4):
        print(satir+1,end="")

    print()
