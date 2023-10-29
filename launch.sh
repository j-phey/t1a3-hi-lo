#!/bin/bash

# Check if Python is installed
if ! [[ -x "$(command -v python)" ]]; then 
    echo 'Error: It looks like Python is not installed. You will need Python to run this game. 
        To install Python, check out https://www.python.org/downloads/'
    exit 1
fi

# Check if the virtual environment (.venv) exists
if [ ! -d .venv ]; then
    echo 'Creating a virtual environment...'
    python -m venv .venv
fi

# Activates the virtual environment
source .venv/bin/activate

# Installs the required packages from requirements.txt
pip install -r requirements.txt

# Run the main game code
python main.py

# Deactivates the virtual environment when the game is exited
deactivate