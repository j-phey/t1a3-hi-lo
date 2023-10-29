# Coder Academy - T1A3 - Jonathan Phey

## Terminal application: Hi-Lo Game

### GitHub Repo
[**t1a3 hi-lo** - GitHub repository link](https://github.com/jjjjjjpppppp/t1a3-hi-lo)

### Hi-Lo game description
"Hi-Lo" is a captivating card game that challenges your math and problem solving skills. Create equations using cards to hit a target number (20 for 'Hi' or 1 for 'Lo'). It's a fun way to boost your math abilities — try to beat your high score each round!

### Features

- **Creates a unique deck of cards**
  - Generates a deck of cards that includes numbers (0-10) and operators (+, -, ×, ÷)
- **Deals cards to the player**
  - Receive 4 number cards and 3 operator cards at random, dealing you a challenging hand for every round
- **Players can choose to target Hi (20) or Lo (1)**
  - Pick your target, Hi (20) or Lo (1), and test your problem solving and math skills.
- **Player can rearrange cards and input equation**
  - Engage in interactive equation creation, combining different cards to form an equation
- **Equation calculation**
  - See your equations appear in real-time, providing immediate feedback
- **Display result and score**
  - View your equation result and score and try to beat your personal high score
- **Aesthetically pleasing terminal interface**
  - Enjoy a visually appealing terminal interface with rich text formatting

### How to install

1. Download the game files from [GitHub](https://github.com/jjjjjjpppppp/t1a3-hi-lo)
   - On the GitHub page, click on `Code` > `Download Zip`
   ![Download instructions](./docs/download.png 'Download instructions')
2. Open a new Terminal window and use `cd` to navigate to the 't1a3-hi-lo-main' > 'src' folder downloaded. 
3. Once the Terminal is in the right 'src' folder, run ```bash launch.sh```
   - This command will look for Python, activate a virtual environment and install the required dependencies to run the game.
4. If `bash launch.sh` is successfully run with all the necessary packages installed, the Hi-Lo game should begin right away. You should see this welcome message:
   ![Welcome screen](./docs/welcome.png 'Welcome screen')

### How to play
- The player will be handed seven cards, which consist of:
  - Four number cards (randomly chosen from 0 to 10)
  - Three operator cards (randomly chosen from +, -, ×, ÷) 
- Once the cards have been dealt, choose Hi or Lo to make an equation that is closest to 20 or 1 respectively
- Place cards one-by-one by entering the corresponding number for each card
- Once an equation is successfully made, a score will be given, depending on how close the player gets to Hi (20) or Lo (1)
- The player's high score will be updated when it's beaten!

### Rules
- When making an equation, type `/reset` to restart the equation
- At the end of the round, type `/quit` to exit out of the app
- A number card must be placed first, followed by an operator, and so on, until a valid equation is made
- Dividing by zero (0) is not allowed
- The equation doesn't need to amount to a whole number and can be a value with decimal places

### Hardware / software requirements

- 100MB free disk space
- Python 3 or higher
- Terminal application that can support `bash` scripts and Python

## How Hi-Lo was built

### Software development and implementation plan

- To build my plan and track my tasks and timelines, I utilised [Linear](https://linear.app/)
- Generally, I took two screenshots of my plan every day - at the mid point of my working day and when I decided to stop coding
- I moved the `Done` tasks to an archive daily, to keep the list clean
- Most days, I moved tasks to the `Todo` column when I wanted to attempt to complete it on a given day, while attempting to clear `In progress` as a priority (besides the slide deck and README files, which were constants)

- 19 October 2023
![Plan screenshot 1](./docs/2023-10-19_5.39.17pm.png 'Plan screenshot 2023-10-19_5.39.17pm')
- 20 October 2023
![Plan screenshot 2](./docs/2023-10-20_3.45.43pm.png 'Plan screenshot 2023-10-20_3.45.43pm')
![Plan screenshot 3](./docs/2023-10-20_6.16.12pm.png 'Plan screenshot 2023-10-20_6.16.12pm')
- 23 October 2023
![Plan screenshot 4](./docs/2023-10-23_2.59.25pm.png 'Plan screenshot 2023-10-23_2.59.25pm')
![Plan screenshot 5](./docs/2023-10-23_5.54.43pm.png 'Plan screenshot 2023-10-23_5.54.43pm')
- 24 October 2023
![Plan screenshot 6](./docs/2023-10-24_2.56.14pm.png 'Plan screenshot 2023-10-24_2.56.14pm')
![Plan screenshot 7](./docs/2023-10-24_5.46.31pm.png 'Plan screenshot 2023-10-24_5.46.31pm')
- 25 October 2023
![Plan screenshot 8](./docs/2023-10-25_7.27.03pm.png 'Plan screenshot 2023-10-25_7.27.03pm')
![Plan screenshot 9](./docs/2023-10-25_8.44.00pm.png 'Plan screenshot 2023-10-25_8.44.00pm')
- 26 October 2023
![Plan screenshot 10](./docs/2023-10-26_2.43.23pm.png 'Plan screenshot 2023-10-26_2.43.23pm')
![Plan screenshot 11](./docs/2023-10-26_6.07.59pm.png 'Plan screenshot 2023-10-26_6.07.59pm')
- 27 October 2023
![Plan screenshot 12](./docs/2023-10-27_7.05.11pm.png 'Plan screenshot 2023-10-27_7.05.11pm')
![Plan screenshot 13](./docs/2023-10-27_12.09.46pm.png 'Plan screenshot 2023-10-27_12.09.46pm')
- 28 October 2023
![Plan screenshot 14](./docs/2023-10-28_5.06.56pm.png 'Plan screenshot 2023-10-28_5.06.56pm')
- 29 October 2023
![Plan screenshot 15](./docs/2023-10-29_6.01.26pm.png 'Plan screenshot 2023-10-29_6.01.26pm')

### Programming language style Guide
[PEP 8](https://peps.python.org/pep-0008/) – Style Guide for Python Code 

### Python package dependencies
- colorama==0.4.6
- rich==13.6.0
- art==6.1

### Tech stack

- **Programming language:** Python, shell
- **Version control:** [GitHub](https://github.com/jjjjjjpppppp/)
- **Project management:** [Linear](https://linear.app/)
- **Slide deck:** [Google Slides](https://workspace.google.com/intl/en/products/slides/)

### References

- Gurav, S. (2022, November 21). Pass vs. Continue in Python Explained. Built In. Retrieved October 26, 2023, from https://builtin.com/software-engineering-perspectives/pass-vs-continue-python
- Haghighi, S., & Khanalizadeh, A. (n.d.). art · PyPI. PyPI. Retrieved October 27, 2023, from https://pypi.org/project/art/
- Hartley, J. (n.d.). colorama · PyPI. PyPI. Retrieved October 26, 2023, from https://pypi.org/project/colorama/
- McGugan, W. (n.d.). rich · PyPI. PyPI. Retrieved October 27, 2023, from https://pypi.org/project/rich/
- Parewa Labs. (n.d.-a). Python eval(). Programiz. Retrieved October 25, 2023, from https://www.programiz.com/python-programming/methods/built-in/eval
- Parewa Labs. (n.d.-b). Python String split(). Programiz. Retrieved October 25, 2023, from https://www.programiz.com/python-programming/methods/string/split
- Parewa Labs. (n.d.-c). Python isinstance(). Programiz. Retrieved October 25, 2023, from https://www.programiz.com/python-programming/methods/built-in/isinstance
- Refsnes Data. (n.d.-a). Python Random Module. W3Schools. Retrieved October 23, 2023, from https://www.w3schools.com/python/module_random.asp
- Refsnes Data. (n.d.-b). Python print() Function. W3Schools. Retrieved October 23, 2023, from https://www.w3schools.com/python/ref_func_print.asp
- Refsnes Data. (n.d.-c). Python enumerate() Function. W3Schools. Retrieved October 24, 2023, from https://www.w3schools.com/python/ref_func_enumerate.asp
- Refsnes Data. (n.d.-d). Python Try Except. W3Schools. Retrieved October 24, 2023, from https://www.w3schools.com/python/python_try_except.asp
- Refsnes Data. (n.d.-e). Python String join() Method. W3Schools. Retrieved October 24, 2023, from https://www.w3schools.com/python/ref_string_join.asp
- Refsnes Data. (n.d.-f). Python String replace() Method. W3Schools. Retrieved October 25, 2023, from https://www.w3schools.com/python/ref_string_replace.asp
- Rocholl, J. C. (n.d.). pycodestyle · PyPI. PyPI. Retrieved October 28, 2023, from https://pypi.org/project/pycodestyle/
- van Rossum, G., Warsaw, B., & Coghlan, A. (2023, October 11). PEP 8 – Style Guide for Python Code. Python PEP. Retrieved October 20, 2023, from https://peps.python.org/pep-0008/