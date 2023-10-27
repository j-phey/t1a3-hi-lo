# Check if colorama is installed
if ! pip3 show colorama >/dev/null; 
then 
    echo 'Error: The required package "colorama" is not installed. Please install it by running: pip install colorama'
    exit 1
fi

# Check if rich is installed
if ! pip3 show rich >/dev/null; then
    echo 'Error: The required package "rich" is not installed. Please install it by running: pip install rich'
    exit 1
fi