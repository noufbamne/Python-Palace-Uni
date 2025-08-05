# The factorial of a number is the product of all positions integers from 1 to n

number = int (input("Enter the number to calculate it's fcatorial: "))

result = 1

for i in range(1, number +1):
    result *= i

print("The factorial of", number, "is:", result)