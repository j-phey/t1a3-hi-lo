import card

# number = list(range(11)) # Creates a list from 0-10, i.e. number = [0, 1, 2, 3, ...]
# operator = ['+', '-', '×', '÷']

def deck(): # Creates the deck of cards as a function
    number_cards = [card.Card(value, 'number') for value in range(11)]  # Creates a list from 0-10, i.e. number = [0, 1, 2, 3, ...]. Used to identify number cards as 'number'
    operator_cards = [card.Card(operator, 'operator') for operator in ['+', '-', '×', '÷']]
    return number_cards, operator_cards

number_cards, operator_cards = deck()

print('Number cards:')
for card in number_cards:
    print(f'{card.value} {card.card_type}')

print('Operator cards:')
for card in operator_cards:
    print(f'{card.value} {card.card_type}')