from main import *
from functions import *

# --- MAIN TEST ---

# Test if the deck has 11 number cards (0-10) and 4 operator cards
def test_deck_initialization():
    number_cards, operator_cards = deck()
    
    assert len(number_cards) == 11  
    assert len(operator_cards) == 4  

# --- FUNCTION TEST ---

# Test if calculate_score() returns the correct score for a given difference from hi or lo
def test_calculate_score(): 
    
    score = calculate_score(0.2)
    assert score == 95  

    score = calculate_score(4.3)
    assert score == 55  