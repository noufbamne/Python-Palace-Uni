'''
Write a program that converts a decimal number into binary and then performs bitwise 
operations (AND, OR, XOR, NOT) on two binary numbers. Then, use logical operators to 
check conditions based on the results. '''

# Convert decimal to binary
def decimal_to_binary(n):
    return bin(n)[2:]  # Convert to binary and remove '0b' prefix

# Take two numbers as input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Convert to binary
bin1 = decimal_to_binary(num1)
bin2 = decimal_to_binary(num2)

print("Binary of", num1, "is", bin1)
print("Binary of", num2, "is", bin2)

# Bitwise operations
and_result = num1 & num2
or_result = num1 | num2
xor_result = num1 ^ num2
not_result1 = ~num1
not_result2 = ~num2

print("AND result:", and_result, "Binary:", decimal_to_binary(and_result))
print("OR result:", or_result, "Binary:", decimal_to_binary(or_result))
print("XOR result:", xor_result, "Binary:", decimal_to_binary(xor_result))
print("NOT result of", num1, "is", not_result1)
print("NOT result of", num2, "is", not_result2)

# Logical operations
if and_result > 0 and or_result > 0:
    print("Both AND and OR results are greater than 0.")

if xor_result > 0 or not_result1 < 0:
    print("Either XOR result is positive or NOT result of first number is negative.")

if not (num1 == 0 and num2 == 0):
    print("At least one number is not zero.")

'''
Flowchart:

 Start
         │
         ▼
 Enter first number (num1)
         │
 Enter second number (num2)
         │
 Convert num1 to binary
         │
 Convert num2 to binary
         │
 Display binary values
         │
 Perform AND, OR, XOR, NOT operations
         │
 Display results
         │
 Check if (AND > 0 AND OR > 0)
       ┌─┴───┐
      Yes    No
       │      │
   Print Msg  │
       │      ▼
 Check if (XOR > 0 OR NOT num1 < 0)
       ┌─┴───┐
      Yes    No
       │      │
   Print Msg  │
       │      ▼
 Check if (num1 ≠ 0 OR num2 ≠ 0)
       ┌─┴───┐
      Yes    No
       │      │
   Print Msg  │
       │      ▼
        End
Flowchart Explanation
Start
Input two numbers from the user
Convert each number to binary
Display binary values
Perform bitwise operations (AND, OR, XOR, NOT)
Display results of bitwise operations
Check logical conditions
If AND and OR results are greater than 0, print a message
If XOR result is positive OR NOT num1 is negative, print a message
If at least one number is not zero, print a message
End
'''