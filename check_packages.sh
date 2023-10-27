# Check if colorama is installed
if ! pip3 show colorama >/dev/null; 
then 
    echo 'Error: The game requires a package called "colorama". Please install it by typing "pip install colorama" and press Enter'
    exit 1
fi

# Check if rich is installed
if ! pip3 show rich >/dev/null; then
    echo 'Error: The game requires a package called "rich". Please install it by typing "pip install rich" and press Enter'
    exit 1
fi

# Check if art is installed
if ! pip3 show art >/dev/null; then
    echo 'Error: The game requires a package called "art". Please install it by typing "pip install art" and press Enter'
    exit 1
fi