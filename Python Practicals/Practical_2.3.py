'''Write a Python program that tests for membership of an element in a nested list or tuple. For 
example, check if the number 7 is present in [(1, 2, 3), [4, 5, 6], {7, 8, 9}].'''

# Function to check membership in a nested structure
def is_present(nested_structure, element):
    for item in nested_structure:
        if isinstance(item, (list, tuple, set)):  # Check if item is a list, tuple, or set
            if element in item:  # Check if element is inside
                return True
    return False  # Return False if not found

# Nested structure
nested_data = [(1, 2, 3), [4, 5, 6], {7, 8, 9}]

# Element to check
element_to_find = 7

# Check and print result
if is_present(nested_data, element_to_find):
    print(element_to_find, "is present in the nested structure.")
else:
    print(element_to_find, "is NOT present in the nested structure.")

'''
Flowchart:
           ┌───────────────┐
       │     Start     │
       └──────┬────────┘
              ▼
       ┌──────────────────────────┐
       │ Take nested structure and│
       │ element to find          │
       └──────┬───────────────────┘
              ▼
       ┌──────────────────────────┐
       │ Loop through each item in│
       │ nested structure         │
       └──────┬───────────────────┘
              ▼
       ┌──────────────────────────┐
       │ Is the item a list, tuple│
       │ or set?                  │
       └──────┬─────────────┬──────┘
             No ▼            ▼ Yes
     ┌──────────────────┐  ┌───────────────────┐
     │ Skip item, move  │  │ Check if element │
     │ to next item     │  │ is in the item   │
     └──────┬───────────┘  └─────────┬─────────┘
            │                         ▼
            │                ┌────────────────┐
            │                │ Is element in  │
            │                │ this item?     │
            │                └─────┬───────┬──┘
            │                     No ▼      ▼ Yes
            │              ┌──────────┐  ┌───────────────────────┐
            │              │ Continue │  │ Return True, print    │
            │              │ checking │  │ "Element is present"  │
            │              │ next item│  └──────────┬────────────┘
            │              └──────────┘             ▼
            │                              ┌──────────────┐
            │                              │     End      │
            │                              └──────────────┘
            ▼
      (Loop completes without finding element)
       ┌─────────────────────────────┐
       │ Return False, print         │
       │ "Element not found"         │
       └──────────┬──────────────────┘
                  ▼
            ┌───────────┐
            │    End    │
            └───────────┘

Flow Explanation (with NO paths clearly marked):
Start the program.
Take inputs (nested structure & element to find).
Loop through each item in the nested structure.
Check if the item is a list, tuple, or set:
YES → Check if the element is inside.
NO → Skip this item and move to the next one.
Check if the element is in the item:
YES → Return True, print "Element is present", and END.
NO → Continue checking the next item.
If the loop completes without finding the element, return False, print "Element not found", and END.'''


'''
flowchart:

       ┌───────────────┐
       │     Start     │
       └──────┬────────┘
              ▼
       ┌──────────────────────────┐
       │ Take nested structure and│
       │ element to find          │
       └──────┬───────────────────┘
              ▼
       ┌──────────────────────────┐
       │ Loop through each item in│
       │ nested structure         │
       └──────┬───────────────────┘
              ▼
       ┌──────────────────────────┐
       │ Is the item a list, tuple│
       │ or set?                  │
       └──────┬─────────────┬──────┘
             No ▼            ▼ Yes
     ┌──────────────────┐  ┌───────────────────┐
     │ Skip item, move  │  │ Check if element  │
     │ to next item     │  │ is in the item    │
     └──────┬───────────┘  └─────────┬─────────┘
            │                         ▼
            ▼                ┌────────────────┐
      (Continue loop)         │ Is element in │
                               │ this item?    │
                               └─────┬───────┬──┘
                                    No ▼      ▼ Yes
                        ┌───────────────────┐  ┌───────────────────────┐
                        │ Are there more    │  │ Return True, print    │
                        │ items to check?   │  │ "Element is present"  │
                        └─────┬───────┬─────┘  └──────────┬────────────┘
                              No ▼      ▼ Yes            ▼
                     ┌──────────────────────┐   ┌──────────────┐
                     │ Return False, print  │   │     End      │
                     │ "Element not found"  │   └──────────────┘
                     └──────────┬───────────┘
                                ▼
                          ┌───────────┐
                          │    End    │
                          └───────────┘
How the Flow Works (With NO Paths Clearly Marked):
Start the program.
Take inputs (nested structure & element to find).
Loop through each item in the nested structure.
Check if the item is a list, tuple, or set:
YES → Move to check if the element is inside.
NO → Skip this item and continue to the next one.
Check if the element is in the item:
YES → Return True, print "Element is present", and END.
NO → Move to check if there are more items left.
Are there more items left?
YES → Continue checking.
NO → Return False, print "Element not found", and END.'''