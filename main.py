# --- IMPORT CLASSES, MODULES AND PACKAGES ---
from functions import Card, deck, shuffle_deck, deal_cards

# --- CREATE DECK OF CARDS ---

# Create an initial deck of cards using the defined lists in the deck() function
number_cards, operator_cards = deck() 
deck_of_cards = number_cards + operator_cards

# With that deck, create it into a shuffled deck of cards using the shuffle_deck() function
shuffled_deck = shuffle_deck(deck_of_cards) 

# --- DEAL THE CARDS ---

player_hand = [] # Creates an empty hand or list for the player
deal_cards(player_hand, shuffled_deck) # From the now shuffled deck, deals the cards into the players hand 

# --- GET USER INPUT ---

print('\nYour current hand:\n')
for index, card in enumerate(player_hand):
    print(f'{index+1}: {card.value}')

played_cards = [] # Create an empty list for the player to hold their inputted equation

print('\nChoose the order to play your cards...')

while len(played_cards) < 7: # While the players list of played cards is less than 7 cards...
    try: # Try this, and print the except at the bottom if it's not valid
        entered_card_number = int(input(f'\nEnter card #{len(played_cards)+1} to play: ')) # Store the players input as an entered_card_number int

        if 1 <= entered_card_number <= 7: # If input is in between 1 and 7 (incl.), add that card to the players hand
            chosen_card = player_hand[entered_card_number-1]

            if chosen_card in played_cards: # If the input is already in the played cards list, tell the player
                print(f'You have already played that card.')
            
            elif chosen_card.card_type == 'number': 
                if len(played_cards) == 0:
                    played_cards.append(chosen_card)
                elif played_cards[-1].card_type == 'operator':
                    played_cards.append(chosen_card)
                else:
                    print('Your next card must be an operator.')
            
            elif chosen_card.card_type == 'operator':
                if len(played_cards) > 0 and played_cards[-1].card_type == 'number':
                    played_cards.append(chosen_card)
                else:
                    print('Your next card must be a number.')
            
            else:('Your next card must be an operator')
                
        else: # If input is not between 1 and 7 (incl.), tell the player
            print('\nPlease enter a number from 1 to 7')
    
    except: # Checks for valid int
        print('\nPlease only enter valid numbers from 1 to 7')

print('\nThis is your equation:')
for card in played_cards:
    print(f'{card.value}', end=' ')


# ------- Print statements to test output ---------
# print('Number cards:')
# for card in number_cards:
#     print(f'{card.value} ', end=' ') # Using 'end' to print across a horizontal line

# print('\n\nOperator cards:')
# for card in operator_cards:
#     print(f'{card.value} ', end=' ')

# print(f'\n\nShuffled deck:')
# for card in deck_of_cards:
#     print(f'{card.value} ', end=' ')

# print(f'\n\nPlayers hand:')
# for card in player_hand:
#     print(f'{card.value} ', end=' ')

# print(f'\n\nRemaining cards in deck:')
# for card in shuffled_deck:
#     print(f'{card.value} ', end=' ')