# This program calculates the bill each person should pay with the tip included. 
# Welcoming message
welcome_message = "Welcome to the tip calculator!"
print(welcome_message)

# Prompt user for inputs

bill = float(input("What was the total bill? $"))
tip_percentage = float(input("How much tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

# Calculations
tip = bill * (tip_percentage / 100)
total_bill = bill + tip
individual_bill = total_bill / number_of_people

# "{:.2f}".format(individual_bill) is a function that rounds off (to 2 decimal numbers) without truncating the zero(0)
individual_bill = "{:.2f}".format(individual_bill)

# Final message to display 
message = f"Each person should pay: ${individual_bill}"
print(message)

