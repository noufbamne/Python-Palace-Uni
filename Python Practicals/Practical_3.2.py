''' Write a program that takes the lengths of three sides of a triangle and determines the type of 
triangle: 
If all sides are equal, it is an Equilateral Triangle. 
If two sides are equal, it is an Isosceles Triangle. 
If no sides are equal, it is a Scalene Triangle. 
If the sum of any two sides is not greater than the third side, it is not a triangle. 
Input: Three positive integers representing the sides of a triangle. 
Expected Output: The type of triangle or a message saying "Not a triangle."'''

# Take input for three sides of a triangle
a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the third side: "))

# Check if it is a valid triangle
if a + b > c and a + c > b and b + c > a:
    # Check for triangle type
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not a triangle")

'''
Flowchart: 

        ┌───────────────┐
        │    Start      │
        └──────┬────────┘
               ▼
        ┌────────────────────────┐
        │ Take input: a, b, c     │
        └─────────┬───────────────┘
                  ▼
        ┌─────────────────────────────┐
        │ Check if (a + b > c) AND     │
        │ (a + c > b) AND (b + c > a) │
        └───────┬─────────────┬───────┘
               No ▼            ▼ Yes
        ┌─────────────────┐  ┌──────────────────────────┐
        │ Print "Not a    │  │ Check: a == b == c?      │
        │ Triangle" & End │  └───────┬───────────────┬──┘
        └─────────────────┘        No ▼              ▼ Yes
                         ┌──────────────────────────┐
                         │ Print "Equilateral       │
                         │ Triangle" & End         │
                         └──────────┬──────────────┘
                                    ▼
                         ┌───────────────────────────┐
                         │ Check: a == b OR b == c OR│
                         │ a == c?                   │
                         └───────┬───────────────┬───┘
                                No ▼              ▼ Yes
                      ┌────────────────────────┐
                      │ Print "Scalene Triangle│
                      │ & End                  │
                      └─────────┬──────────────┘
                                ▼
                     ┌──────────────────────────┐
                     │ Print "Isosceles Triangle│
                     │ & End                    │
                     └──────────────────────────┘

Flowchart Explanation:
Start the program.
Take input for three sides: a, b, and c.
Check if the sides form a valid triangle using the condition:
(a + b > c) AND (a + c > b) AND (b + c > a)
If No, print "Not a Triangle" and End.
Check the type of triangle:
If all sides are equal (a == b == c), print "Equilateral Triangle" and End.
Else, check if two sides are equal (a == b OR b == c OR a == c):
If Yes, print "Isosceles Triangle" and End.
If No, print "Scalene Triangle" and End.
'''