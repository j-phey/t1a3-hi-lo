import card # Importing card class from card.py
import random # Importing in-built Random Python module for shuffling the cards

# (Decided to turn this into a function)
# number = list(range(11)) # Creates a list from 0-10, i.e. number = [0, 1, 2, 3, ...]
# operator = ['+', '-', '×', '÷']

# Function for creating the initial deck of cards
def deck(): 
    number_cards = [card.Card(value, 'number') for value in range(11)]  # Creates a list from 0-10, i.e. number = [0, 1, 2, 3, ...]. Used to identify number cards as 'number'
    operator_cards = [card.Card(operator, 'operator') for operator in ['+', '-', '×', '÷']]
    return number_cards, operator_cards

# Function for shuffling the deck of cards
def shuffle_deck(cards_to_shuffle): 
    random.shuffle(cards_to_shuffle)

# Create a deck of cards using the defined lists in the deck() function
number_cards, operator_cards = deck() 
deck_of_cards = number_cards + operator_cards

# Create a shuffled deck of cards using the shuffle_deck() function
shuffle_deck(deck_of_cards) 

print('Number cards:')
for card in number_cards:
    print(f'{card.value} ', end=' ') # Using 'end' to print across a horizontal line

print('\n\nOperator cards:')
for card in operator_cards:
    print(f'{card.value} ', end=' ')

print(f'\n\nShuffled deck:')
for card in deck_of_cards:
    print(f'{card.value} ', end=' ')