# --- IMPORT CLASSES, MODULES AND PACKAGES ---
from functions import Card, deck, shuffle_deck, deal_cards, calculate_result, calculate_score, load_high_score
from rich import * # Importing rich for further text formatting (package #2)
from rich.console import Console
from colorama import Fore, Back, Style, init # Importing colorama to colour input text (package #3)
init()
from art import * # Importing art for ASCII banner (package #4)

# --- DEFINING VARIABLES ---
console = Console()
high_score = load_high_score()
equation_display = ""

# --- WELCOME BANNER AND INTRODUCTION ---

tprint("HI-LO\n",font="tarty1")

print('Hi there! Welcome to [bold cyan]Hi[/bold cyan]-[bold yellow]Lo[/bold yellow]!')
print('The aim of this game is to create an equation that is closest to or equal to [bold cyan]Hi (20)[/bold cyan] or [bold yellow]Lo (1)[/bold yellow].')
print('Try to beat your high score each round! If you would like a break, type [pink]/quit[/pink] at the end of the round.')

if __name__ == "__main__": # Separates the code from when it's being used by pytest

# --- MAIN GAME LOOP ---
    play_game = True # Remain true until player types /quit at the end

    while play_game:

            # --- SINGLE ROUND LOOP ---
            while True:
                
                # --- CREATE DECK OF CARDS ---

                # Create an initial deck of cards using the defined lists in the deck() function
                number_cards, operator_cards = deck() 
                deck_of_cards = number_cards + operator_cards

                # With that deck, create it into a shuffled deck of cards using the shuffle_deck() function
                shuffled_deck = shuffle_deck(deck_of_cards) 
                
                # --- DEAL THE CARDS ---

                player_hand = [] # Creates an empty hand or list for the player
                deal_cards(player_hand, shuffled_deck) # From the now shuffled deck, deals the cards into the players hand 

                print('\nHere are your cards! Make an equation equal or closest to [bold cyan]Hi (20)[/bold cyan] or [bold yellow]Lo (1)[/bold yellow]:\n')
                for index, card in enumerate(player_hand):
                    console.print(f'[dim]{index+1}[/dim]: [green]{card.value}[/green]', highlight=False) # Prevent rich from colouring the index numbers

                # --- USER INPUT: HI OR LO CHOICE ---

                hilo_choice = input('\nType ' + Fore.CYAN + 'Hi ' + Style.RESET_ALL + 'or ' + Fore.YELLOW + 'Lo ' + Style.RESET_ALL + 'and hit Enter: ')

                while hilo_choice.lower() not in ['hi', 'lo']: # lower() ensures that Hi/hi and Lo/lo are accepted as input
                    hilo_choice = input('Type ' + Fore.CYAN + 'Hi ' + Style.RESET_ALL + 'or ' + Fore.YELLOW + 'Lo ' + Style.RESET_ALL + 'and hit Enter: ')

                hi = 20
                lo = 1

                if hilo_choice.lower() == 'hi':
                    target = hi
                else:
                    target = lo

                # --- USER INPUT: ORDER OF CARDS

                played_cards = [] # Create an empty list for the player to hold their inputted equation

                if hilo_choice.lower() == 'hi':
                    console.print(f'\nYou chose [bold cyan]{hilo_choice}[/bold cyan]! Type the card ([dim bold]1-7[/dim bold]) and hit Enter to place it. Type [purple]/reset[/purple] to restart your placed cards.', highlight=False)
                else:
                    console.print(f'\nYou chose [bold yellow]{hilo_choice}[/bold yellow]! Type the card ([dim bold]1-7[/dim bold]) and hit Enter to place it. Type [purple]/reset[/purple] to restart your placed cards.', highlight=False)

                # --- PERFORM CHECKS ON USER INPUT ---

                while len(played_cards) < 7: # While the players list of played cards is less than 7 cards...
                    try: # Try this, and print the except at the bottom if it's not valid
                        user_input = input(f'\nEnter card #{len(played_cards)+1} to play: ') # Store the players input as an entered_card_number int
                        
                        if user_input.lower() == '/reset': # Allow the user to /reset the current equation at any point
                            played_cards = []
                            equation_display = "" # Resets the equation being displayed
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

                            # Updating the current equation being displayed
                            current_equation = " ".join(str(card.value) for card in played_cards)
                            equation_display = console.print(f'\nCurrent equation: {current_equation}', highlight=False)
                                
                        else: # If input is not between 1 and 7 (incl.), tell the player
                            print('\nPlease enter a number from 1 to 7')
                    
                    except: # Checks for valid int
                        print('\nPlease only enter valid numbers from 1 to 7')


                # --- DISPLAY EQUATION ---

                print('\nThis is your equation:\n')
                for card in played_cards:
                    equation = print(f'{card.value}', end=' ')

                # --- CALCULATE EQUATION RESULT---

                result = calculate_result(" ".join(str(card.value) for card in played_cards))

                # -- CALCULATE DIFFERENCE BETWEEN EQUATION AND Hi/Lo

                difference = abs(result - target) # Want difference to be an absolute value
                round_score = calculate_score(difference) 

                print(f'\n= {result}')
                print(f'\nYou were {difference} away from {hilo_choice}!')
                print(f'\nRound score: {round_score}')
                print(f'Current high score: {high_score}')

                if round_score > high_score: # If the player's round score is greater than the high score
                    high_score = round_score # Save the round score as the high score
                    print(f'Congratulations! New high score: {high_score}')

                    with open('high_score.txt', 'w') as f: # Print the new high score to a file to maintain the high score
                        f.write(str(high_score))
                
                play_again = input('\nTry again? Type /quit to exit or press Enter to play again: ') # Ask the user if they want to play again
                if play_again.lower() == '/quit': # Break the game loop if they type quit
                    play_game = False
                    break

