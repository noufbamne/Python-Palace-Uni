'''Create a Python program that compares two objects using identity operators. Modify one object 
and check how it affects the identity comparison.'''

# Create two lists with the same values
list1 = [1, 2, 3]
list2 = [1, 2, 3]

# Compare identity before modification
print("Before modification:")
print("list1 is list2:", list1 is list2)  # False (Different objects)
print("list1 is not list2:", list1 is not list2)  # True (Different memory locations)

# Modify list1
list1.append(4)

# Compare identity again after modification
print("\nAfter modifying list1:")
print("list1 is list2:", list1 is list2)  # Still False (Objects are still different)
print("list1 is not list2:", list1 is not list2)  # Still True (Memory locations are different)

'''# Assign list1 to list2 (Now both refer to the same object)
list2 = list1

# Compare identity after assignment
print("\nAfter assignment:")
print("list1 is list2:", list1 is list2)  # True (Now both are the same object)
print("list1 is not list2:", list1 is not list2)  # False (They share the same memory location)'''

'''
Flowchart:
       ┌───────────────┐
       │    Start      │
       └──────┬────────┘
              ▼
       ┌───────────────────────┐
       │ Create list1, list2   │
       └──────┬────────────────┘
              ▼
       ┌───────────────────────────────┐
       │ Check: list1 is list2?        │
       └──────┬───────────┬────────────┘
             No▼          ▼ Yes
   ┌────────────────┐   ┌────────────────────────┐
   │ Print False    │   │ Print True             │
   │ Print True for │   │ Print False for        │
   │ list1 is not list2 │ list1 is not list2     │
   └──────────┬─────┘   └──────────┬────────────┘
              ▼                    ▼
       ┌───────────────────────────┐
       │ Append 4 to list1         │
       └──────┬────────────────────┘
              ▼
       ┌───────────────────────────────┐
       │ Check: list1 is list2?        │
       └──────┬───────────┬────────────┘
             No▼          ▼ Yes
   ┌────────────────┐   ┌────────────────────────┐
   │ Print False    │   │ Print True             │
   │ Print True for │   │ Print False for        │
   │ list1 is not list2 │ list1 is not list2     │
   └──────────┬─────┘   └──────────┬────────────┘
              ▼                    ▼
       ┌───────────────────────────┐
       │ Assign list2 = list1      │
       └──────┬────────────────────┘
              ▼
       ┌───────────────────────────────┐
       │ Check: list1 is list2?        │
       └──────┬───────────┬────────────┘
             No▼          ▼ Yes
   ┌────────────────┐   ┌────────────────────────┐
   │ Print False    │   │ Print True             │
   │ Print True for │   │ Print False for        │
   │ list1 is not list2 │ list1 is not list2     │
   └──────────┬─────┘   └──────────┬────────────┘
              ▼                    ▼
       ┌───────────────┐
       │     End       │
       └───────────────┘

How the Flowchart Works:
The program starts by creating list1 and list2.
It checks their identity (is operator). Since they are different objects, it follows the NO path and prints:
python
Copy
Edit
list1 is list2: False
list1 is not list2: True
It modifies list1 by appending 4. Then it checks identity again, but the result remains the same (NO path).
It assigns list1 to list2, making them refer to the same object.
When it checks identity again, the answer is YES, and the program prints:
python
Copy
Edit
list1 is list2: True
list1 is not list2: False
The program ends.'''