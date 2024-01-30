"""
L.H. Wong 2024-01-30
Guess the next card game
Is it higher or lower?
"""
import random as rd

# card list
cards = [
    "2♠", "2♥", "2♣", "2♦",
    "3♠", "3♥", "3♣", "3♦",
    "4♠", "4♥", "4♣", "4♦",
    "5♠", "5♥", "5♣", "5♦",
    "6♠", "6♥", "6♣", "6♦",
    "7♠", "7♥", "7♣", "7♦",
    "8♠", "8♥", "8♣", "8♦",
    "9♠", "9♥", "9♣", "9♦",
    "10♠", "10♥", "10♣", "10♦",
    "J♠", "J♥", "J♣", "J♦",
    "Q♠", "Q♥", "Q♣", "Q♦",
    "K♠", "K♥", "K♣", "K♦",
    "A♠", "A♥", "A♣", "A♦"
]

def to_value(card):
    """
    Convert card face to its value
    """
    card = card.replace('J', '11')
    card = card.replace('Q', '12')
    card = card.replace('K', '13')
    card = card.replace('A', '14')
    card = card.replace('♠', '').replace('♥', '').replace('♣', '').replace('♦', '')
    return int(card)

# Initialise variables
current_card = None
last_card = None
choice = ""

while len(cards) > 0:
    last_card = current_card            # shift the current card to last card
    index = rd.randint(0, len(cards)-1) # randomise a card
    current_card = cards.pop(index)     # pop the card
    print(f"The current card is {current_card}")

    # Show the guess result
    if last_card and choice:
        if to_value(last_card) < to_value(current_card):
            if choice == "L":
                print("You lose! The card is higher.")
            else:
                print("You win! The card is higher.")
        elif to_value(last_card) > to_value(current_card):
            if choice == "L":
                print("You win! The card is lower.")
            else:
                print("You lose! The card is lower.")
        else:
            print("Draw! The value are the same!")

    # Ask for a guess
    if len(cards) > 0:
        choice = ""
        print("Do you think the next card would be higher or lower (H/L)? ")
        while choice not in ['H','L','Q']:
            choice = input("H/L (Q to quit): ").upper()
        if choice == "Q":
            exit()
    else:
        print("All cards drawn!")
