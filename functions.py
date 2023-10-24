import random # Importing in-built Random Python module for shuffling the cards

# --- CLASSES ---

class Card:
    def __init__(self, value, card_type): # always need to initialise the class first!
        self.value = value  # Holds the value of the card, e.g. 1, 2, 3 or - or +
        self.card_type = card_type # Holds the type of card, i.e. number or operator

# --- FUNCTIONS ---

# Function for creating the initial deck of cards
def deck(): 
    number_cards = [Card(value, 'number') for value in range(11)]  # Creates a list from 0-10, i.e. number = [0, 1, 2, 3, ...]. Used to identify number cards as 'number'
    operator_cards = [Card(operator, 'operator') for operator in ['+', '-', '×', '÷']]
    return number_cards, operator_cards

# number_cards, operator_cards = deck() 

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

# Function for displaying the players hand
