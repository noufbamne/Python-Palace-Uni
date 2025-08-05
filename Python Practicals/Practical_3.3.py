'''Write a program to determine if a given year is a leap year. However, add the following extra 
conditions: 
A year is a leap year if it is divisible by 4 but not divisible by 100 unless it is also divisible by 
400. 
If the year is in the 21st century (from 2001 to 2100), print a message indicating whether it is a 
"21st Century Leap Year" or not. 
If the year is before the 21st century or after it, print a simple message whether it's a leap year 
or not. 
Input: A single integer representing the year.
Expected Output: A message indicating whether the year is a leap year or not, with the extra 
condition for the 21st century.'''

# Function to check if a year is a leap year
def is_leap_year(year): #2022, 2024 1999 1996
    # Leap year condition
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Take user input
year = int(input("Enter a year: "))

# Check leap year status
if is_leap_year(year):
    if 2001 <= year <= 2100:  # Check if it's in the 21st century
        print(year, "is a 21st Century Leap Year.")
    else:
        print(year, "is a Leap Year.")
else:
    if 2001 <= year <= 2100:
        print(year, "is NOT a 21st Century Leap Year.")
    else:
        print(year, "is NOT a Leap Year.")

'''
flowchart:

        ┌───────────────┐
        │    Start      │
        └──────┬────────┘
               ▼
        ┌───────────────────────┐
        │   Take input: year     │
        └─────────┬──────────────┘
                  ▼
        ┌──────────────────────────┐
        │ Check: (year % 4 == 0 AND │
        │ year % 100 != 0) OR (year │
        │ % 400 == 0)?              │
        └───────┬───────────────┬───┘
              No ▼               ▼ Yes
    ┌───────────────────┐  ┌─────────────────────┐
    │ Print "NOT a Leap │  │ Check: 2001 ≤ year  │
    │ Year" & End       │  │ ≤ 2100?             │
    └───────────────────┘  └───────┬─────────────┬───┘
                                   No ▼          ▼ Yes
                      ┌────────────────────┐  ┌────────────────────────────┐
                      │ Print "Leap Year"   │  │ Print "21st Century Leap   │
                      │ & End               │  │ Year" & End                │
                      └────────────────────┘  └────────────────────────────┘


Explanation:
Start the program.
Take input: year.
Check if it is a leap year using the condition:
(year % 4 == 0 AND year % 100 != 0) OR (year % 400 == 0).
If No, print "NOT a Leap Year" and End.
If Yes, check if the year is in the 21st century (2001-2100).
If Yes, print "21st Century Leap Year" and End.
If No, print "Leap Year" and End.
End the program.
'''