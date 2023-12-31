import random  # Importing Random Python module for shuffling (package #1)

# --- CLASSES ---

class Card:
    def __init__(self, value, card_type):  # initialise the class first!
        self.value = value  # Holds the value of the card, e.g. 1, 2 or +
        self.card_type = card_type  # Holds the type of card

# --- FUNCTIONS ---

# Function for loading and maintaing the high score file
def load_high_score():
    try:
        with open('high_score.txt', 'r') as f:  # Open high score as read only
            high_score = int(f.read())  # Convert the read content into an int
    except FileNotFoundError:  # If no high_score found, set high_score to 0
        high_score = 0
    return high_score

# Function for creating the initial deck of cards
def deck():
    # Creates a list from 0-10. Used to identify number cards as 'number'
    number_cards = [
        Card(value, 'number')
        for value in range(11)
    ]
    operator_cards = [
        Card(operator, 'operator')
        for operator in ['+', '-', '×', '÷']
    ]
    return number_cards, operator_cards

# Function for shuffling the deck of cards
def shuffle_deck(cards_to_shuffle):
    random.shuffle(cards_to_shuffle)
    return cards_to_shuffle

# Function for dealing 4 number cards and 3 operator cards
def deal_cards(player_hand, shuffled_deck):
    num_number_cards = 0  # Sets the initial amount of number cards
    num_operator_cards = 0  # Sets the initial amount of operator cards

    for card in shuffled_deck:  # Start iterating through the shuffled deck
        # If there are less than 5 number cards that have been dealt...
        if card.card_type == 'number' and num_number_cards < 4:
            player_hand.append(card)  # Put it in the player_hand list
            num_number_cards += 1
        # If there are less than 4 operator cards that have been dealt..
        elif card.card_type == 'operator' and num_operator_cards < 3:
            player_hand.append(card)
            num_operator_cards += 1

        # Once 4 numbers and 3 operators have been dealt, break the loop
        if num_number_cards == 4 and num_operator_cards == 3:
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

# Function for calculating the result of a created equation
def calculate_result(equation):
    equation = equation.replace('×', '*').replace('÷', '/')  # Replace '×' and '÷' with '*' and '/' so the evaluation makes sense in Python

    try:
        result = eval(equation)  # Use the eval() function to calculate the equation as a string
        if isinstance(result, (int, float)):  # Checking if the result is either an int or float
            return round(float(result), 2)  # Round the result to two decimal places
        else:
            return 'This is not a valid result. Please try again.'
    except Exception as invalid:
        return 'This is not a valid equation'

# Function for scoring scale

def calculate_score(difference):
    if difference == 0:
        return 100
    elif difference <= 0.5:
        return 95
    elif difference <= 1:
        return 90
    elif difference <= 1.5:
        return 85
    elif difference <= 2:
        return 80
    elif difference <= 2.5:
        return 75
    elif difference <= 3:
        return 70
    elif difference <= 3.5:
        return 65
    elif difference <= 4:
        return 60
    elif difference <= 4.5:
        return 55
    elif difference <= 5:
        return 50
    elif difference <= 5.5:
        return 45
    elif difference <= 6:
        return 40
    elif difference <= 6.5:
        return 35
    elif difference <= 7:
        return 30
    elif difference <= 7.5:
        return 25
    elif difference <= 8:
        return 20
    elif difference <= 8.5:
        return 15
    elif difference <= 9:
        return 10
    else:
        return 5
