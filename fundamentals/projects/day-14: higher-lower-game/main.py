from random import choice
from game_data import data
from art import logo, vs
from clear_screen import clear

def detail():
    """Returns a dictionary about a random celebrity."""
    return choice(data)

def celebrity_info(celebrity):
    """Takes in celebrity dictionary and displays information about them."""
    return f"{celebrity['name']}, a {celebrity['description']}, from {celebrity['country']}."

def follower_count(celebrity):
    """Takes in celebrity follower count and returns it in int format."""
    return int(celebrity['follower_count'])

def check_answer(celebrity_a_followers, celebrity_b_followers, score):
    """Compares who has more followers"""
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    global should_continue
    if guess == "a":
        if celebrity_a_followers > celebrity_b_followers:
            return score + 1
        else:
             should_continue = False
             return f"Sorry, that's wrong 😅. Final score: {score}."
    else:
        if celebrity_b_followers > celebrity_a_followers:
            return score + 1
        else:
             should_continue = False
             return f"Sorry, that's wrong 😅. Final score: {score}."

def clear_and_dispaly():
    """Clears the screen and prints logo."""
    clear()
    print(logo)

#Flag 
should_continue = True
score = 0

celebrity_a = detail()

print(logo)

while should_continue:

    celebrity_b = detail()

    #Generate new info about celebrity if both have the same details
    if celebrity_a == celebrity_b:
        celebrity_b = detail()

    celeb_a = celebrity_info(celebrity_a)
    celebrity_a_followers = follower_count(celebrity_a)
    print(f"Compare A: {celeb_a}")

    #display follower count associated with celebrity a
    #print(f"celebrity a : {celebrity_a_followers}")

    print(vs)

    celeb_b = celebrity_info(celebrity_b)
    celebrity_b_followers = follower_count(celebrity_b)
    print(f"Against B: {celeb_b}")

    #display follower count associated with celebrity a
    #print(f"celebrity b : {celebrity_b_followers}")

    #Assign score to check_answer function to keep track of score
    score = check_answer(celebrity_a_followers, celebrity_b_followers, score)

    if should_continue == True:
       clear_and_dispaly()
       print(f"You're right! 😎, current score: {score}.")

    #Switch celebrity info
    celebrity_a = celebrity_b

if should_continue == False:
    clear_and_dispaly()
    print(score)
