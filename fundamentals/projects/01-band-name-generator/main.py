# This is a simple programm that generates a band name based on the inputs given by the user.
# This program uses concepts concerning: comments, variables, python built-in functions (print function & input function), escape sequences, and string concatenation.

# Welcome message
welcome_message = "Welcome to the Band Name Generator."
print(welcome_message)

# Prompt user 
city_name = input("What is the name of the city you grew up in?\n")
pet_name = input("What is your pets name?\n")

# Concate user inputs
band_name = city_name + " " + pet_name

# Display Generated Band Name
print("Your band name could be" + " " + band_name)
