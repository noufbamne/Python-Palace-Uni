''' Implement a Python program that uses compound assignment operators to solve an equation 
step-by-step, such as calculating the area of a triangle given base and height, and then adding a 
constant to the result. '''

# Take input for base and height
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculate area using the formula: Area = (1/2) * base * height
area = 1  # Start with 1
area /= 2  # Divide by 2 (for the formula)
area *= base  # Multiply by base
area *= height  # Multiply by height

print("Triangle Area:", area)

# Add a constant value (e.g., 5) to the area
constant = 5
area += constant

print("Final Area after adding", constant, ":", area)

'''
Flowchart:
      Start
        │
        ▼
 Enter base and height
        │
 Initialize area = 1
        │
 Divide area by 2 (area /= 2)
        │
 Multiply area by base (area *= base)
        │
 Multiply area by height (area *= height)
        │
 Print Triangle Area
        │
 Add constant to area (area += constant)
        │
 Print Final Area
        │
       End

Flowchart Explanation:
Start
Input base and height
Initialize area as 1
Apply formula step by step using *=, /=
Print the triangle area
Add a constant (e.g., 5)
Print final area
End
'''