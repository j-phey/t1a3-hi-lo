class Player:
    def __init__(self, name):
        self.name = name
        self.hand = [] # Creates an empty list to store the player's hand
        self.score = 0 # Default / starting value for a player's score