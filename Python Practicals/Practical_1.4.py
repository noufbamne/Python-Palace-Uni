#Write a python script that calculates the sum of the first ten natural numbers. USe multiline comments to explain how the sum is derived mathematically then write the code.
'''
The summ of the first n natural number can be derived usinfg the formula\
sum = n*(n + 1)/2

# For the first 10 natural numbers (1 to 10):
sum = 10(10 + 1)/2 
    = 10 * 11/2 
    = 110/2
    = 55
'''
#initialize the number
natural_number = 10

#calculate sum
sum_of_natural_numbers = natural_number * (natural_number + 1)

#Print the sum of first 10 natural numbers
print("Sum of first 10 natural numbers are: ", sum_of_natural_numbers)