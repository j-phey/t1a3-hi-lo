#!/bin/bash

# Check if Python is installed
if ! [[ -x "$(command -v python3)" ]]; then 
    echo 'Error: It looks like Python 3 is not installed. You will need Python to run this game. 
        To install Python 3, check out https://www.python.org/downloads/'
    exit 1
fi

# Check if the virtual environment (.venv) exists
if [ ! -d .venv ]; then
    echo 'Creating a virtual environment...'
    python3 -m venv .venv
fi

# Activates the virtual environment
source .venv/bin/activate

# Installs the required packages from requirements.txt
pip install -r requirements.txt

# Run the main game code
python3 main.py

# Deactivates the virtual environment when the game is exited
deactivate