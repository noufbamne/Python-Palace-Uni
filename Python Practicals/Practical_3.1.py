'''Write a Python program to calculate the bonus for an employee based on the following 
conditions: 
• If the employee has more than 10 years of experience, they receive a 20% bonus on their salary. 
• If the employee has between 5 and 10 years of experience, they receive a 10% bonus. 
• If the employee has less than 5 years of experience, they receive a 5% bonus. 
• If the employee's performance rating is below 3 (on a scale of 1 to 5), they are not eligible for 
a bonus, regardless of experience. 
Input: 
Salary (integer) 
Years of experience (integer) 
Performance rating (float) 
Expected Output: The bonus amount and final salary after adding the bonus.'''

# Take inputs from the user
salary = int(input("Enter employee's salary: "))
experience = int(input("Enter years of experience: "))
rating = float(input("Enter performance rating (1 to 5): "))

# Initialize bonus percentage
bonus_percentage = 0

# Check performance rating condition first
if rating < 3:
    print("No bonus due to low performance rating.")
else:
    # Determine bonus based on experience
    if experience > 10:
        bonus_percentage = 20
    elif experience >= 5:
        bonus_percentage = 10
    else:
        bonus_percentage = 5

    # Calculate bonus amount
    bonus_amount = (bonus_percentage / 100) * salary
    final_salary = salary + bonus_amount

    # Display the results
    print("Bonus Amount:", bonus_amount)
    print("Final Salary after bonus:", final_salary)


'''
Flowchart:
┌───────────────┐
       │    Start      │
       └──────┬────────┘
              ▼
       ┌─────────────────────┐
       │ Take Salary,        │
       │ Experience, Rating  │
       └────────┬────────────┘
                ▼
       ┌─────────────────────┐
       │ Is Rating < 3?      │
       └───────┬─────────────┘
          Yes ▼   No ▼
   ┌─────────────┐ ┌───────────────────────┐
   │ Print "No   │ │ Check Experience:     │
   │ Bonus" & End│ │ More than 10 years?   │
   └─────────────┘ └──────────┬────────────┘
                              ▼
                    ┌──────────────────────┐
                    │ Bonus = 20% of Salary│
                    └───────┬──────────────┘
                        No ▼  Yes ▼
              ┌───────────────────────────┐
              │ Experience between 5-10?  │
              └───────┬───────────────────┘
                  No ▼   Yes ▼
      ┌──────────────────────────────┐
      │ Bonus = 5% of Salary         │
      └──────────┬───────────────────┘
                 ▼
      ┌──────────────────────────────┐
      │ Calculate Bonus Amount       │
      │ Final Salary = Salary + Bonus│
      └──────────┬───────────────────┘
                 ▼
      ┌───────────────────────────┐
      │ Print Bonus Amount &      │
      │ Final Salary              │
      └──────────┬────────────────┘
                 ▼
           ┌──────────┐
           │   End    │
           └──────────┘
Explanation of the Flowchart:
Start the program.
Take input for:
Salary
Years of experience
Performance rating
Check performance rating:
If rating < 3, no bonus is given → End.
Otherwise, continue checking experience.
Check years of experience:
More than 10 years? → 20% bonus
Between 5-10 years? → 10% bonus
Less than 5 years? → 5% bonus
Calculate the bonus amount.
Calculate the final salary (salary + bonus).
Print bonus amount and final salary.
End the program.
'''