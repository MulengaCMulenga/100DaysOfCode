from random import choice
from clear_screen import clear
from art import logo

#Deal_card() function that uses the List.
def deal_card():
    """Returns a random card from the deck of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = choice(cards)
    return card

#Calculate_score() that takes a List of cards as input 
def calculate_score(cards):
    """Takes in list of cards and returns the sum of cards deck"""
    #Check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    #check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. 
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

#Compare() and pass in the user_score and computer_score.
def compare(user_score, computer_score):
    """Takes in users score and compares it against computers score, then returns the winner or the game is a draw"""
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"
    
def play_game():
    
    print(logo)
    #Deal the user and computer 2 cards each 
    user_cards = []
    computer_cards = []

    # Flag
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not is_game_over:
        #If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True

        #If the game has not ended, ask the user if they want to draw another card. 
        else:
            user_gets_another_card = input("Type 'y' to get anohter card, type 'n' to pass: ")
            if user_gets_another_card == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True


    #The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

#Ask the user if they want to restart the game. 
while input("Do you want to play a game of Blackjack? Type 'y' or 'n':  ") == "y":
   clear()
   play_game() 
