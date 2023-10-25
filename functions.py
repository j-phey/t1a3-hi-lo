import random # Importing in-built Random Python module for shuffling the cards
from sympy import sympify

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

# [ARCHIVED] Function for calculating the result of a created equation
# def calculate_result2(equation):
#     equation = equation.replace('×', '*').replace('÷', '/') # Replace '×' and '÷' with '*' and '/'
#     parts = equation.split() # Using split() to break up the equation into different parts to handle / 0. split() will use spaces as the delimiter
#     result = 0 # Set default result
#     current_operator = '+' # Set default operator to start with
    
#     for part in parts:

#         if part in ('+', '-', '*', '/'): # If the current part is up to an operator, 
#             current_operator = part # ... assign it to current_operator
#         else:
#             number = float(part) # ... Otherwise assign it the current number as a float
#             if current_operator == '+':
#                 result += number
#             elif current_operator == '-':
#                 result -= number
#             elif current_operator == '*':
#                 result *= number
#             elif current_operator == '/': # Once the code reaches a division operator
#                 if number == 0: # If the proceeding number is 0,
#                     result = 0 # ... make the result 0
#                 else:
#                     result /= number # Otherwise divide the number as usual

    # return result

# [NEW] Function for calculating the result of a created equation
def calculate_result(equation): 
    equation = equation.replace('×', '*').replace('÷', '/') # Replace '×' and '÷' with '*' and '/' so the evaluation makes sense in Python

    try:
        result = eval(equation) # Use the eval() function to calculate the equation as a string
        if isinstance(result, (int, float)): # Checking if the result is either an int or float
            return round(float(result), 2) # Round the result to two decimal places
        else:
            return 'This is not a valid result. Please try again.'
    except:
        return 'This is not a valid equation'