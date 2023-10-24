# --- IMPORT CLASSES, MODULES AND PACKAGES ---
from functions import Card, deck, shuffle_deck, deal_cards

# --- CREATE DECK OF CARDS ---

# Create a deck of cards using the defined lists in the deck() function
number_cards, operator_cards = deck() 
deck_of_cards = number_cards + operator_cards

# Create a shuffled deck of cards using the shuffle_deck() function
shuffled_deck = shuffle_deck(deck_of_cards) 

# --- DEAL THE CARDS ---

player_hand = [] # Creates an empty hand or list for the player
deal_cards(player_hand, shuffled_deck) # Deals the cards from the deal_cards function

# --- GET USER INPUT ---



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