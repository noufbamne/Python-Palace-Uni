#Write a program that take a string input from the user and prints it in reverse order with each seperated by comma

user_input = input("Enter a String: ")
reversed_string = ',' .join (user_input[:: -1])
print("Reversed string is: ", reversed_string)