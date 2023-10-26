# --- IMPORT CLASSES, MODULES AND PACKAGES ---
from functions import Card, deck, shuffle_deck, deal_cards, calculate_result, calculate_score, load_high_score

# --- DEFINING VARIABLES ---
high_score = 0

# --- CREATE DECK OF CARDS ---

# Create an initial deck of cards using the defined lists in the deck() function
number_cards, operator_cards = deck() 
deck_of_cards = number_cards + operator_cards

# With that deck, create it into a shuffled deck of cards using the shuffle_deck() function
shuffled_deck = shuffle_deck(deck_of_cards) 

# --- DEAL THE CARDS ---

player_hand = [] # Creates an empty hand or list for the player
deal_cards(player_hand, shuffled_deck) # From the now shuffled deck, deals the cards into the players hand 

print('\nYour current hand:\n')
for index, card in enumerate(player_hand):
    print(f'{index+1}: {card.value}')

# --- USER INPUT: HI OR LO CHOICE ---

print('\nMake an equation closest to Hi (20) or Lo (1)')
hilo_choice = input('Type Hi or Lo and hit Enter: ')

while hilo_choice.lower() not in ['hi', 'lo']: # lower() ensures that Hi/hi and Lo/lo are accepted as input
    hilo_choice = input('Type Hi or Lo and hit Enter: ')

hi = 20
lo = 1

if hilo_choice.lower() == 'hi':
    target = hi
else:
    target = lo

# --- USER INPUT: ORDER OF CARDS

played_cards = [] # Create an empty list for the player to hold their inputted equation

print('\nChoose the order to play your cards...')

# --- PERFORM CHECKS ON USER INPUT ---

while len(played_cards) < 7: # While the players list of played cards is less than 7 cards...
    try: # Try this, and print the except at the bottom if it's not valid
        user_input = input(f'\nEnter card #{len(played_cards)+1} to play: ') # Store the players input as an entered_card_number int
        
        if user_input.lower() == '/reset': # Allow the user to /reset the current equation at any point
            played_cards = []
            print('Equation reset. You can start again.')
            continue

        entered_card_number = int(user_input)

        if 1 <= entered_card_number <= 7: # If input is in between 1 and 7 (incl.), add that card to the players hand
            chosen_card = player_hand[entered_card_number-1]

            if chosen_card in played_cards: # If the input is already in the played cards list, tell the player
                print(f'You have already played that card.')
            
            elif chosen_card.card_type == 'number': # Ensures that the first card played is a number
                if len(played_cards) == 0:
                    played_cards.append(chosen_card)
                elif played_cards[-1].card_type == 'operator': # Ensures that an operator is played after a number

                    if chosen_card.value == 0 and played_cards[-1].value == '÷': # Ensures that 0 cannot be played after a division symbol
                        print('Cannot divide by zero')
                    else:
                        played_cards.append(chosen_card)

                else:
                    print('Your next card must be an operator.')
            
            elif chosen_card.card_type == 'operator': # Ensures that a number is played after an operator
                if len(played_cards) > 0 and played_cards[-1].card_type == 'number':
                    played_cards.append(chosen_card)
                else:
                    print('Your next card must be a number.')
            
            else:('Your next card must be an operator')
                
        else: # If input is not between 1 and 7 (incl.), tell the player
            print('\nPlease enter a number from 1 to 7')
    
    except: # Checks for valid int
        print('\nPlease only enter valid numbers from 1 to 7')

# --- DISPLAY EQUATION ---

print('\nThis is your equation:')
for card in played_cards:
    equation = print(f'{card.value}', end=' ')

# --- CALCULATE EQUATION RESULT---

result = calculate_result(" ".join(str(card.value) for card in played_cards))

# -- CALCULATE DIFFERENCE BETWEEN EQUATION AND Hi/Lo

difference = abs(result - target) # Want difference to be an absolute value
round_score = calculate_score(difference) 

print(f'\nResult: {result}')
print(f'You were {difference} away from {hilo_choice}!')
print(f'Round score: {round_score}')

if round_score > high_score: # If the player's round score is greater than the high score
    high_score = round_score # Save the round score as the high score
    print(f'New high score! {high_score}')

    with open('high_score.txt', 'w') as f: # Print the new high score to a file to maintain the high score
        f.write(str(high_score))

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