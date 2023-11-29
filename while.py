'''This program functions to continually as a user for an input integer\
until the user enters -1,this the prompts the program to\
calculate the average of all the user inputs.'''
SUM_NUMBER = 0
i = 0
USER_INPUT = 0
while USER_INPUT != -1:
    USER_INPUT = int(input("Enter any interger: \n"))
    if USER_INPUT == -1:
        break
    SUM_NUMBER += USER_INPUT
    i += 1
    SUM_AVERAGE = SUM_NUMBER/i 
print("Thank you for your inputs.")
print(f"The average of all inputs is: {SUM_AVERAGE}.")