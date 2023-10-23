# --- IMPORT CLASSES, MODULES AND PACKAGES ---
import card # Importing card class from card.py
import random # Importing in-built Random Python module for shuffling the cards

# --- FUNCTIONS ---

# Function for creating the initial deck of cards
def deck(): 
    number_cards = [card.Card(value, 'number') for value in range(11)]  # Creates a list from 0-10, i.e. number = [0, 1, 2, 3, ...]. Used to identify number cards as 'number'
    operator_cards = [card.Card(operator, 'operator') for operator in ['+', '-', '×', '÷']]
    return number_cards, operator_cards

# Function for shuffling the deck of cards
def shuffle_deck(cards_to_shuffle): 
    random.shuffle(cards_to_shuffle)
    return cards_to_shuffle

# Function for dealing 4 number cards and 3 operator cards
def deal_cards(player_hand, shuffled_deck):
    num_number_cards = 0 # Sets the initial amount of number cards 
    num_operator_cards = 0 # Sets the initial amount of operator cards 

    for card in shuffled_deck: # Start iterating through the shuffled deck
        if card.card_type == 'number' and num_number_cards < 4: # If there are less than 5 number cards that have been dealt
            player_hand.append(card) # Put it in the player_hand list
            num_number_cards += 1 
        elif card.card_type == 'operator' and num_operator_cards < 3: # If there are less than 4 operator cards that have been dealt
            player_hand.append(card)
            num_operator_cards += 1
        
        if num_number_cards == 4 and num_operator_cards == 3: # Once 4 numbers and 3 operator cards have been dealt, break out of the loop
            break 
    
    for card in player_hand:
        shuffled_deck.remove(card)

# --- CREATE DECK OF CARDS ---

# Create a deck of cards using the defined lists in the deck() function
number_cards, operator_cards = deck() 
deck_of_cards = number_cards + operator_cards

# Create a shuffled deck of cards using the shuffle_deck() function
shuffled_deck = shuffle_deck(deck_of_cards) 

# --- DEAL THE CARDS ---

player_hand = [] # Creates an empty hand or list for the player
deal_cards(player_hand, shuffled_deck) # Deals the cards from the deal_cards function



# ------- Print statements to test output ---------
print('Number cards:')
for card in number_cards:
    print(f'{card.value} ', end=' ') # Using 'end' to print across a horizontal line

print('\n\nOperator cards:')
for card in operator_cards:
    print(f'{card.value} ', end=' ')

print(f'\n\nShuffled deck:')
for card in deck_of_cards:
    print(f'{card.value} ', end=' ')

print(f'\n\nPlayers hand:')
for card in player_hand:
    print(f'{card.value} ', end=' ')

print(f'\n\nRemaining cards in deck:')
for card in shuffled_deck:
    print(f'{card.value} ', end=' ')