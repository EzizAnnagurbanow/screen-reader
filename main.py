import sys
import keyboard
import espeak
# Current position on the screen
position = 0

# Read text from a file or command-line argument
text = sys.stdin.read() if len(sys.argv) <= 1 else open(sys.argv[1]).read()

def speak(text):
    # Replace 'espeak' with your preferred text-to-speech tool
    os.system(f"espeak -ven-us+f4 '{text}'")

def move_left():
    global position
    if position > 0:
        position -= 1

def move_right():
    global position
    if position < len(text):
        position += 1

def read_character():
    speak(text[position])

def read_word():
    start = position
    while position < len(text) and text[position] != " ":
        position += 1
    speak(text[start:position])

def read_line():
    start = position
    while position < len(text) and not text[position] in ("\n", "\r"):
        position += 1
    speak(text[start:position])

# Bind keyboard shortcuts to navigation and reading actions
keyboard.on_press_key('left', move_left)
keyboard.on_press_key('right', move_right)
keyboard.on_press_key('c', read_character)
keyboard.on_press_key('w', read_word)
keyboard.on_press_key('l', read_line)

# Main loop
while True:
    # Wait for user input
    keyboard.wait()
