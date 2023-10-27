# Check if Python is installed
if ! [[ -x "$(command -v python)" ]]; 
then 
    echo 'Error: 
        It looks like Python is not installed. You will need Python to run this game.
        To install Python, check out https://www.python.org/downloads/'
    exit 1
fi