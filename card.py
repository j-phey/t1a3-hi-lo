class Card:
    def __init__(self, value, card_type): # always need to initialise the class first!
        self.value = value  # Holds the value of the card, e.g. 1, 2, 3 or - or +
        self.card_type = card_type # Holds the type of card, i.e. number or operator