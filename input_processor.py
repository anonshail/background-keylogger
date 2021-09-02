import keyboard  # using module keyboard

# holds the value of the previous keypress to avoid multiple fires
lastKeyPress = None

while True:
    if(keyboard.is_pressed('1') and lastKeyPress != 1):
        lastKeyPress = 1
        print("Do something when ", lastKeyPress, " is pressed")
    if(keyboard.is_pressed('2') and lastKeyPress != 2):
        lastKeyPress = 2
        print("Do something when ", lastKeyPress, " is pressed")
    if(keyboard.is_pressed('3') and lastKeyPress != 3):
        lastKeyPress = 3
        print("Do something when ", lastKeyPress, " is pressed")
    if(keyboard.is_pressed('4') and lastKeyPress != 4):
        lastKeyPress = 4
        print("Do something when ", lastKeyPress, " is pressed")
    if(keyboard.is_pressed('5') and lastKeyPress != 5):
        lastKeyPress = 5
        print("Do something when ", lastKeyPress, " is pressed")
    if(keyboard.is_pressed('6') and lastKeyPress != 6):
        lastKeyPress = 6
        print("Do something when ", lastKeyPress, " is pressed")
    if(keyboard.is_pressed('7') and lastKeyPress != 7):
        lastKeyPress = 7
        print("Do something when ", lastKeyPress, " is pressed")
    if(keyboard.is_pressed('8') and lastKeyPress != 8):
        lastKeyPress = 8
        print("Do something when ", lastKeyPress, " is pressed")
    if(keyboard.is_pressed('9') and lastKeyPress != 9):
        lastKeyPress = 9
        print("Do something when ", lastKeyPress, " is pressed")