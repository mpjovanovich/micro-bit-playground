# Run these commands one at a time in powershell
# Requires usbipd to be installed via winget
usbipd list # Get the appropriate ID
usbipd bind --busid 1-1
usbipd attach --wsl --busid 1-1

# Then from linux:
python -m serial.tools.miniterm /dev/ttyACM0 115200