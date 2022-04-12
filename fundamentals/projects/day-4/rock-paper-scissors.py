# This is a rock, paper and scissors game.

# Import random module
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

# Make list of choices
choices = [rock, paper, scissors]

# Users choice
users_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print(choices[users_choice])

# Computers choice
random_position = random.randint(0,2)
computers_choice = choices[random_position]
print("Computer chose: \n" +  computers_choice)

# Determine winner
if users_choice == 0 and random_position == 2:
    print("You win")
elif users_choice == 1 and random_position  == 0:
    print("You win")
elif users_choice == 2 and random_position  == 1:
    print("You win")
elif users_choice == random_position :
    print("It's a draw")
else:
    print("You lose")

