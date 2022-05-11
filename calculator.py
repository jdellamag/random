# Calculator program

# Define the computations
def add():
    return(num1 + num2)
def subtract():
    return(num1 - num2)
def multiply():
    return(num1 * num2)
def divide():
    return(num1 / num2)

# Prompt with error message if a lowercase letter is entered - then loop back to top - would like to do this right as i enter it
def invalid_input():
    return("Invalid calculation choice - please choose A, B, C, or D")

# Map the user input to the correct calculation
def calc():
    if ask == "A":
        return(add())
    elif ask == "B":
        return(subtract())
    elif ask == "C":
        return(multiply())
    elif ask == "D":
        return(divide())
    else:
        return(invalid_input())

# Ask the user what they want to do
ask = input("What calculation do you want to do?\n A - Add\n B - Subtract\n C - Multiply\n D - Divide \n I want to:  ")

# Add note about invalid calc - below is wrong
if ask != ("A","B"):
    print("Invalid Selection - Choose Again")

# Ask the user to input first and second numbers
num1 = int(input("Enter your first number:  "))
num2 = int(input("Enter you second number:  "))

# Print the answer
print(calc())


# Send invalid calc message before prompted to enter first and second number
# Ask if they want to do another calculation
 # test commit to see if picked up by GH