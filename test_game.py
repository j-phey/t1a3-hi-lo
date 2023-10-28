from main import *
from functions import *

# --- MAIN TEST ---

# Test if the deck has 11 number cards (0-10) and 4 operator cards
def test_deck_initialization():
    number_cards, operator_cards = deck()

    assert len(number_cards) == 11
    assert len(operator_cards) == 4

# --- FUNCTION TEST ---

# Test if calculate_score() returns correct score for a difference
def test_calculate_score():
    score = calculate_score(0.2)
    assert score == 95

    score = calculate_score(4.3)
    assert score == 55

# Test calculate_result() to ensure equations are calculated correctly
def test_calculate_result():
    # Test addition
    assert calculate_result("1 + 4") == 5
    # Test subtraction
    assert calculate_result("5 - 3") == 2
    # Test multiplication
    assert calculate_result("10 * 4") == 40
    # Test division
    assert calculate_result("2 / 8") == 0.25
