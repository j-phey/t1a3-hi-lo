# Coder Academy - T1A3 - Jonathan Phey

### GitHub Repo
[**t1a3 hi-lo** - GitHub repository link](https://github.com/jjjjjjpppppp/t1a3-hi-lo)

### Features

### How to install

- python3 main.py
- pip install colorama
- pip install rich
- ./run_game.sh

### Implementation Plan

- I used Linear
- Generally took a snapshot of plan at the midday point and when I would stop finish coding for the day 
- I moved the Done tasks to an archive daily, to keep the list clean
- Generally I moved tasks to the 'Todo' column when I wanted to attempt to complete it that day, while attempting to clear 'In progress' as a priority (besides the Slide deck and README files, which were constants)

### Tech stack

- **Programming language:** Python
- **Version control:** [GitHub](https://github.com/jjjjjjpppppp/)
- **Project management:** [Linear](https://linear.app/)
- **Slide deck:** [Google Slides](https://workspace.google.com/intl/en/products/slides/)

### Programming language style Guide
[PEP 8](https://peps.python.org/pep-0008/) – Style Guide for Python Code 

### Description
Create a card game that focuses on problem solving and maths, where a player will attempt to rearrange a dealt hand of number cards and operators to create an equation that is closest to 20 or 1

### How to play
- The player will be handed seven cards, which consist of:
 - Four number cards (randomly chosen from 0 to 10)
 - Three operator cards (randomly chosen from +, -, ×, ÷) 
 
 - Something about /reset
 - Type /quit at the end of round to exit game
 - Can always exit with Ctrl+Z

### Rules
- Using these seven cards, the player must rearrange the seven cards into a valid equation, following the BODMAS order 
- After the player receives their four number cards and three operator cards, they will choose to 'bet' on **Hi** or **Lo**, where 
  - **Hi** means they will attempt to make an equation that is closest to the value 20, and 
  - **Lo** means they will make an equation that is closest to the value of 1
- Once Hi or Lo is chosen, using their dealt hand, the player will input their equation from left to right 
- The output will include:
  - Hi / Lo chosen 
  - The entered equation and what it equates to
  - The difference between Hi / Lo and the created equation
     - The difference will always be shown as a positive number
  - The score for the round and total score so far

### Scoring *(I'm still thinking through this...)*
- Total score will be based on three rounds of Hi-Lo
- The player will get a max of 100 points per round for getting exactly Hi or Lo, and the round score will reduce as they get further away from Hi or Lo

### Assume
- Dividing by zero (0) is not allowed
- The equation doesn't need to be a whole number and can be a value with decimal places

***Some stretch goals or things I want to explore, but not sure if I know how to implement:***
- Including a square root card as an option to the randomly chosen operators
- The ability to play with a second player
- The ability to play against a dealer
- An option to have a timer or not
- Saving the high score somewhere (probably only possible for each instance of the game for now)

### References

van Rossum, G., Warsaw, B., & Coghlan, A. (2023, October 11). PEP 8 – Style Guide for Python Code. Python PEP. Retrieved October 20, 2023, from https://peps.python.org/pep-0008/